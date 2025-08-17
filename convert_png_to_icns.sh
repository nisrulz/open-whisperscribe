#!/bin/bash
# Exit on any error and treat unset variables as an error
set -eu

sips -s format icns assets/logo.png --out assets/logo.icns
