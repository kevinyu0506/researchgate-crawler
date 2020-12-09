#!/bin/bash

echo "Target url: $1"

docker build -t researchgate-crawler .

docker run --rm -v $(pwd)/output:/app/output researchgate-crawler url=$1
