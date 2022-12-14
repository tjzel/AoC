#!/bin/bash
sed -E 's/\]/,\],/g' | 
sed -E 's/\[/,\[,/g' | 
tr -s ',' |
sed -E 's/^,//g' |
sed -E 's/,$//g' |
tr ',' ' '