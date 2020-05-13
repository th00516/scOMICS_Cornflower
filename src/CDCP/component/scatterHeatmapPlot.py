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


    def drawScatterHeatmap(self, fieldName):
        """"""

        self.FIGURE = go.Figure()

        X1 = self.METADATA.DATATABLE[f[fieldName] == 0, 'UMAP1'].to_list()[0]
        Y1 = self.METADATA.DATATABLE[f[fieldName] == 0, 'UMAP2'].to_list()[0]

        X2 = self.METADATA.DATATABLE[f[fieldName] > 0, 'UMAP1'].to_list()[0]
        Y2 = self.METADATA.DATATABLE[f[fieldName] > 0, 'UMAP2'].to_list()[0]

        C = self.METADATA.DATATABLE[f[fieldName] > 0, fieldName].to_list()[0]

        C = np.array(C)

        Cl = np.percentile(C, (self.FILTER_MIN))
        Ch = np.percentile(C, (self.FILTER_MAX))

        C[C < Cl] = Cl
        C[C > Ch] = Ch

        C = list(C)

        self.FIGURE.add_trace(
            go.Scattergl(
                name='Unexp.',

                x=X1,
                y=Y1,

                mode='markers',
                marker=dict(
                
                    size=2,
                    color='darkblue',
                    showscale=False

                ),
                
                hoverinfo='text',
                hovertext=self.METADATA.DATATABLE[f[fieldName] == 0, 'TYPE'].to_list()[0],

                showlegend=False
            )
        )

        self.FIGURE.add_trace(
            go.Scattergl(
                name='Exp.',

                x=X2,
                y=Y2,

                mode='markers',
                marker=dict(
                
                    size=2,
                    color=C,
                    colorscale=['darkblue', 'yellow', 'red'],
                    showscale=True

                ),
                
                hoverinfo='text',
                hovertext=self.METADATA.DATATABLE[f[fieldName] > 0, 'TYPE'].to_list()[0],

                showlegend=False
            )
        )

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                x=0.5,

                text='Expression of <i>' + fieldName + '</i>', 
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE

                )

            )
            
        )