import graphviz as gv
import functools

graph = functools.partial(gv.Graph)
#digraph = functools.partial(gv.Graph)


g1 = gv.Digraph ( comment='The Round Table')
#g1=gv.AGraph(ranksep='0.1')
nodes = ['A', 'B', ('C', {})]

edges = [
    ('A', 'B'),
    ('B', 'C'),
    (('A', 'C'), {}),
]

def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph

#g1 = add_nodes(g1, nodes)
#g1 = add_edges(g1, edges)

g1.node_attr['shape']='record'
g1.node_attr['width']='0.01'
g1.graph_attr['rankdir'] = 'LR'



g1.node('A', label = 'A: ROOT', rank = "A")
g1.node('B', 'B: King Arthur', rank = "B")
g1.node('C', 'C: King Arthur', rank = "A")
g1.node('D', 'D: King Arthur', rank = "A")
g1.node('E', 'E: King Arthur', rank = "A")
g1.node('F', 'F: King Arthur', rank = "A")
g1.node('G', label = 'G: ROOT', rank = "A")
g1.node('H', 'H: King Arthur', rank = "A")
g1.node('I', 'I: King Arthur', rank = "A")
g1.node('J', 'J: King Arthur', rank = "A")
g1.node('K', 'K: King Arthur', rank = "A")
g1.node('L', 'L: King Arthur', rank = "A")

g1.edge('A', 'B', label="haha", constraint = "false", style = "dotted", arrowhead = "none", weight = "5")
g1.edge('B', 'C', label="haha", constraint = "false", style = "dotted", arrowhead = "none")
g1.edge('C', 'D', label="haha", constraint = "false", style = "dotted", arrowhead = "none")
g1.edge('D', 'E', label="haha", style = "dotted", arrowhead = "none")
g1.edge('E', 'F', label="haha", style = "dotted", arrowhead = "none")
g1.edge('F', 'G', label="haha", style = "dotted", arrowhead = "none", weight = "5")
g1.edge('G', 'H', label="haha", style = "dotted", arrowhead = "none")
g1.edge('H', 'I', label="haha", style = "dotted", arrowhead = "none")
g1.edge('I', 'J', label="haha", style = "dotted", arrowhead = "none")
g1.edge('J', 'K', label="haha", style = "dotted", arrowhead = "none")
g1.edge('K', 'L', label="haha", style = "dotted", arrowhead = "none")

g1.edge('A', 'B', label="haha", arrowhead="none")
g1.edge('B', 'C', label="haha")
g1.edge('C', 'D', label="haha", weight = "0")
g1.edge('F', 'J', label="haha", weight = "0")
g1.edge('D', 'B', label="haha", arrowhead="none")
g1.edge('B', 'K', label="haha")
g1.edge('L', 'A', label="haha", weight = "0")
g1.edge('E', 'F', label="haha", weight = "2")
g1.edge('D', 'J', label="haha", arrowhead="none")
g1.edge('I', 'J', label="haha")
g1.edge('K', 'D', label="haha", weight = "0")
g1.edge('L', 'B', label="haha", weight = "0")

#stringem = (g1.source)
#start = g1.source.find('{')

#stringem = stringem[:start] + "rankdir=LR;" + stringem[start:]

#g1.setsource(stringem)

#g1.

#g1.attr('graph',{("rankdir","LR")})
print(g1.source)  # doctest: +NORMALIZE_WHITESPACE
g1.render('test-output/round-table.gv', view=True)
'test-output/round-table.gv.pdf'