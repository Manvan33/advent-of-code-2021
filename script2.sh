#!/bin/bash
echo `fgrep forward input2 | cut -c 9 | paste -sd+ | bc` "*" `sed -ne "s/up /-/p" -e "s/down /+/p" input2 | paste -sd "" | cut -c 2- | bc` | bc
