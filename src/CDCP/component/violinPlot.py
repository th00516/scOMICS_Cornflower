#!/usr/bin/env python3




import plotly.graph_objects as go

from datatable import f




class  Illustration:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj

        self.FIGURE = None

        self.TITLE_SIZE = 18


    def drawViolin(self, fieldName):
        """"""

        self.FIGURE = go.Figure()

        for trace in self.METADATA.FEATURE['typeSet']:

            self.FIGURE.add_trace(
                go.Violin(
                    name=trace,

                    y=self.METADATA.DATATABLE[f.TYPE == trace, fieldName].to_list()[0],

                    fillcolor=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],
                    line_color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],

                    line_width=2,

                    points=False,

                    hoverinfo='text',
                    hovertext=trace,

                    showlegend=False
                )
            )

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                text='Exp. Distribution of <i>' + fieldName +'</i> in Each Cluster', 
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE
                    
                )

            ),

            xaxis_tickangle=-45
        )
