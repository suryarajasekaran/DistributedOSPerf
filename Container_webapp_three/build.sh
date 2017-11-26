#!/bin/sh

BASEDIR=$(dirname "$0")
docker build -t webapp_three:latest -f "$BASEDIR/Dockerfile" $BASEDIR
