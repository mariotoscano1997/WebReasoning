# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:05:22 2022

@author: tosca
"""

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

g.parse("hasSiblingParent.ttl")



q = """
    construct {
        ?x wr:hasUncle ?z.
        }
    where{
        ?x wr:hasParent ?y.
        {?y wr:hasSibling ?z}UNION{?z wr:hasSibling ?y}.
        ?z rdf:type wr:Man.      
         
          }
    """

result = g.query(q,initNs=dict(
        rdf=Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
        wr = Namespace("https://www.dropbox.com/home/Webreasoning/voc.ttl/")))


g+=result



g.serialize(destination="hasUncle.ttl", format="turtle")