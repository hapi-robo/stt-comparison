#!/bin/bash

echo "Extracting all data files..."

cd voice-statistics.github.com/assets/data/

for filename in *.tar.gz
do
  tar xvzf $filename
done

echo "Done!"