#!/bin/bash

cat $1 | awk -F $"\t" '{ OFS = "\t" ; print $1, tolower($2); }'
