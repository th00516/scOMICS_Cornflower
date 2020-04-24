#!/usr/bin/env python3


"""

    Author: Hao Yu (yuhao@genomics.cn)
    Date:   2020-04-24
    
"""




import plotly.graph_objects as go

from datatable import f




class  Illustration:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj

        self.FIGURE = None

        self.TITLE_SIZE = 18


    def drawSplitViolin(self, fieldName1, fieldName2):
        """"""

        self.FIGURE = go.Figure()

        for trace in self.METADATA.FEATURE['typeSet']:

            self.FIGURE.add_trace(
                go.Violin(
                    name=trace,

                    side='negative',

                    y=self.METADATA.DATATABLE[f.TYPE == trace, fieldName1].to_list()[0],

                    fillcolor=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],
                    line_color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],
                    opacity=1.0,

                    line_width=2,

                    points=False,
                    spanmode='hard',

                    hoverinfo='text',
                    hovertext=fieldName1,

                    showlegend=False
                )
            )

            self.FIGURE.add_trace(
                go.Violin(
                    name=trace,

                    side='positive',

                    y=self.METADATA.DATATABLE[f.TYPE == trace, fieldName2].to_list()[0],

                    fillcolor=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],
                    line_color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],
                    opacity=0.5,

                    line_width=2,

                    points=False,
                    spanmode='hard',

                    hoverinfo='text',
                    hovertext=fieldName2,

                    showlegend=False
                )
            )

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                text='Exp. Distribution of ' + \
                '<i>' + fieldName1 + '</i> (<b>LEFT side</b>) and ' + \
                '<i>' + fieldName2 + '</i> (<b>RIGHT side</b>) in Each Cluster', 
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE
                    
                )

            ),

            xaxis_tickangle=-45
        )
