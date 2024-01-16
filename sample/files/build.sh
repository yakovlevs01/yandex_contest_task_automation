#!/bin/bash

OUT=participantSolution.py
TMP=tempNameForParticipantSolution.py

cat $filename > $TMP || exit 1
rm $filename
cat $TMP > $OUT || exit 1