#!/bin/bash

IMAGE_NAME=challenge-landbot:dev


docker rmi $IMAGE_NAME
docker build -f Dockerfile.dev -t $IMAGE_NAME .

echo "Created docker image $IMAGE_NAME"
