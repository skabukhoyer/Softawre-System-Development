#!/bin/bash

grep -w -i "\w*ing" $1 | awk '{print tolower($0)}' | tr ' ' '\n' > $2
