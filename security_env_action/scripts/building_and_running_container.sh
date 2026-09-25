#!/bin/bash

DOCKERFILE="$1"
NAME_FOR_IMAGE="$2"
PORT_FORWARDING="$3"


docker build -t "$NAME_FOR_IMAGE" "$DOCKERFILE"

docker run -d -p "$PORT_FORWARDING"

