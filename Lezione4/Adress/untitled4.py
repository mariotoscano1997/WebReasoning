# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:56:11 2022

@author: tosca
"""
from rdflib import Graph, Namespace, XSD,Literal

exstaff = Namespace("http://www.example.org/staffid/")
exaddressid = Namespace("http://www.example.org/addressid/")
exterms = Namespace("http://www.example.org/terms/")
wr = Namespace("https://www.dropbox.com/home/WebReasoning/voc.ttl#")
dbr = Namespace("https://dbpedia.org/page/")

Bedford="Bedford,_Massachusetts"

g=Graph()
g.bind("exstaff",exstaff)
g.bind("exaddressid",exaddressid)
g.bind("exterms",exterms)
g.bind("wr",wr)
g.bind("dbr",dbr)

g.add((exstaff.john, exterms.adress, exaddressid.n85740))
g.add((exaddressid.n85740,wr.civicnumber, Literal('1501', datatype=XSD.integer)))
g.add((exaddressid.n85740,wr.street, Literal('Gran Avenue')))
g.add((exaddressid.n85740,wr.town,dbr.Bedford))
g.add((exaddressid.n85740,wr.state,dbr.Massachusetts))
g.add((exaddressid.n85740,wr.ZIP, Literal('01730', datatype=XSD.integer)))

g.serialize(destination="Address.ttl", format="turtle")

