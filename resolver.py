#!/usr/bin/env python3
import dns.resolver

record = input("Input record: ")
path = input("Input path: ")

my_resolver = dns.resolver.Resolver(configure=False)
my_resolver.nameservers = ['8.8.8.8', '1.1.1.1']

with open(path, 'r') as f:
    for line in f:
        if record == 'A':
            result = my_resolver.query(line.rstrip(), record)
            for rdata in result:
                print(rdata.address)
        if record == 'PTR':
            result = my_resolver.resolve_address(line.rstrip())
            for rdata in result:
                print(rdata.target)