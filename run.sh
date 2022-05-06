#!/bin/bash

if [ -z "$1" ]; then
  echo "$ ./run.sh <cmd>"
  exit 1
fi

docker run --gpus all -it --rm -v $PWD/src:/w -v $PWD/data:/w/data -w /w tensorflow/tensorflow:2.9.0rc2-gpu-jupyter $1