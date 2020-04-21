#!/usr/bin/env python3




import plotly.graph_objects as go
from plotly.subplots import make_subplots




class  Illustration:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj

        self.FIGURE = None

        self.TITLE_SIZE = 18


    def drawMultiScatterHeatmap(self, fieldNames):
        """"""

        title = [
            
            fieldNames[1] + ' (Co-exp.)', 
            fieldNames[0] + ' (Exp.)'

        ]

        if len(fieldNames) > 2:
            for i in range(2, len(fieldNames)):
                title.append(fieldNames[i] + ' (Co-exp.)')


        self.FIGURE = make_subplots(2, 2, specs=[[{}, {}], [{}, {}]], subplot_titles=title)

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

        self.FIGURE.add_trace(
            go.Scattergl(
                name=fieldNames[1],

                x=X,
                y=Y,

                mode='markers',
                marker=dict(
                
                    size=2,
                    color=self.METADATA.DATATABLE[fieldNames[1]].to_list()[0],
                    colorscale=['lightgrey', 'green'],
                    showscale=False,
                    opacity = 0.6

                ),

                hoverinfo='text',

                showlegend=False
            ),

            1, 1
        )
        
        if len(fieldNames) > 2:

            for i in range(2, len(fieldNames)):

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
                            showscale=False,
                            opacity = 0.6

                        ),

                        hoverinfo='text',

                        showlegend=False
                    ),

                    2, i - 1
                )


        self.FIGURE.update_xaxes(matches='x')
        self.FIGURE.update_yaxes(matches='y')

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                text='Expression and Co-expression Heatmap', 
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE

                )

            )
            
        )