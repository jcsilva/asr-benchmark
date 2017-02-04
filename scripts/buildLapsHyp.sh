#!/bin/bash

transc=$(cut -d$'\t' -f2 $1)
dirname=$(cut -d$'\t' -f1 $1 | rev | cut -d'/' -f2 - | rev | cut -d'-' -f2 - )
filename=$(cut -d$'\t' -f1 $1 | rev | cut -d'/' -f1 - | rev | cut -d'.' -f1 - | cut -d'_' -f2 -)

id=$(paste <(echo "$dirname") <(echo "$filename") --delimiters '-' )

# create hypotheses file according to kaldi's "text" format
# remove lines with no transcription
paste <(echo "$id") <(echo "$transc") | awk -F'\t' '$2!=""' -
