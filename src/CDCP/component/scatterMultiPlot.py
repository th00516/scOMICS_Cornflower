#!/usr/bin/env python3


"""

    Author: Hao Yu (yuhao@genomics.cn)
    Date:   2020-04-24
    
"""




import plotly.graph_objects as go
from plotly.subplots import make_subplots

from datatable import f




class  Illustration:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj

        self.FIGURE = None

        self.TITLE_SIZE = 18


    def drawMultiScatter(self, sources):
        """"""

        self.FIGURE = make_subplots(1, len(sources), subplot_titles=(sources))
        
        for i in range(0, len(sources)):

            for trace in self.METADATA.FEATURE['typeSet']:
                
                X = self.METADATA.DATATABLE[(f.TYPE == trace) & (f.SOURCE == sources[i]), 'UMAP1'].to_list()[0]
                Y = self.METADATA.DATATABLE[(f.TYPE == trace) & (f.SOURCE == sources[i]), 'UMAP2'].to_list()[0]

                self.FIGURE.add_trace(
                    go.Scattergl(
                        name=trace + ' (' + sources[i] + ')',

                        x=X,
                        y=Y,

                        mode='markers',
                        marker=dict(
                        
                            size=2,
                            color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],

                        ),
                        
                        hoverinfo='text',
                        hovertext=trace,

                        legendgroup=trace
                    ),

                    1,
                    i + 1
                )

        self.FIGURE.update_xaxes(matches='x')
        self.FIGURE.update_yaxes(matches='y')

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                text='Cluster by Cell Type (Multiplot)', 
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE
                    
                )

            ),

            legend=dict(

                itemsizing='constant'

            )
            
        )