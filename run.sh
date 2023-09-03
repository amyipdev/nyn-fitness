set -e
cd "$(dirname "$0")"
if [ ! -f "nyn-conf.json" ]; then echo "No config file"; exit 1; fi
make setup
make
source venv/bin/activate
gunicorn -w 4 -b "[::]:$(jq -j .port nyn-conf.json)" app:app