#!/bin/sh

ROOT="$(dirname $0)/.."

# Build HTML
podman run \
    --rm \
    -v "${ROOT}:/docs:Z" \
    sphinxdoc/sphinx \
    /bin/bash _script/_build_html.sh

# Build PDF
podman run \
    --rm \
    -v "${ROOT}:/docs:Z" \
    sphinxdoc/sphinx-latexpdf \
    /bin/bash _script/_build_pdf.sh
