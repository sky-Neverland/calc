#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
fout=open('result.txt','w')
fout.write('1751514\n')

def calc():
	n=random.randint(3,5)
	num=[0]*5	#numbers used in equations
	op=['']*4	#oprators used in equations
	equ=''		#equation

	for i in range(n-1):								#randomize num & op
		num[i]=random.randint(1,100)
		op[i]=random.choice('+-*/')
		equ+=str(num[i])+op[i]							#set up equations
	num[n-1]=random.randint(1,100)
	equ+=str(num[n-1])		

	fout.write('%s%s%d%s'%(equ,'=',eval(equ),'\n'))		#use "eval()" to calculate equations

for i in range(5):
	calc()

fout.close()