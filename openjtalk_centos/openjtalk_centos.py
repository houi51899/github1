#coding: utf-8
import subprocess
from datetime import datetime
import time

def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/usr/local/share/open_jtalk_dic']              # the directory you put the dic in
    htsvoice=['-m','/usr/local/share/hts-voice/mei_normal.htsvoice'] # the directory you put the voice file in
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t.encode('utf-8'))
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)

def pre_alert():
    d = datetime.now()
    text = '今は%s月%s日、%s時%s分%s秒です' % (d.month, d.day, d.hour, d.minute, d.second)+'     何秒後、注意しますか。入力してください'
    jtalk(text)
  
    n=int(input("何秒後、注意しますか? 入力してください: "))
    text = 'わかりました。それでは%s秒後、また注意しますね' % (n)
    jtalk(text)
    return n

def say_datetime():
    d = datetime.now()
    text = '時間になります。今は%s月%s日、%s時%s分%s秒です。これからも頑張ってください' % (d.month, d.day, d.hour, d.minute, d.second)
    jtalk(text)

    
def countdown(n):
    while n>1:
        n=n-1
        print(n)
        time.sleep(1)

def alert():
    count_timer=pre_alert()
    countdown(count_timer)
    say_datetime()
        
        
if __name__ == '__main__':
    alert()
