#!/usr/local/bin/p'y'thon2.7
# encoding: utf-8


import os
import sys
import numpy as NP
from redis import StrictRedis as redis


r0 = redis(db=0)

def timeseries_to_redis(fname, game, end_time, time_step=86400000):
    with open(fname, "r") as f:
        data = [ row.strip().split(',')[-1] for row in f.readlines() 
                if not row.startswith('#')][1:]
    this_time = end_time
    for datapoint in data:
        key = '{0}:{1}'.format(game, this_time)
        r0.hset('game:backyardMonsters', key, datapoint)
        this_time -= time_step


ddir = '/Users/doug/Dropbox/DataArchive/competitor intelligence/raw data appdata'
dfile = 'BackYard_Monsters_to29Jun11.csv'

fname = os.path.join(ddir, dfile)

timeseries_to_redis(fname, 'BackyardMonsters', 1309392000000)

