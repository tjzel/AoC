#!/bin/bash
tr -ds 'A-z,:=' ' ' | sed -E 's/^ //g'