#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json


string_data = ""
for line in open('model_classfier_edit.json'):
    string_data = string_data + line
data_dict = json.loads(string_data)

one_data = {}
zero_data = {}

for k,v in data_dict["storage"]["weight"].items():
    print( v )
    if v["1"]["v1"] in one_data:
        one_data.update({k: v["1"]["v1"]})
    if v["0"]["v1"] in one_data:
        zero_data.update({k: v["0"]["v1"]})

sorted(one_data.items(), key=lambda x: x[1])
sorted(zero_data.items(), key=lambda x: x[1])
