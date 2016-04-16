from graphviz import Digraph

print("jó lesz?")



class draw(object):

    def drawGraph(self, edges, tokens):
        dot = Digraph (comment='Példa gráf')
        #for edge in edges:
        #    if edge._From is not None and edge._From not in tokens:
        #        tokens.append(edge._From)
        #    if edge._To is not None and edge._From not in tokens:
        #        tokens.append(edge._To)
        dot.attr('graph',{("rankdir","TD")})
        #dot.attr('node',{("rankdir","TD")})
        dot.node_attr['shape']='circle'
        #dot.graph_attr['splines']='ortho'
        #dot.edge_attr['labelfloat'] = "true"

        for token in tokens:
            if 'Index' in token.getPropertyTypes():
                if 'Index' in token.getPropertyTypes() and 'Word' in token.getPropertyTypes():
                    dot.node(token.getProperty('Index'), token.getProperty('Word'))
        for edge in edges:
            if edge._From is not None and edge._To is not None:
                if 'Index' in edge._From.getPropertyTypes() and 'Index' in edge._To.getPropertyTypes():
                    dot.edge(edge._From.getProperty('Index'), edge._To.getProperty('Index'), constraint='false',label = edge._type )
        print(dot.source)
        dot.render('test-output/round-table.gv', view=True)




