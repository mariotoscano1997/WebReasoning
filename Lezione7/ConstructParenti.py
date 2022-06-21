# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:21:42 2022

@author: tosca
"""

from rdflib import Graph, Namespace

g=Graph()

g.parse("Parents.ttl")



q = """
    construct {
        ?Father wr:hasSon ?Son.        
        }
    where{
        ?Son rdf:type wr:Man.
        ?Son wr:hasFather ?Father.
         
         
          }
    """
    
q1 =  """
    construct {
        ?Mother wr:hasSon ?Son.        
        }
    where{
        ?Son rdf:type wr:Man.
        ?Son wr:hasMother ?Mother.         
          }
    """
result = g.query(q,initNs=dict(
        rdf=Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
        wr = Namespace("https://www.dropbox.com/home/Webreasoning/voc.ttl/")))
resultMother = g.query(q1,initNs=dict(
        rdf=Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
        wr = Namespace("https://www.dropbox.com/home/Webreasoning/voc.ttl/")))

g+=result
g+=resultMother


g.serialize(destination="hasSon.ttl", format="turtle")