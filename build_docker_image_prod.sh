#!/bin/bash

IMAGE_NAME=challenge-landbot:prod

docker rmi $IMAGE_NAME
docker build --no-cache -t $IMAGE_NAME .
echo "Created docker image $IMAGE_NAME"
