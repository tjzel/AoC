#!/bin/bash
tr -d 'Valves' | sed -E 's/[[:alpha:]]*([[:digit:]]+)/\1/' | sed -E 's/^ +//' | tr -d ';=,a-z' | tr -s ' '