#/usr/bin/env bash -e
#
# This script will downsample an audio file.
#
# Requires SOX
#	sudo apt install sox
#
# Usage: 
#	./downsample.sh [file] [(optional) desired sample_rate: 8000, 16000]

file=$1
filename="${file%.*}"
bit_rate=16
sample_rate=$2

# provide a default sampling rate is none is defined
if [ -z $sample_rate ]; then sample_rate="16000"; fi

# generate output file name
out_file="${filename}_${sample_rate}.wav"

echo "Resampling..."
sox ${file} --bits ${bit_rate} --rate ${sample_rate} --channels 1 ${out_file}

echo "${file} -> ${out_file}"
echo "Done!"