# Speech-to-Text Service Comparison
The scripts in this repository are used for testing online speech recognition services for the Japanese language.

Each service comes with API credentials and some services require installation of SDK or library. Refer to the individual services documentation for this.

Note that there exists a Python package to do some of this https://pypi.org/project/SpeechRecognition/, but I've decided to go through the process of figuring it out myself to better understand the inner-workings of each service.


## Install
```
$ git clone https://github.com/ray-hrst/stt.git
$ cd stt/
$ git submodule init
$ git submodule update
```

## Setup
Each script uses it's own [Python virtual environment](https://virtualenv.pypa.io/en/stable/). Python package requirements for each enviroment can be found in the `requirements` folder. Auto-generate the virtual environment with:
```
$ ./setup.sh XXX
```

where `XXX` can be:
* `google`
* `ibm`
* `wit`
* `fuetrek`

For example:
```
$ ./setup.sh google
```


## Usage
First start the appropriate Python virtual environment:
```
$ . venv/XXX/bin/activate
```

Then run the script. Note that all scripts are located in the `scripts` directory.
```
$ python stt_XXX.py /path/to/audio/sample.wav
```

where `XXX` can be:
* `google`
* `ibm`
* `wit`
* `fuetrek`


## Resources
The `resources` folder contains voice samples and transcripts from various online sources. They can be used as input for each of the scripts.


## Online Services
The following services were tested.

### [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/)
**Notes**
* Easy to setup only after you figure out how to turn on the service; Google's Cloud management system (which is complicated).
* Provides the most fastest and reliable service

### [IBM Watson Speeth to Text](https://www.ibm.com/watson/services/speech-to-text/)
**Notes**
* Straightforward to use with good documentation and out of the box working examples

### [wit.ai](https://wit.ai/)
**Notes**
* Free: https://wit.ai/faq
* Straightforward to use with good documentation and out of the box working examples
* Unreliable service

### [Fuetrek](https://www.fuetrek.co.jp/)
**Notes**
* TBD

### [Nuance Mix](https://developer.nuance.com/mix/)
**Notes**
* Documentation is outdated
* I can't get it to work; examples don't work out of the box; difficult to setup
* Nobody from Nuance seems to be supporting the forum
* Code only works with Python 2


## Voice-Sample Resources
* Japanese Speech Corpus of Saruwatari-lab., University of Tokyo (JSUT). https://sites.google.com/site/shinnosuketakamichi/publication/jsut
* Voice Statistics. http://voice-statistics.github.io/
	* nico-opendata. https://nico-opendata.jp/ja/casestudy/2stack_voice_conversion/report.html
* ASJ Japanese Newspaper Article Sentences Read Speech Corpus (JNAS). http://research.nii.ac.jp/src/en/JNAS.html
	* BM001A05.wav "救急車が　十分に　動けず　救助作業が　遅れている"
	* NM001001.wav "まだ 正式 に 決まっ た わけ で は ない ので"
* Kota Takahashi Laboratory. http://www.it.ice.uec.ac.jp/SRV-DB/


## TODO
* Use metadata
* Compare against text