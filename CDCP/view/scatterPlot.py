#!/usr/bin/env python3




import plotly.graph_objects as go

from datatable import f




class  Illustration:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj

        self.FIGURE = None

        self.TITLE_SIZE = 28


    def drawScatter(self, dim):
        """"""

        self.FIGURE = go.Figure()

        for trace in self.METADATA.FEATURE['typeSet']:

            X = self.METADATA.DATATABLE[f.TYPE == trace, 'UMAP1'].to_list()[0]
            Y = self.METADATA.DATATABLE[f.TYPE == trace, 'UMAP2'].to_list()[0]
            Z = self.METADATA.DATATABLE[f.TYPE == trace, 'UMAP3'].to_list()[0]

            if dim == 2:

                self.FIGURE.add_trace(
                    go.Scattergl(
                        name=trace,

                        x=X,
                        y=Y,

                        mode='markers',
                        marker=dict(
                        
                            size=2,
                            color=self.METADATA.COLOR[f.TYPE == trace, 'COLOR'][0, 0]

                        ),

                        hoverinfo='text',
                        hovertext=trace
                    )
                )

            if dim == 3:

                self.FIGURE.add_trace(
                    go.Scatter3d(
                        name=trace,

                        x=X,
                        y=Y,
                        z=Z,

                        mode='markers',
                        marker=dict(
                        
                            size=2,
                            color=self.METADATA.COLOR[f.TYPE == trace, 'COLOR'][0, 0],

                        ),
                        
                        hoverinfo='text',
                        hovertext=trace
                    )
                )


        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                text='Cell Type Cluster',
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE

                )

            ),

            legend=dict(

                itemsizing='constant'

            )

        )