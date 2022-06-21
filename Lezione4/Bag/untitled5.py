# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:10:03 2022

@author: tosca
"""
from rdflib import Namespace, Graph, RDF, Literal, BNode
stu = Namespace("http://www.example.org/students/")

cou = Namespace("http://www.example.org/courses/")

voc = Namespace("http://www.example.org/students/vocab#")

n1=BNode()

g = Graph();
g.bind("stu",stu)
g.bind("cou",cou)

g.bind("voc",voc)



g.add((n1,RDF.type, RDF.Bag))

g.add((cou.C345,voc.students, n1))

g.add((n1,RDF.List, stu.Anna))
g.add((n1,RDF.List, stu.Marco))
g.add((n1,RDF.List, stu.Giovanni))

g.serialize(destination="EsempioBag2.ttl", format="turtle")