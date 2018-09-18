#!/bin/bash

CLIENT=0

POSITIONAL=()
while [[ $# -gt 0 ]]
do

  key="$1"

  case $key in
    -m|--mode)
      MODE="$2"
      shift
      shift
      ;;
    -l|--label)
      LABEL="$2"
      shift
      shift
      ;;
    -a|--address)
      ADDRESS="$2"
      shift
      shift
      ;;
    -d|--debug)
      DEBUG="$2"
      shift
      shift
      ;;
    *)
      POSITIONAL+=("$1")
      shift
      ;;
  esac
done

set -- "${POSITIONAL[@]}"

source setup_env.sh

if [[ "${MODE}" = "server" ]]; then
  DARKNET_DIR="darknet/"
  if [[ ! -d "$DARKNET_DIR" ]]; then
    echo "No Darknet installation found."
    echo "Aborting..."
    exit 1
  fi
  INBOX_DIR="server/inbox/"
  if [[ ! -d "$INBOX_DIR" ]]; then
    mkdir -p "$INBOX_DIR"
  fi
  python3 main.py -l $LABEL -d $DEBUG
else
  CLIENT=1
fi

if [[ "${CLIENT}" = 1 ]]; then
  CAPTURE_DIR="client/capture/"
  if [[ ! -d "$CAPTURE_DIR" ]]; then
    mkdir -p "$CAPTURE_DIR"
  fi
  python3 main_client.py -a $ADDRESS
fi
