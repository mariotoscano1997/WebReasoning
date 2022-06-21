# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 01:16:42 2022

@author: tosca
"""

from rdflib import Graph, RDF, Literal, Namespace, BNode

g = Graph()

dbr = Namespace("https://dbpedia.org/page/")
dbo = Namespace("https://dbpedia.org/ontology/")
lit = Namespace("http://www.workingontologist.org/Examples/Chapter3/shakespeare#")


n1 = BNode()


g.add((n1, lit.title, dbr['Adventures_of_Huckleberry_Finn']))
g.add((n1, lit.author, dbr["Mark_Twain"]))
g.add((dbr["Mark_Twain"], dbo.pseudonym, Literal("Samuel Clemens")))

n2 = BNode()

g.add((n2, lit.title, dbr["The_Adventures_of_Tom_Sawyer"]))
g.add((dbr["Mark_Twain"], lit.wrote, n2))

n3 = BNode()
g.add((dbr["Mark_Twain"], dbo.child, n3))
g.add((n3, RDF.type, RDF.Bag))
g.add((n3,RDF.List, dbr["Jean_Clemens"]))
g.add((n3,RDF.List, dbr["Clara_Clemens"]))
g.add((n3,RDF.List, dbr["Susy_Clemens"]))

g.serialize(destination="EsercizioPerCasa.ttl", format="turtle")
#Adventures_of_Huckleberry_Finn
#Mark_Twain
#The_Adventures_of_Tom_Sawyer
#Jean_Clemens
#Clara_Clemens
#Susy_Clemens
#Missouri