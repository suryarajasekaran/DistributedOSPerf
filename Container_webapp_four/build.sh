#!/bin/sh

BASEDIR=$(dirname "$0")
docker build -t webapp_four:latest -f "$BASEDIR/Dockerfile" $BASEDIR
