#!/bin/sh

BASEDIR=$(dirname "$0")
docker build -t webapp_two:latest -f "$BASEDIR/Dockerfile" $BASEDIR
