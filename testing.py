#python version 3.8
#Yaml testing


import yaml as ym
import psutil

#Pulls in name of nics
nics = psutil.net_if_addrs()
#prints name of nics
for i in nics:
	print(i)

name = input('please enter the name of the nic you wish to use(must be an exact match):')

#datsset1 is a dictionary of dictionaries to be converted into the YAMl f ile
dataset1 = {'network':
		       {'version':2,'Renderer': 'networkd','ethernets':
		           { name:
				       {'Dhcp4': 'yes'}}}}

#opens and writes the YAML file. Will create t he file it it doesn't exist.
with open('testyaml.yml','w') as outfile:
	ym.dump(dataset1,outfile, default_flow_style = False, sort_keys = False)
