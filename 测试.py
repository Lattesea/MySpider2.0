#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-12 下午2:17 
# @Author : Lattesea 
# @File : 测试.py


# from sys import argv
import sys

script = sys.argv[0]
user_name = sys.argv[1]
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
