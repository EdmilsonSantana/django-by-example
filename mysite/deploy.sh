#!/bin/bash

echo "Cleaning..."

if [[ $(docker ps -a | grep blog ) ]]; then
	echo "Removing "
	docker stop blog && docker rm blog
fi

if [[ $(docker ps -a | grep proxy ) ]]; then
	echo "Removing "
	docker stop proxy && docker rm proxy
fi

echo "Building..."

docker build -t blog . 

echo "Starting"

docker run -d --restart=always \
 	-v $(pwd)/app:/app \
    --name=blog blog 

docker run -d --restart=always \
	-p 8080:80 \
	--link blog:blog \
	-e NGINX_HOST=192.168.99.100 \
	-e NGINX_PROXY=http://blog:8081 \
	--name=proxy edmilsonsantana/proxy:1.0

echo "Started"
