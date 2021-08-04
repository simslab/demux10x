#! /usr/bin/python
import os 
import argparse

def parse_user_input():
    parser=argparse.ArgumentParser()
    parser.add_argument('-m','--mode',required=True,choices=['single','dual'],help='Indicate single- or dual-index demultiplexing.')
    parser.add_argument('-s','--sample-table',required=True,help='Path to 2- or 3-column tab-delimited text file with sample name, index sequence 1, and optionally, index sequence 2.')
    parser.add_argument('-i1','--index1-fastq',required=True,help='Path to index read 1 (I1) fastq file.')
    parser.add_argument('-i2','--index2-fastq',required=False,help='Path to index read 2 (I2) fastq file. This is required only for dual index demultiplexing.')
    parser.add_argument('-t','--target-fastq',required=True,help='Path to the target fastq file that you want to demultiplex.')
    parser.add_argument('-r','--target-read',required=True,choices=['R1','R2','I1','I2'],help='Illumina read to which the target fastq corresponds (R1, R2, I1, or I2).')
    return parser

parser = parse_user_input()
ui = parser.parse_args()

if ui.mode == 'dual':
    if ui.index2_fastq==None:
        print('Error: Dual index demultiplexing requires index read 2 (I2) fastq file required for argument --index2-fastq') 
        exit()
    else:
        target=ui.target_fastq
        index1=ui.index1_fastq
        index2=ui.index2_fastq
        read=ui.target_read
        with open(ui.sample_table) as f:
            for line in f:
                llist = line.split()
                s=llist[0]
                i1=llist[1]
                i2=llist[2]
                cmd = 'zcat %(target)s | python dual_index_demux.py -i1 %(index1)s -i2 %(index2)s -ind1 %(i1)s -ind2 %(i2)s -s %(s)s | gzip > %(s)s_%(read)s_001.fastq.gz &' % vars()
                os.system(cmd)
elif ui.mode=='single':
    target=ui.target_fastq
    index1=ui.index1_fastq
    read=ui.target_read
    with open(ui.sample_table) as f:
        for line in f:
            llist=line.split()
            s=llist[0]
            i1=llist[1]
            cmd = 'zcat %(target)s | python single_index_demux.py -ind %(i1)s -s %(s)s -i %(index1)s | gzip > %(s)s_%(read)s_001.fastq.gz &' % vars()
            os.system(cmd)

