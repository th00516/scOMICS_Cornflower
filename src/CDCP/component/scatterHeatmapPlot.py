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


    def drawScatterHeatmap(self, cluster_class, fieldName):
        """"""

        self.FIGURE = go.Figure()

        tip1 = ''
        tip2 = ''

        if cluster_class == 'Cell Type':
            tip1 = self.METADATA.DATATABLE[f[fieldName] == 0, 'TYPE'].to_list()[0]
            tip2 = self.METADATA.DATATABLE[f[fieldName] > 0, 'TYPE'].to_list()[0]

        if cluster_class == 'Tissue':
            tip1 = self.METADATA.DATATABLE[f[fieldName] == 0, 'SOURCE'].to_list()[0]
            tip2 = self.METADATA.DATATABLE[f[fieldName] > 0, 'SOURCE'].to_list()[0]

        X1 = self.METADATA.DATATABLE[f[fieldName] == 0, 'UMAP1'].to_list()[0]
        Y1 = self.METADATA.DATATABLE[f[fieldName] == 0, 'UMAP2'].to_list()[0]

        X2 = self.METADATA.DATATABLE[f[fieldName] > 0, 'UMAP1'].to_list()[0]
        Y2 = self.METADATA.DATATABLE[f[fieldName] > 0, 'UMAP2'].to_list()[0]

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
                hovertext=tip1,

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
                    color=self.METADATA.DATATABLE[f[fieldName] > 0, fieldName].to_list()[0],
                    colorscale=['darkblue', 'yellow', 'red'],
                    showscale=True

                ),
                
                hoverinfo='text',
                hovertext=tip2,

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