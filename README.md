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

Results shown in terms of WER (Word Error Rate) and SER (Sentence Error Rate).

| Database          | IBM                                                        | Microsoft                                              |
| :---------------: |:-----------------------------------------------------------|:-------------------------------------------------------|
| Laps 16 kHz       | %WER 13.59 [ 982 / 7228, 110 ins, 217 del, 655 sub ] <br>  |                                                        |
|                   | %SER 64.14 [ 449 / 700 ]                                   |                                                        |
| Laps 8 kHz        | %WER 13.89 [ 1004 / 7228, 106 ins, 242 del, 656 sub ] <br> |                                                        |
|                   | %SER 64.57 [ 452 / 700 ]                                   |                                                        |
| Voxforge 16 kHz   | %WER 31.23 [ 1067 / 3417, 134 ins, 313 del, 620 sub ] <br> | %WER 18.28 [ 616 / 3370, 46 ins, 186 del, 384 sub ]  \ |
|                   | %SER 54.74 [ 375 / 685 ]                                   | %SER 39.73 [ 269 / 677 ]                               |
| Voxforge 8 kHz    | %WER 28.62 [ 995 / 3477, 115 ins, 284 del, 596 sub ] <br>  |                                                        |
|                   | %SER 53.58 [ 374 / 698 ]                                   |                                                        |
