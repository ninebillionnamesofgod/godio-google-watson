#!/usr/bin/env python
#-*- coding: utf-8 -*-

from oauth2client.service_account import ServiceAccountCredentials
from godio.transcribe_async import transcribe_gcs
from godio.sttClient import run_transcribe
import apiclient.discovery
from apiclient.http import MediaIoBaseUpload
import httplib2
import sys
import os
import yaml

with open("conf.yaml") as f:
    conf = yaml.load(f)

def upload_gcs(filename):
    scopes = ['https://www.googleapis.com/auth/devstorage.full_control']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(conf['keyfile'], scopes=scopes)
    storage = apiclient.discovery.build('storage', 'v1', http=credentials.authorize(httplib2.Http()))
    with open(filename) as f:
        media = MediaIoBaseUpload(f, mimetype="audio/flac")
        req = storage.objects().insert(bucket=conf['bucket'], name=filename.split("/")[1], media_body=media)
        resp = req.execute()

if __name__ == '__main__':
    for p, n, filenames in os.walk("google"):
        for filename in filenames:
            if not os.path.exists("audio/{}.google.txt".format(filename.split(".")[0])):
                upload_gcs("google/{}".format(filename))
                try:
                    alternatives = transcribe_gcs("gs://{}/{}".format(conf['bucket'], filename))
                    with open("audio/{}.google.txt".format(filename.split(".")[0]), "w") as f:
                        for alternative in alternatives:
                            f.write(alternative.transcript)
                            f.write(' confidence:{}\n'.format(alternative.confidence))
                except ValueError:
                    pass

    for p, n, filenames in os.walk("watson"):
        for filename in filenames:
            if not os.path.exists("watson-transcripts/{}.json.txt".format(filename)):
                run_transcribe("watson-transcripts", filename, conf['username'], conf['password'])
