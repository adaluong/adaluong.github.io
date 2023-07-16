#!/usr/bin/env python3
# generate img html given a folder name
# run from /assets/img/photography folder 
# usage: ./img_html.py [folder]

import glob
import sys

if len(sys.argv) != 2:
    print("usage: ./img_html.py [folder]")
    exit(1)

base_path = "/assets/img/"
folder = sys.argv[1]
files = glob.glob(folder + "/*")

for img_path in files:
    print('  <div class="mItem">')
    print(f'    {{% picture loaded gallery/{img_path} %}}')
    print('  </div>')
