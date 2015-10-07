#!/usr/bin/env python
__author__ = 'theodorkulczycki'

import os, sys
from ecmwfapi import ECMWFDataServer

# To run this example, you need an API key
# available from https://api.ecmwf.int/v1/key/

year = sys.argv[1]

name = 'raw'

outputDir = os.path.expandvars('$HOME/ERA_Interim/'+name+'/')

try:
    os.makedirs(outputDir)
except OSError:
    if not os.path.isdir(outputDir):
        raise

server = ECMWFDataServer()

startDate = year + '-01-01'
if year==2015:
    endDate = year + '-06-30'
else:
    endDate = year + '-12-31'


server.retrieve({
    'stream'    : "oper",
    'levtype'   : "sfc",
    'param'     : "201.128/202.128/228.128",
    'dataset'   : "interim",
    'step'      : "03/06/09/12",
    'grid'      : "0.25/0.25",
    'time'      : "00/12",
    'date'      : "{}/to/{}".format(startDate, endDate),
    'type'      : "fc",
    'class'     : "ei",
    'format'    : "netcdf",
    'target'    : "{}ERAI_mx2t_mn2t_tp_{}to{}.nc".format(outputDir, startDate, endDate)
})
