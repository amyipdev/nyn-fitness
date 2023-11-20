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

#### Adding workouts

Your NYN instance will not initially have content. You can add workouts using:

```sh
python3 setup/input_workouts.py
```

#### SSL/TLS

NYN currently does not ship with SSL. However, you can use a reverse proxy
(we recommend NGINX) to enable SSL support with free certificates from Let's Encrypt.