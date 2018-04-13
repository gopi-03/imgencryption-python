#!/usr/bin/env bash
#cd $1
convert -size $1x$1 -background white -gravity Center -weight 700 -pointsize 20 caption:"$2" "$3"


