# asr-benchmark


Download databases
------------------

* LapsBenchMark1.4: 
`wget http://www.laps.ufpa.br/falabrasil/files/LapsBM1.4.rar`

* Voxforge: 
`wget -r -nH -nd -np -R index.html* http://www.repository.voxforge1.org/downloads/pt/Trunk/Audio/Original/48kHz_16bit/`


After downloading you must downsample the databases to 16000 Hz and 8000 Hz. It can be done with any tool you want. A good one is [sox](http://sox.sourceforge.net/).


Dependencies
------------

python 3.5
```
conda create -n asr
source activate asr
pip install --upgrade watson-developer-cloud
pip install python-dotenv
```

Go to the scripts directory and create a .env file with the following variables with theirs values (you must get your keys values from your account at Bluemix/IBM and Bing/Microsoft):
BLUEMIX_USERNAME="XXXXXXXX"
BLUEMIX_PASSWORD="YYYYYY"
SUBSCRIPTION_KEY="MMMMMM"
INSTANCE_ID="ZZZZZZ"
REQUEST_ID="QQQQQQQ"

BLUEMIX_USERNAME and BLUEMIX_PASSWORD are keys necessary for running IBM benchmark. The other 3 keys are only necessary to run Microsoft benchmark.

Benchmark
---------

```
source activate asr

python scripts/ibmASR.py 16000 laps-16k.txt > results/ibm-laps-16k.tra
python scripts/ibmASR.py 8000  laps-8k.txt  > results/ibm-laps-8k.tra
python scripts/ibmASR.py 16000 voxforge-16k.txt > results/ibm-voxforge-16k.tra
python scripts/ibmASR.py 8000  voxforge-8k.txt  > results/ibm-voxforge-8k.tra

python scripts/microsoftASR.py 16000 laps-16k.txt > results/microsoft-laps-16k.tra
python scripts/microsoftASR.py 8000  laps-8k.txt  > results/microsoft-laps-8k.tra
python scripts/microsoftASR.py 16000 voxforge-16k.txt > results/microsoft-voxforge-16k.tra
python scripts/microsoftASR.py 8000  voxforge-8k.txt  > results/microsoft-voxforge-8k.tra
```

Results
-------
