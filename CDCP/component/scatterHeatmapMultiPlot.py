#!/usr/bin/env python3




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


    def drawMultiScatterHeatmap(self, fieldNames):
        """"""

        self.FIGURE = make_subplots(2, 2, specs=[[None, {}], 
                                                 [{}, {}]],
                                                 subplot_titles=(fieldNames[0] + ' (Exp.)', 
                                                    'Co-exp. ' + fieldNames[1],
                                                    'Co-exp. ' + fieldNames[2]))

        X = self.METADATA.DATATABLE['UMAP1'].to_list()[0]
        Y = self.METADATA.DATATABLE['UMAP2'].to_list()[0]

        self.FIGURE.add_trace(
            go.Scattergl(
                name='Exp.',

                x=X,
                y=Y,

                mode='markers',
                marker=dict(
                
                    size=2,
                    color=self.METADATA.DATATABLE[fieldNames[0]].to_list()[0],
                    colorscale=['darkblue', 'yellow', 'red'],
                    showscale=True

                ),
                
                hoverinfo='text',
                hovertext=self.METADATA.DATATABLE[fieldNames[0]].to_list()[0]
            ),

            1, 2
        )
        
        for i in range(1, len(fieldNames)):

            self.FIGURE.add_trace(
                go.Scattergl(
                    name=fieldNames[i],

                    x=X,
                    y=Y,

                    mode='markers',
                    marker=dict(
                    
                        size=2,
                        color=self.METADATA.DATATABLE[fieldNames[i]].to_list()[0],
                        colorscale=['lightgrey', 'green'],
                        opacity = 0.6

                    ),

                    hoverinfo='text',

                    showlegend=False
                ),

                2, i
            )

        self.FIGURE.update_xaxes(matches='x')
        self.FIGURE.update_yaxes(matches='y')

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                text='Expression Heatmap (Multiplot)', 
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE

                )

            )
            
        )