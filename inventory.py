#!/usr/bin/env python

import argparse
import json
import csv


class Inventory(object):

    def __init__(self):

        self.inventory = {"group": {"hosts": [], "vars": {}}, "_meta": {"hostvars": {}}}
        self.parse_cli_args()

        if self.args.list:
            self.inventory = self.read_dynamic_inventory()
        elif self.args.host:
            self.inventory = self.inventory
        else:
            self.inventory = self.inventory

        print json.dumps(self.inventory)

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
        hostvars = []
        for i in hostdata:
            for j in i.split(","):
                hostvars.append(j)
            inventory["group"]["hosts"].append(hostvars[1])

            data = dict(zip(headerData, hostvars))
            inventory["_meta"]["hostvars"].update({hostvars[1]: data})
            hostvars = []

        return inventory

    def parse_cli_args(self):

        parser = argparse.ArgumentParser(description='Produce an Ansible Inventory from a file')
        parser.add_argument('--list', action='store_true', help='List Hosts')
        parser.add_argument('--host', action='store', help='Get all the variables about a specific host')

        self.args = parser.parse_args()


Inventory().read_dynamic_inventory()