# About

This script downloads videos from various pornographic websites, separates the audio files from the video. Then uses Google Speech API to find audio files with the phrase "god" in the them. It uses IBM Watson Speech-to-Text service to get transcripts of the audio along with the timing. This is used to clip the audio files at the points where the phrase occurs. 

# Folder structure and files

video - the videos downloaded from the sites
audio - the stripped mp3 of the videos
  id.mp3 - the mp3 file for file id.mp4 or id.webm
  id.google.txt - the google transcript of the mp3 is placed here
  id.watson.clip.1.mp3 - the clip produced by IBM Watson
  id.watson.clip.2.mp3
google - the mp3 converted to flac format for use in Google Speech API
watson - the mp3 converted to wav format for use in IBM Watson Speech-to-Text Service
watson-transcript - the transcript of the wav file

# Instructions

## Google Cloud Platform

Sign-up for [Google Cloud Platform](https://cloud.google.com/free/). Create a default project, choose Python as the language. Go through the tutorial and let it create the default project and will also create a bucket for the storage needed later. Create [security credentials](https://cloud.google.com/storage/docs/authentication#generating-a-private-key). Choose the json file format for the security credentials. In the [console](https://console.cloud.google.com/) select "Storage" and then view the buckets. The bucket name will appear as "project-id.appspot.com". This is the bucket-name used in conf.yaml and the path to security-credentials.json file is stored in keyfile in conf.yaml

## IBM Watson

Sign-up for [IBM Watson](https://www.ibm.com/watson/developercloud/speech-to-text.html), create a new Service, select "Watson/Speech to Text". View the service and click on "Service credentials", then "View credentials". The username and password found there are the ones to be used in conf.yaml

## Copy conf.yaml
Copy conf.yaml.example to conf.yaml and edit the values mentioned above.

## Install dependencies

    $ pip install -r requirements.txt

## Run the downloader

    $ python download.py

## Run the splitter

    $ bash process.sh

## Run the transcript process

    $ python main.py
