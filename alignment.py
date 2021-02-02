import argparse as ag
from Bio.Sequencing.Applications import BwaIndexCommandline, BwaMemCommandline, SamtoolsCalmdCommandline, SamtoolsMpileupCommandline,SamtoolsFixmateCommandline, SamtoolsSortCommandline, SamtoolsViewCommandline
import pandas as pd
import pandas_genomics
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import vcf
from datetime import datetime
import time
import os
from shutil import copyfile
parser = ag.ArgumentParser(description='GSA and Variant calling')
parser.add_argument('Input',help='Input sequence(s)', type = str, nargs="+")
parser.add_argument('Outdir', help='Output directory (deafault = current directory)',type=str,default='.')
parser.add_argument('-v', '--verbose',help="increase output verbosity", action="store_true")
parser.add_argument('Ref', help= 'Reference sequence', type = str)
args = parser.parse_args()
input_sequences = args.Input
output = args.Outdir
ref = args.Ref
os.mkdir(f'{output}/ref')
os.mkdir(f'{output}/sams')
os.mkdir(f'{output}/sorted_bams')
os.mkdir(f'{output}/bams')
copyfile(ref,f'{output}/ref/ref.fasta')
ref = f'{output}/ref/ref.fasta'
cmd = BwaIndexCommandline (infile=ref)
cmd()
for i in input_sequences:
    cmd = BwaMemCommandline(reference = ref,read_file1= i)
    outname = os.path.splitext(os.path.basename(i))[0]
    cmd(stdout=f'{output}/sams/{outname}.sam')
    cmd = SamtoolsFixmateCommandline(
        input_file=f'{output}/sams/{outname}.sam',
        output_file=f'{output}/bams/{outname}.bam')
    cmd()
    

