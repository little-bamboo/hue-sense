# README #

This covers the implementation of the HueSLIS python package and overall operation.

### What is this repository for? ###

* Installing the Package
* Version 0.0.1a
* Required Dependencies

### How do I get set up? ###

* Git Pull git@bitbucket.org:briansc2008/hue-sense.git 
* Ensure you have developer access to both AWS and Google Cloud security keys
* Install both Google Cloud Speech and AWS Config
* pip install -r requirements.txt
* Ensure PyAudio is installed (pip install pyaudio)
* USB Mic
* Raspberry Pi 3b (with compatible Debian wheezy/jesse OS)
* Mac Support

### AWS Config

* Run aws config and save your credentials to the device
* If you don't have aws cli installed, run the below commands

```
    $ pip install awscli --upgrade --user
 ```

https://docs.aws.amazon.com/cli/latest/userguide/installing.html

### Using Google Speech API

Follow the Google Speech API Quickstart - https://cloud.google.com/speech/docs/quickstart

Create 'config' directory in the root and save the generated key file as 'HuePi.json'

### PyAudio Installation Support

If you have problems installing PyAudio

Option 1: Install from source

``` 
$ sudo apt-get install git
$ git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
$ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
$ sudo apt-get python-dev
$ sudo python pyaudio/setup.py install

```

Option 2 from pip:

```
$ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
$ sudo apt-get python-dev
$ pip install pyaudio 
```

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Contact: brian.schaper@little-bamboo.com