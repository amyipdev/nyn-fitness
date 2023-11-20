<div align="center">

<img alt="NYN Fitness" src="https://media.discordapp.net/attachments/753662266305413353/1176006224916004905/image.png" />

</div>

---

**NYN Fitness** is a dynamic-recommendations workout app designed to provide users
with the most relevant workout recommendations for their individual preferences and
goals. It provides:

- 🚀 A simple, clean, responsive interface
- 📱 Many available platforms (web, Linux, Windows, macOS, Android and iOS via PWAs)
- ⚙️ Configurable attributes which change recommendation results
- 🖥️ A robust API for connecting to personal scripts/existing health components
- 🏃‍♀️ Easy self-deployment to customize workout libraries

NYN is covered under the GNU Affero General Public License, version 3.0 or later;
you have the right to receive the source code behind any NYN deployment.

## Installation

### End Users

We maintain a deployment of NYN at https://main.dev362.amyip.net. You can simply log
into that instance to use NYN!

If you want an app version:

#### iOS/Android

The specific web browser you're using changes the specific method; however, most
mobile web browsers will let you install PWAs (which NYN is shipped as). All of
these require you first visit the web deployment; however, you do not need to log
in. 

For Chrome on Android, click the kebab menu (three dots, top right corner)
and look for "Install app". This will put the app in your app drawer, and from
there you can place it on your home screen.

For Safari on iOS, click the Share button, and then click "Add to home screen".
You can then configure it to your liking.

#### Windows

We currently only ship a "portable" version of NYN for Windows. You can find this
in the most recent release on the Releases tab. Portable versions execute as a file,
but don't "install" to your system; this may be more inconvienent. If you're on
Microsoft Edge, you can use the web version by clicking "Install app" to install it
as a PWA; this is still largely equivalent.

If you'd like to see a properly-installable version of NYN for Windows, contribute
to NYN by submitting a Pull Request.

#### macOS/Darwin

NYN for macOS is shipped as a Zip archive in Releases. Download that archive and
double-click on it in Finder to extract it. From there, you can take the NYN icon
(appears as an atom on macOS) and drag it into your Applications folder; this will
install NYN. If you want to use the app in portable mode, you can double-click it,
and it will still execute correctly.

#### Linux

If you use a dpkg-based distribution (like Debian, Ubuntu, and Linux Mint), you can
use the .deb file in Releases.

If you use an RPM-based distribution (like Fedora, RHEL, CentOS, Rocky, and SUSE),
you can use the .rpm file in Releases.

We don't ship any other packaging formats currently for NYN, and we recommend using
the web version. Some browsers may allow you to install the app to your system as
a PWA; this is known to work on Firefox, through extensions, and natively on Edge.
You can also download the source code and use the `electron` folder to run/package
natively yourself.

#### Other systems

We do not currently have support for desktop apps on any other operating systems.
You can use the web version, or use a browser with PWA support to install as a PWA.

### Deployment

Prerequsites:
- A MySQL or MariaDB database set up with the tables in the `setup` folder.
- A Linux server with modern build tools (gcc/g++), Python 3, nodejs/npm, and Make.
- (Optional) a Cron implementation (such as Cronie) that supports `@weekly`

First, clone the repository:

```sh
git clone https://github.com/amyipdev/nyn-fitness
```

Then, use the interactive generator to make a config file:

```sh
cd nyn-fitness
python3 gen_config.py
```

Now, run the server (perhaps in a terminal multiplexer like `tmux`):

```sh
./run.sh
```

To keep your database size reasonable on large instances, install the crontab:

```sh
cron/insert-crontab.sh
```

#### Adding workouts

Your NYN instance will not initially have content. You can add workouts using:

```sh
python3 setup/input_workouts.py
```

#### SSL/TLS

NYN currently does not ship with SSL. However, you can use a reverse proxy
(we recommend NGINX) to enable SSL support with free certificates from Let's Encrypt.

## Contributing

To report bugs, use the Issues tab. To submit changes (which will be under AGPLv3),
use the Pull Requests tab. To report security vulnerabilities, email amy@amyip.net.

## Licensing/Credits

This project was made by Amy Parker, Nicholas Goulart, Kevin Ramirez, Theresa Nguyen,
Srinidhi Chevvuri, and Dat Lam. © Copyright 2023.

NYN is licensed under the AGPLv3. You can view the license in the LICENSE file.

Credits go out to the following libraries/toolchains/frameworks used in NYN:

Bootstrap, Sveltestrap, Svelte, Electron, TypeScript, CPython/libpython,
RabbitHoleSyndrome's Portable Windows Electron-Forge Maker, Electron Forge,
js-cookie, jq, Flask, MySQL Connector Python.

## Motivation

NYN is the Fall 2023 term project for the aforementioned authors in Swayam Pati's CPSC 362
at California State University, Fullerton. This does not dispel the copyrights
retained by the individual authors, who retain sole copyright and all rights
as expressed under the AGPLv3.

We chose to make a fitness tracking/workouts app to help promote health and fitness
on campus, as we found many of the existing solutions (like Sworkit) to
not meet the needs of the CSU Fullerton community. NYN is also one of the few
content-based solutions to be 100% free (as in freedom) software.

The name comes from our inability to find a name; NYN is short for "not yet named".
The acronym eventually stuck due to its palindromic nature.

We also used this opportunity to learn frameworks we previously had no experience
with, like libpython and Svelte. These ended up being critical to the project.
Svelte has saved signficant amounts of development time, and contributes heavily
to incredible site performance, even on low-performing machines. By writing our
mathematical code in C++, we were able to reduce total API latency across the
entire stack (including network latency!) to an average of 7ms, even for recommendation
requests; in fact, the average non-database-hitting request takes up 4ms, and
the average database-hitting request takes 5ms, meaning processing the entire workout
database to generate recommendations only takes ~2ms of additional processing time!
(Times were measured on a Ryzen 7 7700X, real deployments may be on a 3700X or less)

Optimization has been a critical part of the project. Our current infrastructure
uses AVX2 to optimize vector computations for recommendations; most of our mathematical
code gets executed as straight AVX2 instructions with no interruptions that could
cause speculative execution misses to occur. Given the size of our vectors, we also
have the ability to scale well to AVX-512 hardware.

## Help/Assistance

For assistance with NYN, contact Amy:

- Email: amy@amyip.net
- Matrix: https://matrix.to/#/@amyipdev1:matrix.org
- Fediverse: https://blahaj.zone/@amyipdev
- Instagram: https://instagram.com/amyipdev

You can also file an Issue.