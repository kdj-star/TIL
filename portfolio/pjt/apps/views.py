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


def index(request):
    

    return render(request,'apps/index.html')

def lotto(request):
    

    return render(request,'apps/lotto.html')

def practice(request):
    

    return render(request,'apps/practice.html')

def email_authentication(request):
    

    return render(request,'apps/email_authentication.html')

