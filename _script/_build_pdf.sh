#!/bin/sh

ROOT="$(dirname $0)/.."

pushd "${ROOT}"

pip install -r requirements.txt
make latexpdf

popd
