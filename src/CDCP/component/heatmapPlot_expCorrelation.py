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


    def drawHeatmap(self, corList):
        """"""

        self.FIGURE = go.Figure()

        X = corList
        Y = X
        Z = self.METADATA.MATRIX

        self.FIGURE.add_trace(
            go.Heatmap(
                name='Correlation of Expression',

                x=X,
                y=Y,
                z=Z,

                xgap=1,
                ygap=1,

                colorscale='Viridis',

                zmax=1,
                zmin=-1
            )
        )

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                text='Correlation of Expression',
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE

                )

            ),

            legend=dict(

                itemsizing='constant'

            ),

            showlegend=True

        )