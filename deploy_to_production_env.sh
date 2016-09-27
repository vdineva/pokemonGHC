#!/bin/bash
RELEASE_ARTIFACT=$1
tar -xvf $RELEASE_ARTIFACT.tar.gz

cp -r $RELEASE_ARTIFACT/pokestarter/static /pokestarter_prod/pokestarter
cp -r $RELEASE_ARTIFACT/pokestarter/templates /pokestarter_prod/pokestarter
cp $RELEASE_ARTIFACT/pokestarter/app.py /pokestarter_prod/pokestarter/app.py
cp $RELEASE_ARTIFACT/pokestarter/starters.py /pokestarter_prod/pokestarter/starters.py
