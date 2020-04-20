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


    def drawBar(self, cluster_class):
        """"""

        self.FIGURE = go.Figure()

        if cluster_class == 'Cell Type':

            for trace in self.METADATA.FEATURE['typeSet']:

                self.FIGURE.add_trace(
                    go.Bar(
                        name=trace,

                        x=[trace],
                        y=[self.METADATA.DATATABLE[f.TYPE == trace, 'CELL'].nrows],

                        marker_color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],
                        marker_line_color='white',

                        hoverinfo='text',
                        hovertext=trace + '<br />' + str(self.METADATA.DATATABLE[f.TYPE == trace, 'CELL'].nrows) + ' cells',

                        showlegend=False
                    )
                )

        if cluster_class == 'Source':

            for trace in self.METADATA.FEATURE['sourceSet']:

                self.FIGURE.add_trace(
                    go.Bar(
                        name=trace,

                        x=[trace],
                        y=[self.METADATA.DATATABLE[f.SOURCE == trace, 'CELL'].nrows],

                        marker_color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],
                        marker_line_color='white',

                        hoverinfo='text',
                        hovertext=trace + '<br />' + str(self.METADATA.DATATABLE[f.SOURCE == trace, 'CELL'].nrows) + ' cells',

                        showlegend=False
                    )
                )


        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                text='Cell Number in Each ' + cluster_class, 
                font=dict(
                    
                    family='Arial', 
                    size=self.TITLE_SIZE

                )

            ),

            yaxis_type='log', 
            xaxis_tickangle=-45

        )