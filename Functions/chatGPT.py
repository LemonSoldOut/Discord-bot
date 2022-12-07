#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Date: 2022-12-07 15:00:27
@Author: 今日摸鱼 
@Email: lemonsoldout@163.com
@Github: https://www.github.com/lemonsoldout
@Package: Discord\Discord-Bot\Functions\chatGPT.py
@Version: v1.0
@Description: ChatGPT API 构建与封装
'''

# import modules
import requests
import datetime
import yaml
import json
import os

def getToken():
    abs_path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    config_file_path = abs_path + "\\config\\config.yaml"
    with open(config_file_path) as file:
        config = yaml.safe_load(file)

    sk_token = config['config']['chatGPT']
    return sk_token



def AICodeCompletion(msg = "编写一个 Java 语言的冒泡排序"):
    token = getToken()
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
    }
    
    url = "https://api.openai.com/v1/completions"
    
    model = "code-davinci-002"
    
    
    prompt = "/*" + msg + "*/"
    
    temperature = 0
    max_tokens = 256
    top_p = 1
    frequency_penalty = 0
    presence_penalty = 0
    
    data = json.dumps({"model": model, "prompt": prompt, "temperature": temperature, "max_tokens": max_tokens, "top_p": top_p, "frequency_penalty": frequency_penalty, "presence_penalty": presence_penalty})
    
    res = requests.post(url=url,headers=headers, data=data).json()
    
    return res["choices"][0]["text"]

def QAService(msg = "who ami i"):
    token = getToken()
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
    }
    
    url = "https://api.openai.com/v1/completions"
    
    model = "text-davinci-003"
    
    
    prompt = msg
    
    temperature = 0
    max_tokens = 100
    top_p = 1
    frequency_penalty = 0.0
    presence_penalty = 0.0
    timeout = 20
    data = json.dumps({"model": model, "prompt": prompt, "temperature": temperature, "max_tokens": max_tokens, "top_p": top_p, "frequency_penalty": frequency_penalty, "presence_penalty": presence_penalty})
    
    
    try:
        res = requests.post(url=url,headers=headers, data=data, timeout=timeout).json()
    
    except:
        return {"ERROR":"Timeout"}
    
    return res["choices"][0]["text"]



#print(QAService("原神是哪家游戏公司开发的"))