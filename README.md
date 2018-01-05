# Create your own Kaldi speech recognition system

Voco allows you to create a Kaldi speech recognition system based on your own voice that will allow you to program by predominantly using your voice. This is intended for programmers who have developed RSI or have other injuries or disabilities and need to continue their work but are unable to use a traditional keyboard and mouse setup for extended periods of time. This software was developed to be used prmarily with EMACS (Spacemacs with VIM emulation as the modal navigation menus are crucial to its use).

Example:
- alpha bravo charlie -> abc
- switch window -> alt + tab
- page down -> page down
- up three -> up up up
- jump 308 -> move cursor to line 308 in emacs
- jump india foxtrot -> move cursor to "if" using evil-avy-goto-char 

## What is Voco

Voco packages the following things together:
1. A data creation module that helps you create a training set
2. A Kaldi training script resuired to train a GMM model on the data you created
3. A decode module that records your voice when you speak, decodes it using Kaldi, parses it using Silvius (and some custom code) and then executes the commands on your computer

## Why use Voco

By training on data that is representive of the data the system will see during operation and by keeping the dictionary of possible words small this system is able to provide the following advantages:

1. **Low error rates:**
By keeping the dictionary small (I am using 86 possible commands) and by training on the microphone and noise profile that will be used during operation the system is able to achieve WER (word error rates) of ~0.5% and SER (sentence error rates) of ~1.35%. This is achieved with a low cost USB microphone (Platronics XXX) that has a unipressive XXX dB of signal sepperation. In my opinion these error rates are the mininum for a keyboard replacement system since anything higher results in frustration.

2. **Low latency and low recourse utilization:**
Since the model is small the system does not require much processing power to decode samples and samples are decoded *almost* in real time (<500ms). This system runs in the background on a Thinkpad T420 with 8GB Ram and and i5-2540M (Geekbench Multicore score of ~5000) while programming with no appreciable performance issues. In addition, since the model is small a "first draft" model can be trained on just 500 samples and re-trained on correctly decoded samples creaded during operation. 

3. **Easy to modify:**
The entire system is written in Python and 


## Based on Kaldi and Silvius
This work is based on Kaldi speech recognition system and the Silvius grammar parser. My thanks to Tavis Rudd and David Williams-King for discussing how they dealt with not being able to use a keyboard and sharing their solutions. I developed this system when I developed RSI and needed a low error, low resource, simple and easy to customize replacement for my keyboard.

Coding by Voice with Open Source Speech Recognition - https://www.youtube.com/watch?v=YRyYIIFKsdU
Using Python to Code by Voice - https://www.youtube.com/watch?v=8SkdfdXWYaI

Related links:
Kaldi: http://kaldi-asr.org/
Silvius: http://voxhub.io/silvius


## Procedure
* Create the training data
VoxForgeDict

* Train a GMM based Kaldi model


copy model

* Use the system

setup KALDI_ROOT in path file


* Improve results by adding previously decoded samples



Limitations:




Contact:


Prerequisites: