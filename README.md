# HiPAMA 

This repository is the implementation of the paper, [**Hierarchical Pronunciation Assessment with Multi-Aspect Attention**](https://ieeexplore.ieee.org/document/10095733/) (ICASSP 2023).

> Our code is based on the open source, [https://github.com/YuanGongND/gopt](https://github.com/YuanGongND/gopt) (Gong et al, 2022).

## Dataset

An open source dataset, SpeechOcean762 (licenced with CC BY 4.0) is used. You can download it from [https://www.openslr.org/101](https://www.openslr.org/101).

## Training and Evaluation (HiPAMA)
This bash script will run each model 5 times with ([0, 1, 2, 3, 4]).
- `cd src`
- `bash run_hipama.sh`

Note that every run does not produce the same results due to the random elements.

## Run baseline (GOPT)
This bash script will run each model 5 times with ([0, 1, 2, 3, 4]).
- `cd src`
- `bash my_run_gopt.sh`

## Analysis Running
The base code provided is not able to generate results successfully. You can run the code file `analysis.py` on the `exp/` folder which gives the mean, std for phonemes, utterances and words. 

## Citation

```
@INPROCEEDINGS{10095733,
  author={Do, Heejin and Kim, Yunsu and Lee, Gary Geunbae},
  booktitle={ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)}, 
  title={Hierarchical Pronunciation Assessment with Multi-Aspect Attention}, 
  year={2023},
  volume={},
  number={},
  pages={1-5},
  doi={10.1109/ICASSP49357.2023.10095733}}
```