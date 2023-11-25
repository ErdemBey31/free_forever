from threading import Thread
import os

def run_jupyter():
  os.system("pip install jupyter && jupyter notebook --ip=0.0.0.0 --port=3000 --allow-root g")

def run_ssh():
  os.system("ssh -R akls.serveo.net:80:localhost:3000 serveo.net")

if True:
  Thread(target=run_jupyter).start();
  Thread(target=run_ssh).start();
