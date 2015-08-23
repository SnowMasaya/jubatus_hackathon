#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re

f1 = open("minister_exp_count.csv", "r")
key_data = ()
election_data = {}

for line in f1.readlines():
    split_data = line.split(',')
    split_data[0] = re.sub(r'_[0-9]', "" , split_data[0])
    split_data[2] = re.sub(r'\n', "" , split_data[2])
    key_data = (split_data[0], split_data[1])
    if key_data not in election_data:
        election_data.update({key_data: split_data[2]})

    
f = open("j_c.json", "r")

for line in f.readlines():
    label, dat = line[:-1].split('\t')
    split_data = dat.split(",")
    for data in split_data:
        data = data.replace("\"", "")
        if "flame" in data:
            year = re.sub(r'{flame:', "" , data)
            if year == "y1985":
                year = '2000'
            if year == "y1990":
                year = '2005'
            if year == "y1995":
                year = '2010'
            if year == "y2000":
                year = '2015'
        if "cand_last" in data:
            name = re.sub(r'cand_last:', "" , data)
            key_data = (year,name)
            if key_data in election_data:
                label = 1
                election_count = ",\"election_count\":" + str(election_data[key_data]) + "}"
                dat = dat.replace("}", election_count)
                print(str(label) + "\t" + dat)
            else:
                label = 0
                election_count = ",\"election_count\":0}"
                dat = dat.replace("}", election_count)
                print(str(label) + "\t" + dat)
    

f.close()
