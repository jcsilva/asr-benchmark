#!/bin/bash

transc=$(cut -d$'\t' -f2 $1)
dirname=$(cut -d$'\t' -f1 $1 | rev | cut -d'/' -f3 - | rev )
filename=$(cut -d$'\t' -f1 $1 | rev | cut -d'/' -f1 - | rev | cut -d'.' -f1 -)


transc=${transc,,} # converts to lowercase. Depends on bash 4.3 or greater
transc=$(echo "$transc" | tr -d '[:punct:]') # delete punctuations


id=$(paste <(echo "$dirname") <(echo "$filename") --delimiters '-' )

# create hypotheses file according to kaldi's "text" format
# remove lines with no transcription
paste <(echo "$id") <(echo "$transc") | awk -F'\t' '$2!=""' -
