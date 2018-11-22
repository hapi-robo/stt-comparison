#/usr/bin/env bash -e
#
# This script will convert all audio files in a folder to Fuetrek's format.
#
# Format specifications:
# - 16 kHz sampling rate
# - 16-bit resolution
# - Big-endian PCM file (WAV without header information)
#
# Requires SOX
#	sudo apt install sox
#
# Usage: 
#	./wav2fuetrek.sh [dir-in] [dir-out]

folder=$1
folder2=$2

echo "Converting..."

for filename in ${folder}*.wav
do
	base=${filename##*/}
	pref=${base%.*}

	sox ${filename} --bits 16 --rate 16000 --encoding signed-integer --endian big ${folder2}${pref}.raw
	echo "${filename} -> ${folder2}${pref}.raw" 
done

echo "Done!"
