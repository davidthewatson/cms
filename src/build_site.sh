#!/usr/bin/env bash
. ../.env
rm -rf $DOCS/*
cp -rf $STATIC/* $DOCS/.
    
python ./md2html.py

