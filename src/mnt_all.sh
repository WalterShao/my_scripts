#!/usr/bin/env bash

BASEDIR=$(dirname "$0")

set -x
$BASEDIR/mnt_qnap.sh
$BASEDIR/mnt_mynb.sh

set +x
