#!/bin/bash

docker build --network=host -t selenium-docker:v1 .

docker run -d  --privileged -v "$PWD":/app \
		--log-opt max-size=3m --log-opt max-file=3 \
        --name selenium-docker selenium-docker:v1
