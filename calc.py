#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
fout=open('result.txt','w')
fout.write('1751514\n')
def calc():
	n=random.randint(3,5)
	a=[0]*5
	b=['']*4
	s=''
	for i in range(n-1):
		a[i]=random.randint(1,100)
		b[i]=random.choice('+-*/')
		s+=str(a[i])+b[i]
	a[n-1]=random.randint(1,100)
	s+=str(a[n-1])
	fout.write('%s%s%d%s'%(s,'=',eval(s),'\n'))

for i in range(5):
	calc()

fout.close()