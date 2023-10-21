#!/usr/bin/env bash

source ../venv/bin/activate
python3 api/create_account.py
python3 api/generate_token.py
python3 api/verify_token.py 