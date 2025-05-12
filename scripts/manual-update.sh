#!/bin/bash

git pull


python ./scripts/build-ad.py
python ./scripts/build-telegram.py
python ./scripts/build-direct.py
python ./scripts/build-proxy.py
python ./scripts/build-netease.py
python ./scripts/build-node.py
python ./scripts/build-sgmodule.py
python ./scripts/build-adlite.py
python ./scripts/build-adlite-clash.py
python ./scripts/gen-final.py

git add .
git commit -m "manual update" -a
git push
