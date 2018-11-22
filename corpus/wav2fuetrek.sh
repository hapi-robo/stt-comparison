#/usr/bin/env bash -e
#
# This script will convert all audio files in a folder to Fuetrek's format.
#
# Format specifications:
# - 16 kHz sampling rate
# - 16-bit resolution
# - Big-endian PCM file (WAV without header information)
#
# Requires FFMPEG
#	sudo apt install ffmpeg
#
# Usage: 
#	./wav2fuetrek.sh [dir]

folder=$1

echo "Converting..."

for filename in ${folder}/*.wav
do
	sox ${filename} --bits 16 --rate 16000 --encoding signed-integer --endian big ${filename%.*}.raw
	echo "${filename} -> ${filename%.*}.raw" 
done

echo "Done!"
