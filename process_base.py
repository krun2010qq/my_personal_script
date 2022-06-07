#!/usr/bin/python

import argparse,sys,getopt,re

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0', help="Show program's version number and exit.")

parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='segment_file_size.py --input <input_filename_name> --output <output_file_name>')

parser.add_argument('-o', '--output', required=True,help="output file")

parser.add_argument('-i','--input', required=True,help='Input file')

args = parser.parse_args()
files_dic={}
base_files_dic={}
base_file_pattern1='^[0-9]*$'
base_file_pattern2='(^[0-9]*)(\.)([0-9]*$)'
base_file_pattern3='(^[0-9]*)(\_)(FSM$)'


pattern1=re.compile(base_file_pattern1)
pattern2=re.compile(base_file_pattern2)
pattern3=re.compile(base_file_pattern3)

if args.output:
    print("Processing the data")
    with open(args.input) as ls_file:
 	for line in ls_file:
             split_line=line.split()
             if len(split_line)>7:
                key,value = split_line[8],int(split_line[4])
                files_dic[key]=value
                if pattern1.match(key):
                    base_files_dic[key]=value
            

        for key in files_dic.keys():
            if pattern2.match(key):
                m=pattern2.match(key)
                key_base=m.group(1)
                try:
                    base_files_dic[key_base]=files_dic[key]+base_files_dic[key_base]
                except KeyError,e:
                    print "The base file does not exist", e

            if pattern3.match(key):
                m=pattern2.match(key)
                key_base=m.group(1)
                try:
                    base_files_dic[key_base]=files_dic[key]+base_files_dic[key_base]
                except KeyError,e:
                    print "The base file does not exist", e

        with open(args.output,'w') as output:
            for key in sorted(base_files_dic,key=base_files_dic.get, reverse=True):
                output_line="Base_File: "+key+" File_size: "+str(base_files_dic[key])+"\n"
                output.write(output_line)

    print("Done!")
