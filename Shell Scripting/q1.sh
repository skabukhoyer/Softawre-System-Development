#!/bin/bash

du -sh */ | sort -hr | awk '{print $2"\t"$1"B"}' | column -t | sed 's/^\///;s/\// /g'



