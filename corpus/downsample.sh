#/usr/bin/env bash -e
#
# This script will convert all audio files to 16-bit, 16 kHz sampling rate .wav files.
#
# Requires SOX
#	sudo apt install sox
#
# Usage: 
#	./downsample2.sh [dir-in] [dir-out]

folder1=$1
folder2=$2

echo "Resampling..."

for filename in ${folder1}*.wav
do
	base=${filename##*/}
	pref=${base%.*}

	sox ${filename} --bits 16 --rate 16000 ${folder2}${pref}.wav
	echo "${filename} -> ${folder2}${pref}.wav" 
done

echo "Done!"
