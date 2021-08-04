# demux10x

This code is for demultiplexing both single- and dual-index Illumina sequencing runs starting from fastq files.  The envisioned application is demultiplexing the index reads from various types of 10x Genomics sequencing library construction methods, but the code is broadly applicable.  It requires Python >=3.6.

For single-index Illumina runs, a two-column, tab-delimited input file is required. The first column contains the names of each sample; the second column contains the index sequences for each sample.  For single-index Illumina runs, example usage is as follows:

```
python demux10x.py --mode single --sample-table sample_index_table.txt -i1 Undetermined_S0_L001_I1_001.fastq.gz --target-fastq Undetermined_S0_L001_R1_001.fastq.gz -r R1 -l L001
```

This command would use the index read fastq Undetermined_S0_L001_I1_001.fastq.gz to identify all of the Illumina clusters containing the index sequences in sample_index_table.txt and create a new set of fastqs, one for each sample in sample_index_table.txt, containing the appropriate reads from Undetermined_S0_L001_R1_001.fastq.gz, which corresponds to read 1 and lane 1.

For dual-index Illumina runs, a three-column, tab-delimited input file is required. The first column contains the names of each sample; the second and third columns contain the two index sequences for each sample. For dual-index Illumina runs, example usage is as follows:

```
python demux10x.py --mode dual --sample-table sample_index_table.txt -i1 Undetermined_S0_L001_I1_001.fastq.gz -i2 Undetermined_S0_L001_I2_001.fastq.gz --target-fastq Undetermined_S0_L001_R2_001.fastq.gz  -r R2 -l L001
```

This command would use the two index read fastqs Undetermined_S0_L001_I1_001.fastq.gz and Undetermined_S0_L001_I2_001.fastq.gz to identify all of the Illumina clusters containing the correctly paired index sequences in sample_index_table.txt and create a new set of fastqs, one for each sample in sample_index_table.txt, containing the appropriate reads from Undetermined_S0_L001_R2_001.fastq.gz, which corresponds to read 2 and lane 1.

Note that for both single- and dual-index demultiplexing, the program assumes that the index sequences are separated by at least Hamming distance = 3, allowing the correction of a single-base error. The samples in sample_index_table.txt are demultiplexed in parallel, ideally with two CPU threads for each sample (one for decompressing and streaming the target fastq file; one for demultiplexing and writing the output file).



