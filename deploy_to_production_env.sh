#!/bin/bash
RELEASE_ARTIFACT=$1
rm -rf $RELEASE_ARTIFACT
mkdir $RELEASE_ARTIFACT
tar -xvf $RELEASE_ARTIFACT.tar.gz -C $RELEASE_ARTIFACT --strip-components 1

cp -r $RELEASE_ARTIFACT/pokestarter/static /pokestarter_prod/pokestarter
cp -r $RELEASE_ARTIFACT/pokestarter/templates /pokestarter_prod/pokestarter
cp $RELEASE_ARTIFACT/pokestarter/app.py /pokestarter_prod/pokestarter/app.py
cp $RELEASE_ARTIFACT/pokestarter/starters.py /pokestarter_prod/pokestarter/starters.py
