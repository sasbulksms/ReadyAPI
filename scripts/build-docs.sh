#!/usr/bin/env bash

set -e
set -x

# Check README.md is up to date
python ./scripts/docs.py verify-docs
python ./scripts/docs.py build-all
