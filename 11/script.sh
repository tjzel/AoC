#!/bin/bash
tr -d 'A-z:=,' | tr -s ' ' | sed -E 's/^ +//' | sed -E 's/ +$//'