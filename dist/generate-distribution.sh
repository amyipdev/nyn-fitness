set -e
cd "$(dirname "$0")"

BASEDIR=$(pwd)
cd ../electron
rm -rf node_modules
npm i
cd node_modules/@rabbitholesyndrome/electron-forge-maker-portable
git init
git apply $BASEDIR/0.patch
cd ../../..
# squirrel has been removed due to mono errors
npm run make -- --targets @rabbitholesyndrome/electron-forge-maker-portable --platform win32
npm run make -- --targets @electron-forge/maker-zip --platform darwin
npm run make -- --targets @electron-forge/maker-deb,@electron-forge/maker-rpm --platform linux