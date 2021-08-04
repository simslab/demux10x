#! /usr/bin/python
import argparse
import gzip
import io
import sys


def enumerate_bc(bc):
	bcs = []
	N = len(bc)
	for i in range(N):
		bc1=''
		bc2=''
		bc3=''
		bc4=''
		bc5=''
		for j in range(N):
			if i==j:
				bc1+='A'
				bc2+='G'
				bc3+='C'
				bc4+='T'
				bc5+='N'
			else:
				bc1+=bc[j]
				bc2+=bc[j]
				bc3+=bc[j]
				bc4+=bc[j]
				bc5+=bc[j]
		bcs.append(bc1)
		bcs.append(bc2)
		bcs.append(bc3)
		bcs.append(bc4)
		bcs.append(bc5)
	bcs = list(set(bcs))
	return bcs


def parse_user_input():
	parser = argparse.ArgumentParser()
	parser.add_argument('-ind','--index',required=True,help='Index sequence.')
	parser.add_argument('-s','--sample',required=True,help='Sample name.')
	parser.add_argument('-i','--index-fastq',required=True,help='Path to gzipped index fastq file.')
	return parser

parser = parse_user_input()
ui = parser.parse_args()

i1set = set(enumerate_bc(ui.index))
n=len(ui.index)

go=0
i=0
with io.BufferedReader(gzip.open(ui.index_fastq,'rb')) as f1:
	for line1,line3 in zip(f1,sys.stdin):
                if i == 0:
                        store=line3
                        i+=1
                elif i==1:
                        i1read = line1.decode()[0:n]
                        if i1read in i1set:
                                sys.stdout.write(store)
                                sys.stdout.write(line3)
                                go=1
                        i+=1
                elif i==2:
                        if go==1:
                                sys.stdout.write(line3) 
                        i+=1
                elif i==3:
                        if go==1:
                                sys.stdout.write(line3)
                        i=0
                        go=0

