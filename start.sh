#!/bin/sh

cd servidor-1-flask
sudo docker-compose -f "docker-compose.yaml" up -d --build
docker ps
echo Ready!