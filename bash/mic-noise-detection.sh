#!/usr/bin/env bash

filename=$1
duration=$2


if [ "$(uname)" == "Darwin" ]; then

    # Do something under Mac OS X platform
    sox -t coreaudio "Logitech USB He" $filename trim 0 $duration

    # Analyser
    sox $filename -n stat 2>&1 | sed -n 's#^Maximum amplitude:[^0-9]*\([0-9.]*\)$#\1#p'

elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Do something under GNU/Linux platform

    # USB C-media
    arecord --quiet --format S16_LE -D plughw:1,0 --rate 44100 -d $duration $filename

    # Analyser
    sox $filename -n stat 2>&1 | sed -n 's#^Maximum amplitude:[^0-9]*\([0-9.]*\)$#\1#p'

# Uncomment and handle for windows systems
#elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
#    # Do something under 32 bits Windows NT platform
#elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
#    # Do something under 64 bits Windows NT platform
fi