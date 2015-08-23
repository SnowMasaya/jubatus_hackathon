#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,json
import json

from jubatus.classifier.client import Classifier
from jubatus.classifier.types import LabeledDatum
from jubatus.common import Datum
from sklearn.cross_validation import train_test_split
import numpy
from itertools import izip


def parse_args():
    from optparse import OptionParser, OptionValueError
    p = OptionParser()
    p.add_option('-s', '--server_ip', action='store',
                 dest='server_ip', type='string', default='127.0.0.1')
    p.add_option('-p', '--server_port', action='store',
                 dest='server_port', type='int', default='9199')
    p.add_option('-n', '--name', action='store',
                 dest='name', type='string', default='tutorial')
    return p.parse_args()

def get_most_likely(estm):
    ans = None
    prob = None
    result = {}
    result[0] = ''
    result[1] = 0
    for res in estm:
        if prob == None or res.score > prob :
            ans = res.label
            prob = res.score
            result[0] = ans
            result[1] = prob
    return result

def cross_validation_python():
    train_data = numpy.array([])
    train_label = numpy.array([])
    test_data = numpy.array([])
    test_label = numpy.array([])
    x_vector = []
    y_vector = []
    first_flag = 1 
    for line in open('election_data.json'):
        label, dat = line[:-1].split('\t')
        y_vector.append(label)
        x_vector = numpy.array(dat)
        if first_flag == 1:
            train_data = numpy.hstack((train_data, x_vector))
            train_label = numpy.array(y_vector)
            first_flag = 0
        else:
            train_data = numpy.vstack((train_data, x_vector))
            train_label = numpy.array(y_vector)
    train_list = [train_data, train_label]
    return train_list


if __name__ == '__main__':
    options, remainder = parse_args()

    classifier = Classifier(options.server_ip,options.server_port, options.name, 10.0)


    train_list = cross_validation_python()
    data_train, data_test, label_train, label_test = train_test_split(train_list[0], train_list[1])

    for label, dat in izip(label_train, data_train):
        data_dict = json.loads(dat[0])
        datum = Datum(data_dict)
        classifier.train([LabeledDatum(label, datum)])





    count_ok = 0
    count_ng = 0
    #for label, dat in izip(label_test, data_test):
    for line in open('j_c_2015.json'):
        label, dat = line[:-1].split('\t')
        data_dict = json.loads(dat)
        datum = Datum(data_dict)
        ans = classifier.classify([datum])
        if ans != None:
            estm = get_most_likely(ans[0])
            if (estm[0] == "1"):
                result = "OK"
                print(dat)
                print(result + "," + label + ", " + estm[0] + ", " + str(estm[1]))
                count_ok += 1
            else:
                result = "NG"
                count_ng += 1
    print("===================")
    print("OK: {0}".format(count_ok))
    print("NG: {0}".format(count_ng))
