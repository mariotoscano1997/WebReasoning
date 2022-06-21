# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:22:19 2022

@author: tosca
"""
from rdflib import Graph, RDF,BNode, Namespace
dbr= Namespace("https://dbpedia.org/page/")

g=Graph();

n1 = BNode()

g.add((n1, RDF.type, RDF.Statement))
g.add((n1, RDF.subject, dbr.Shakespeare))
g.add((n1, RDF.predicate, dbr.wrote))
g.add((n1, RDF.object, dbr.Hamlet))
g.add((dbr.Wikipedia, dbr.says, n1))

print(len(g))