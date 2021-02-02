import argparse as ag
from Bio.Sequencing.Applications import BwaIndexCommandline, BwaIndexCommandline, SamtoolsCalmdCommandline, SamtoolsMpileupCommandline, SamtoolsSortCommandline, SamtoolsViewCommandline
import pandas as pd
import pandas_genomics
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import vcf
from datetime import datetime
import time
import os
parser = ag.ArgumentParser(description='GSA and Variant calling')
parser.add_argument('Input',help='Input sequence(s)', type = str, nargs="+")
parser.add_argument('Outdir', help='Output directory (deafault = current directory)',type=str,default='.')
parser.add_argument('-v', '--verbose',help="increase output verbosity", action="store_true")
parser.add_argument('Ref', help= 'Reference sequence', type = 'str')
args = parser.parse_args()
input_sequences = args.Input
output = args.Outdir
ref = args.Ref
os.mkdir(f'{output}/refrence')
os.mkdir(f'{output}/raw_sams')
os.mkdir(f'{output}/sorted_sams')
os.mkdir(f'{output}/bams')

