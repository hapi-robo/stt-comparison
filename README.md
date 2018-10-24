# Speech-to-Text Service Comparison
The scripts in this repository are used for testing speech recognition services for the Japanese language.

Note that there exists a Python package to do some of this https://pypi.org/project/SpeechRecognition/, but I've decided to go through the process of figuring it out myself to better understand the inner-workings of each service.

## Online Services
Each script uses it's own [Python virtual environment](https://virtualenv.pypa.io/en/stable/). Python package requirements for each enviroment can be found in the `requirements_*.txt` files.

### Google Cloud Speech-to-Text
https://cloud.google.com/speech-to-text/
* Easy to setup only after you figure out how to turn on the service; Google's Cloud management system (which is complicated).

### IBM Watson Speeth to Text
https://www.ibm.com/watson/services/speech-to-text/
* Straightforward to use with good documentation and out of the box working examples

### wit.ai
https://wit.ai/
* Free: https://wit.ai/faq
* Straightforward to use with good documentation and out of the box working examples

### Nuance Mix
https://developer.nuance.com/mix/
* I can't get it to work
* Examples don't work out of the box; difficult to setup
* Documentation is outdated
* Nobody from Nuance seems to be supporting the forum
* Code only works with Python 2

## Resources
* http://research.nii.ac.jp/src/en/JNAS.html
	* BM001A05.wav "救急車が　十分に　動けず　救助作業が　遅れている"
	* NM001001.wav "まだ 正式 に 決まっ た わけ で は ない ので"


## TODO
* Use metadata
* Compare against text
