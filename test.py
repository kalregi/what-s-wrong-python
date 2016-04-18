from graphviz import Digraph

print("jó lesz?")



class draw(object):

    def drawGraph(self, edges, tokens):
        dot = Digraph (comment='Példa gráf')

        dot.node_attr['shape']='record'
        dot.node_attr['width']='0.1'
        dot.node_attr['height']='0.1'

        dot.graph_attr['rankdir'] = 'LR'
        dot.graph_attr['outputorder']='edgesfirst'
        #for edge in edges:
        #    if edge._From is not None and edge._From not in tokens:
        #        tokens.append(edge._From)
        #    if edge._To is not None and edge._From not in tokens:
        #        tokens.append(edge._To)
        #dot.attr('node',{("rankdir","TD")})
        #dot.graph_attr['splines']='ortho'
        #dot.edge_attr['labelfloat'] = "true"
        beforeindex = ""
        for token in tokens:
            if 'Index' in token.getPropertyTypes():
                if 'Index' in token.getPropertyTypes() and 'Word' in token.getPropertyTypes():
                    #dot.node(token.getProperty('Index')+":Index", token.getProperty('Word'))
                    label = ""
                    for property in token.getPropertyTypes():
                        label += "<"+property+"> " + token.getProperty(property) + " | "
                    dot.node(token.getProperty('Index'), label[:-2])
                    if beforeindex != "":
                        dot.edge(beforeindex, token.getProperty('Index') + ":Index", style="invisible", arrowhead="none")
                    beforeindex = token.getProperty('Index')+ ":Index"

        for edge in edges:
            if edge._From is not None and edge._To is not None:
                if 'Index' in edge._From.getPropertyTypes() and 'Index' in edge._To.getPropertyTypes():
                    dot.edge(edge._From.getProperty('Index')+ ":Index", edge._To.getProperty('Index')+ ":Index", constraint='false',label = edge._label )
        print(dot.source)
        dot.render('test-output/round-table.gv', view=False)
