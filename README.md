# asr-benchmark


Download databases
------------------

* LapsBenchMark1.4:
`wget http://www.laps.ufpa.br/falabrasil/files/LapsBM1.4.rar`

* Voxforge:
`wget -r -nH -nd -np -R index.html* http://www.repository.voxforge1.org/downloads/pt/Trunk/Audio/Original/48kHz_16bit/`


After downloading you must downsample the databases to 16000 Hz and 8000 Hz.
It can be done with any tool you want. A good one is [sox](http://sox.sourceforge.net/).


Dependencies
------------

You will need Python 3 to run the benchmark scripts. And, optionally, you may
use some scripts I wrote in Bash to process the transcriptions generated by the
benchmark scripts.

I use [Anaconda](https://www.continuum.io/downloads) to deal with Python
dependencies, which were watson-developer-cloud and python-dotenv.

For creating my environment, I did:

```
conda create -n asr python=3.5
source activate asr
pip install --upgrade watson-developer-cloud
pip install python-dotenv
```

In this benchmark, word error rate (WER) and sentence error rate (SER) will be
evaluated and you will need a tool to measure them.
The [NIST Speech Recognition Scoring Toolkit] (ftp://jaguar.ncsl.nist.gov/pub/sctk-2.4.10-20151007-1312Z.tar.bz2)
may be used for this purpose. Another equivalent tool is the
`compute-wer` from [kaldi toolkit](http://kaldi-asr.org/doc/tools.html). I used
this last one just because I had kaldi installed in my machine.

You will also need to create some credentials to access IBM and Microsoft speech API.
You must go to [IBM Bluemix](https://console.ng.bluemix.net/) and
[Microsoft Bing](https://www.microsoft.com/cognitive-services/en-us/speech-api)
to get your keys.

After grabbing your keys, create a .env file in the scripts directory
with the following variables and theirs values:
* BLUEMIX_USERNAME="XXXXXXXX"
* BLUEMIX_PASSWORD="YYYYYY"
* SUBSCRIPTION_KEY="MMMMMM"
* INSTANCE_ID="ZZZZZZ"
* REQUEST_ID="QQQQQQQ"

BLUEMIX_USERNAME and BLUEMIX_PASSWORD are keys necessary for running IBM
benchmark. The other 3 keys are only necessary to run Microsoft benchmark.

Benchmark
---------

```
source activate asr

python scripts/ibmASR.py 16000 data/laps-16k.txt > results/ibm-laps-16k.tra
python scripts/ibmASR.py 8000  data/laps-8k.txt  > results/ibm-laps-8k.tra
python scripts/ibmASR.py 16000 data/voxforge-16k.txt > results/ibm-voxforge-16k.tra
python scripts/ibmASR.py 8000  data/voxforge-8k.txt  > results/ibm-voxforge-8k.tra

python scripts/microsoftASR.py 16000 data/laps-16k.txt > results/microsoft-laps-16k.tra
python scripts/microsoftASR.py 8000  data/laps-8k.txt  > results/microsoft-laps-8k.tra
python scripts/microsoftASR.py 16000 data/voxforge-16k.txt > results/microsoft-voxforge-16k.tra
python scripts/microsoftASR.py 8000  data/voxforge-8k.txt  > results/microsoft-voxforge-8k.tra

./scripts/buildLapsHyp.sh results/ibm-laps-16k.tra > results/ibm-laps-16k.hyp
./scripts/buildLapsHyp.sh results/ibm-laps-8k.tra  > results/ibm-laps-8k.hyp
./scripts/buildVoxforgeHyp.sh results/ibm-voxforge-8k.tra  > hypotheses/ibm-voxforge-8k.hyp
./scripts/buildVoxforgeHyp.sh results/ibm-voxforge-16k.tra > hypotheses/ibm-voxforge-16k.hyp

./scripts/buildLapsHyp.sh results/microsoft-laps-16k.tra > results/microsoft-laps-16k.hyp
./scripts/buildLapsHyp.sh results/microsoft-laps-8k.tra  > results/microsoft-laps-8k.hyp
./scripts/buildVoxforgeHyp.sh results/microsoft-voxforge-8k.tra  > hypotheses/microsoft-voxforge-8k.hyp
./scripts/buildVoxforgeHyp.sh results/microsoft-voxforge-16k.tra > hypotheses/microsoft-voxforge-16k.hyp

compute-wer --mode=present ark:references/laps.ref ark:hypotheses/ibm-laps-16k.hyp
compute-wer --mode=present ark:references/laps.ref ark:hypotheses/ibm-laps-8k.hyp
compute-wer --mode=present ark:references/voxforge.ref ark:hypotheses/ibm-voxforge-16k.hyp
compute-wer --mode=present ark:references/voxforge.ref ark:hypotheses/ibm-voxforge-8k.hyp

compute-wer --mode=present ark:references/laps.ref ark:hypotheses/microsoft-laps-16k.hyp
compute-wer --mode=present ark:references/laps.ref ark:hypotheses/microsoft-laps-8k.hyp
compute-wer --mode=present ark:references/voxforge.ref ark:hypotheses/microsoft-voxforge-16k.hyp
compute-wer --mode=present ark:references/voxforge.ref ark:hypotheses/microsoft-voxforge-8k.hyp
```

Results
-------

Results shown in terms of WER (Word Error Rate) and SER (Sentence Error Rate).

| Database          | IBM                                                                                  | Microsoft                    |
| :---------------: |:-------------------------------------------------------------------------------------|:-----------------------------|
| Laps 16 kHz       | %WER 13.59 [ 982 / 7228, 110 ins, 217 del, 655 sub ]  <br> %SER 64.14 [ 449 / 700 ]  |                              |
| Laps 8 kHz        | %WER 13.89 [ 1004 / 7228, 106 ins, 242 del, 656 sub ] <br> %SER 64.57 [ 452 / 700 ]  |                              |
| Voxforge 16 kHz   | %WER 31.23 [ 1067 / 3417, 134 ins, 313 del, 620 sub ] <br> %SER 54.74 [ 375 / 685 ]  | %WER 18.28 [ 616 / 3370, 46 ins, 186 del, 384 sub ] <br>  %SER 39.73 [ 269 / 677 ] |
| Voxforge 8 kHz    | %WER 28.62 [ 995 / 3477, 115 ins, 284 del, 596 sub ] <br>  %SER 53.58 [ 374 / 698 ]                                 |
