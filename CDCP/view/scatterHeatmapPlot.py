#!/usr/bin/env python3




import plotly.graph_objects as go




class  Illustration:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj

        self.FIGURE = None

        self.TITLE_SIZE = 28


    def drawScatterHeatmap(self, fieldName):
        """"""

        self.FIGURE = go.Figure()

        X = self.METADATA.DATATABLE['UMAP1'].to_list()[0]
        Y = self.METADATA.DATATABLE['UMAP2'].to_list()[0]

        self.FIGURE.add_trace(
            go.Scattergl(
                name='Expression',

                x=X,
                y=Y,

                mode='markers',
                marker=dict(
                
                    size=2,
                    color=self.METADATA.DATATABLE[fieldName].to_list()[0],
                    showscale=True

                ),
                
                hoverinfo='text',
                hovertext=self.METADATA.DATATABLE[fieldName].to_list()[0]
            )
        )

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                text='Expression Heatmap', 
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE

                )

            )
            
        )