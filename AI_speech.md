==============================================================================================
# Speaking Chat Bot using TensorFlow on CentOS

In this trial, I apply the Japanese speech synthesis engine(OpenJTalk) in a chat bot whose replies generated using framework TensorFlow. In this way, the bot could response to the complain by voice.

Since framework TensorFlow has been used in the bot's scripts generation and the program is going to be put on a server(CentOS), I need build a proper development environment. 
Here are the tools I need at least:
- CentOS7
------------------------------
- Python3.6
- TensorFlow
- other modules for Python
------------------------------
- OpenJTalk(HTS engine, voice model, voice source, dictionary files)

I divided these in to three parts(OS,Python,synthesis engine). Thus the manual consists of three parts.  I'd like to share the experience of installing the corresponding tools.

## Part 1 CentOS installation

I installed the CentOS system on virtual machine(VirtualBox)
- Download the iso file of CentOS
http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-DVD-1804.iso
- Setup for the system(memory, hard disc)
- Read the iso file by VirtualBox
- Select the OS type and the software going to be installed in advance
- Install the system
Be aware that minimal system will be installed by default in OS type selection session which means you can only use the CUI (which is not recommended for ordinary user). To avoid this, you shall select the OS type in the selecting session. (I chose the one recommended as development environment)
--------------------------------------------------------------------------------------------
## Part 2
After the OS installation, let's install the development tools. 
(In the first time I installing the TensorFlow, I tried directly installing it in anaconda environment which I have installed in advance for previous work. This method worked well on Window 10. However, things are not going in the same way on CentOS7. Version conflictions and files missing arise one after another. So I hope that after reading this note, you could have a better installing experience than me.)

- Build virtual environment for Python
To avoid conflictions between different versions of Python, we need some tools to build a virtual environment for them. Here we use Pyenv. We can download it in https://github.com/pyenv/pyenv/releases. At present, the latest version is v1.2.4. Please download the "Source code(zip)".And then install it. The command you might use is:
#"cd" to get into download folder
$unzip pyenv-1.2.4.zip

$mv pyenv-1.2.4 ~/.pyenv

#After this we need setup the path:
$echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

$echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

$echo 'eval "$(pyenv init -)"' >> ~/.bashrc

$source ~/.bashrc

- Install and setup Anaconda 4.3.0(here we only utilize the "conda" command not the python neither spyder...)
$pyenv install anaconda3-4.3.0

$pyenv rehash

$pyenv global anaconda3-4.3.0

$echo 'export PATH="$PYENV_ROOT/versions/anaconda3-4.3.0/bin/:$PATH"' >> ~/.bashrc

$source ~/.bashrc
#update anaconda and confirm current python version

$conda update conda

$python -V

- Install Python ( Yes, it's necessary)
$conda create -n tensorflow python=3.6.0

$source activate tensorflow

$python -V

- Install TensorFlow
$export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp36-cp36m-linux_x86_64.whl

$pip install --ignore-installed --upgrade $TF_BINARY_URL
#now the installation of tensorflow and corresponding python has been down.

-Check whether it works
$source activate tensorflow(go into the virtual tensorflow environment)

$python

$import tensorflow as tf

$hello = tf.constant('Hello, TensorFlow!')

$sess = tf.Session()

$print(sess.run(hello))

#If you can see the text 'Hello, TensorFlow!', it means you complete the installation successfully. Then press Ctrl+D to exit python. And finally exit virtual tensorflow environment by:
$source deactivate

- Beware that to run a source coding using tensorflow module, you need:
$source activate tensorflow #go into the virtual environment

$python XXXX.py #run your code file here

- (option)Also beware that you are not in the environment of anaconda&spyder. Many libraries are not installed in this environment. You need add them manually in the way like this:
$source activate tensorflow

$conda install -c anaconda numpy=1.12.1

$conda install -c menpo opencv3=3.1.0

$conda install -c anaconda pillow=4.0.0

$conda install -c anaconda pandas #not sure

--------------------------------------------------------------------------------------------
## Part 3
Install OpenJalk
- Install Some necessary tools

$yum install alsa-utils unzip wget gcc gcc-c++

- Download and install hts_engine, OpenJTalk, voice model, dictionary.

$mkdir ~/download/

$mkdir ~/src/

$cd ~/download

$wget https://jaist.dl.sourceforge.net/project/hts-engine/hts_engine%20API/hts_engine_API-1.10/hts_engine_API-1.10.tar.gz

$wget https://jaist.dl.sourceforge.net/project/open-jtalk/Open%20JTalk/open_jtalk-1.10/open_jtalk-1.10.tar.gz

$wget https://jaist.dl.sourceforge.net/project/open-jtalk/HTS%20voice/hts_voice_nitech_jp_atr503_m001-1.05/hts_voice_nitech_jp_atr503_m001-1.05.tar.gz

$wget http://downloads.sourceforge.net/open-jtalk/open_jtalk_dic_utf_8-1.10.tar.gz

$cd ~/src/

$tar xvzf ~/download/hts_engine_API-1.10.tar.gz

$cd hts_engine_API-1.10/

$./configure

$make

$make install

$tar xzvf ~/download/open_jtalk-1.10.tar.gz

$cd open_jtalk-1.10/

$./configure --with-charset=UTF-8

$make

$make install

$tar xzfv ~/download/hts_voice_nitech_jp_atr503_m001-1.05.tar.gz

$mv hts_voice_nitech_jp_atr503_m001-1.05 /usr/local/share/hts_voice

$tar xzfv ~/download/open_jtalk_dic_utf_8-1.10.tar.gz

$mv open_jtalk_dic_utf_8-1.10 /usr/local/share/open_jtalk_dic

#Now the setup for all of three parts has be done. 




=======================================================================================

## Acknowledgements


## References
- [Python+TensorFlow on CentOS](https://qiita.com/harrynezumi/items/8e373a0563b92f3fc033)

- [OpengJtalk on CentOS](https://umiushizn.blogspot.com/2017/10/openjtalklinuxcentos7.html)