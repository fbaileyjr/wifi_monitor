#!/bin/bash



iwlist wlan0 scan | awk -F '[ :=]+' '/Cell/ {printf substr($0,30)" " } /(ESS|Freq)/{printf$3" " } /Qual/{print$3" " $6" " }' | sort -k1 -k5nr
