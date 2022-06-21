# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:59:38 2022

@author: tosca
"""

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
        ?x1 wr:hasSibling ?y1.
        ?x2 wr:hasSibling ?y2.
        ?x3 wr:hasParent ?y3.
        ?x4 wr:hasParent ?y4.        
        }
    where{
        ?x1 wr:hasBrother ?y1.
        ?x2 wr:hasSister ?y2.
        ?x3 wr:hasMother ?y3.
        ?x4 wr:hasFather ?y4.
         
          }
    """

result = g.query(q,initNs=dict(
        rdf=Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
        wr = Namespace("https://www.dropbox.com/home/Webreasoning/voc.ttl/")))


g+=result



g.serialize(destination="hasSiblingParent.ttl", format="turtle")