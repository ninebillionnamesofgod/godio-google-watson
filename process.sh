#!/bin/bash

for f in ./video/*.mp4; do
    filename=${f##*/}
    name=${filename%.*}
    if [ ! -f ./audio/$name.mp3 ]; then
        ffmpeg -i $f ./audio/$name.mp3
    fi
    if [ ! -f ./watson/$name.wav ]; then
        #for IBM Watson
        ffmpeg -i $f ./watson/$name.wav
    fi
    if [ ! -f ./google/$name.flac ]; then
        #for Google Speech API
        ffmpeg -i $f -ac 1 -ar 16k ./google/$name.flac
    fi
done
