#!/usr/bin/env python3


"""

    Author: Hao Yu (yuhao@genomics.cn)
    Date:   2020-04-24
    
"""




import plotly.graph_objects as go

from datatable import f

import numpy as np




class  Illustration:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj

        self.FIGURE = None

        self.TITLE_SIZE = 18

        self.FILTER_MIN = 0
        self.FILTER_MAX = 100


    def drawViolin(self, fieldName):
        """"""

        self.FIGURE = go.Figure()

        for trace in self.METADATA.FEATURE['typeSet']:

            Y = self.METADATA.DATATABLE[f.TYPE == trace, fieldName].to_list()[0]

            Y = np.array(Y)

            Yl = np.percentile(Y, (self.FILTER_MIN))
            Yh = np.percentile(Y, (self.FILTER_MAX))

            Y[Y < Yl] = Yl
            Y[Y > Yh] = Yh

            Y = list(Y)

            self.FIGURE.add_trace(
                go.Violin(
                    name=trace,

                    y=Y,

                    fillcolor=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],
                    line_color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],

                    line_width=2,

                    points=False,
                    spanmode='hard',

                    hoverinfo='text',
                    hovertext=trace,

                    showlegend=False
                )
            )

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                x=0.5,

                text='Expression of <i>' + fieldName + '</i> in Each Cluster',
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE
                    
                )

            ),

            xaxis_tickangle=-45
        )
