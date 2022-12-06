#!/bin/bash
#making input easy to parse
tr -d '[]' | tr '  ' ' ' |
sed -E 's/ *[[:alpha:]]+ *([[:digit:]]+)/\1 /g' |
sed -E 's/    / -/g' |
sed -E 's/-([[:alpha:]])/- \1/g' |
sed -E 's/^ *//g' |
sed -E 's/ *([[:digit:]]) +/\1 /g' |
sed -E 's/ +$//g'
