#!/usr/bin/env python

import argparse
import json
import csv
import yaml
import pdb

class Inventory(object):

    def __init__(self):
        self.inventory = {"_meta": {"hostvars": {}}}
        self.parse_cli_args()

        if self.args.list:
            self.inventory = self.read_dynamic_inventory()
        elif self.args.host:
            self.inventory = self.inventory
        else:
            self.inventory = self.inventory

        print json.dumps(self.inventory)

    def open_yml_file(self, ymlFile):
        fileData = open(ymlFile)
        vars = yaml.load(fileData)
        return vars

    def open_csv_file(self, csvFile):
        fileData = open(csvFile)
        header = next(fileData)
        csv_file = csv.reader(fileData, delimiter="\t")
        data = []
        for line in enumerate(csv_file):
            data.append(line)
        fileData.close()
        return data, header

    def read_dynamic_inventory(self):
        inventory = self.inventory
        (csvData, header) = self.open_csv_file('big.csv')

        vars = self.add_vars()

        headerData = []
        hdrData = header.split(",")
        for i in hdrData:
            headerData.append(i)
        headerData[-1] = headerData[-1].strip()

        # Same as host vars but not in a list
        hostdata = []
        for a in csvData:
            for b in a[1]:
                hostdata.append(b)

        # Iterate over list of hostvars
        group_vars = {}
        hostvars = []
        for i in hostdata:
            for j in i.split(","):
                hostvars.append(j)

            data = dict(zip(headerData, hostvars))

            # pdb.set_trace()


            group_vars.update({hostvars[0]: {"hosts": hostvars[2], "vars": vars}})
            inventory["_meta"]["hostvars"].update({hostvars[2]: data})
            new_inventory = group_vars.copy()
            new_inventory.update(inventory)
            print(hostvars)

            hostvars = []

        print(hostvars)
        return new_inventory


    def add_vars(self):
        data = self.open_yml_file('group_vars.yml')
        return data





    def parse_cli_args(self):
        parser = argparse.ArgumentParser(description='Produce an Ansible Inventory from a file')
        parser.add_argument('--list', action='store_true', help='List Hosts')
        parser.add_argument('--host', action='store', help='Get all the variables about a specific host')

        self.args = parser.parse_args()


Inventory().add_vars()