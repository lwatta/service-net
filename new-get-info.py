#!/usr/bin/python
import argparse
import string
import os
import urllib
import httplib
import re
import sys, traceback
import time
import json
import logging

# Define files to be used
novashow = open('./nova_list_all', 'r')
x=0
listoflists = []
record = []


# Loop through novahow info and print out data
for line in novashow.readlines():
#	print (line)
	temp = line.split("| ")
	print "Instance ID  %s" % temp[1]
	record.append(temp[1])
#	print "User ID %s" % temp[1]
#	print "Tenant ID %s" % temp[3]
        for templine in open('./keystone-user-list').readlines():
		if temp[2] in templine:
			print "have userid %s" % temp[2]
			ttemp = templine.split()
			print "have username %s" % ttemp[3]
                        record.append(ttemp[3])
			break
        for templine in open ('./keystone-tenant-list').readlines():
		if temp[3] in templine:
			print "have tenantid %s" % temp[3]
			ttemp = templine.split()
			print "have tenant name %s" % ttemp[3]
                        record.append(ttemp[3])
        for templine in open ('./nova-flavor-list').readlines():
		if temp[4] in templine:
			print "have flavor %s" % temp[4]
			ttemp = templine.split()
			print "have tenant name %s" % ttemp[3]
                        record.append(ttemp[3])
	print "name ID %s" % temp[5]
	record.append(temp[5])
	print "network is %s" % temp[6]
	record.append(temp[6])
	print "host is %s " % temp[7]
	record.append(temp[7])
	listoflists.append(record)
	x = x+1
	record = []

		
#print (len(listoflists))

output = open('./output', 'w')
for item in listoflists:
#	print (item)
	output.write("%s\n" % item)

output.close()

sys.exit(0)

