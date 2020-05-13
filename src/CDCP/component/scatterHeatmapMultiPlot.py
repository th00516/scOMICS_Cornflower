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


    def drawMultiScatterHeatmap(self, cluster_class, fieldNames):
        """"""

        title = [
            
            fieldNames[1] + ' (Do-pos.)', 
            fieldNames[0] + ' (Exp.)'

        ]

        if len(fieldNames) > 2:
            for i in range(2, len(fieldNames)):
                title.append(fieldNames[i] + ' (Do-pos.)')


        self.FIGURE = make_subplots(2, 2, specs=[[{}, {}], [{}, {}]], subplot_titles=title)

        tip1 = ''
        tip2 = ''

        if cluster_class == 'Cell Type':
            tip1 = self.METADATA.DATATABLE[f[fieldNames[0]] == 0, 'TYPE'].to_list()[0]
            tip2 = self.METADATA.DATATABLE[f[fieldNames[0]] > 0, 'TYPE'].to_list()[0]

        if cluster_class == 'Tissue':
            tip1 = self.METADATA.DATATABLE[f[fieldNames[0]] == 0, 'SOURCE'].to_list()[0]
            tip2 = self.METADATA.DATATABLE[f[fieldNames[0]] > 0, 'SOURCE'].to_list()[0]


        ## 表达量图 ##
        X1 = self.METADATA.DATATABLE[f[fieldNames[0]] == 0, 'UMAP1'].to_list()[0]
        Y1 = self.METADATA.DATATABLE[f[fieldNames[0]] == 0, 'UMAP2'].to_list()[0]

        X2 = self.METADATA.DATATABLE[f[fieldNames[0]] > 0, 'UMAP1'].to_list()[0]
        Y2 = self.METADATA.DATATABLE[f[fieldNames[0]] > 0, 'UMAP2'].to_list()[0]


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
            ),

            1, 2
        )

        self.FIGURE.add_trace(
            go.Scattergl(
                name='Exp.',

                x=X2,
                y=Y2,

                mode='markers',
                marker=dict(
                
                    size=2,
                    color=self.METADATA.DATATABLE[f[fieldNames[0]] > 0, fieldNames[0]].to_list()[0],
                    colorscale=['darkblue', 'yellow', 'red'],
                    showscale=True

                ),
                
                hoverinfo='text',
                hovertext=tip2,

                showlegend=False
            ),

            1, 2
        )


        ## 共表达图 1 ##
        tip1 = ''
        tip2 = ''

        if cluster_class == 'Cell Type':
            tip1 = self.METADATA.DATATABLE[f[fieldNames[1]] == 0, 'TYPE'].to_list()[0]
            tip2 = self.METADATA.DATATABLE[f[fieldNames[1]] == 1, 'TYPE'].to_list()[0]

        if cluster_class == 'Tissue':
            tip1 = self.METADATA.DATATABLE[f[fieldNames[1]] == 0, 'SOURCE'].to_list()[0]
            tip2 = self.METADATA.DATATABLE[f[fieldNames[1]] == 1, 'SOURCE'].to_list()[0]

        X1 = self.METADATA.DATATABLE[f[fieldNames[1]] == 0, 'UMAP1'].to_list()[0]
        Y1 = self.METADATA.DATATABLE[f[fieldNames[1]] == 0, 'UMAP2'].to_list()[0]

        X2 = self.METADATA.DATATABLE[f[fieldNames[1]] == 1, 'UMAP1'].to_list()[0]
        Y2 = self.METADATA.DATATABLE[f[fieldNames[1]] == 1, 'UMAP2'].to_list()[0]

        self.FIGURE.add_trace(
            go.Scattergl(
                name=fieldNames[1],

                x=X1,
                y=Y1,

                mode='markers',
                marker=dict(
                
                    size=2,
                    color='lightgrey',
                    showscale=False

                ),

                hoverinfo='text',
                hovertext=tip1,

                showlegend=False
            ),

            1, 1
        )

        self.FIGURE.add_trace(
            go.Scattergl(
                name=fieldNames[1],

                x=X2,
                y=Y2,

                mode='markers',
                marker=dict(
                
                    size=4,
                    color=self.METADATA.DATATABLE[f[fieldNames[1]] == 1, fieldNames[1]].to_list()[0],
                    colorscale=['lightgrey', 'green'],
                    showscale=False

                ),

                hoverinfo='text',
                hovertext=tip2,

                showlegend=False
            ),

            1, 1
        )

        ## 共表达图 2、3 ##        
        if len(fieldNames) > 2:

            for i in range(2, len(fieldNames)):

                tip1 = ''
                tip2 = ''

                if cluster_class == 'Cell Type':
                    tip1 = self.METADATA.DATATABLE[f[fieldNames[i]] == 0, 'TYPE'].to_list()[0]
                    tip2 = self.METADATA.DATATABLE[f[fieldNames[i]] == 1, 'TYPE'].to_list()[0]

                if cluster_class == 'Tissue':
                    tip1 = self.METADATA.DATATABLE[f[fieldNames[i]] == 0, 'SOURCE'].to_list()[0]
                    tip2 = self.METADATA.DATATABLE[f[fieldNames[i]] == 1, 'SOURCE'].to_list()[0]

                X1 = self.METADATA.DATATABLE[f[fieldNames[i]] == 0, 'UMAP1'].to_list()[0]
                Y1 = self.METADATA.DATATABLE[f[fieldNames[i]] == 0, 'UMAP2'].to_list()[0]

                X2 = self.METADATA.DATATABLE[f[fieldNames[i]] == 1, 'UMAP1'].to_list()[0]
                Y2 = self.METADATA.DATATABLE[f[fieldNames[i]] == 1, 'UMAP2'].to_list()[0]

                self.FIGURE.add_trace(
                    go.Scattergl(
                        name=fieldNames[i],

                        x=X1,
                        y=Y1,

                        mode='markers',
                        marker=dict(
                        
                            size=2,
                            color='lightgrey',
                            showscale=False

                        ),

                        hoverinfo='text',
                        hovertext=tip1,

                        showlegend=False
                    ),

                    2, i - 1
                )

                self.FIGURE.add_trace(
                    go.Scattergl(
                        name=fieldNames[i],

                        x=X2,
                        y=Y2,

                        mode='markers',
                        marker=dict(
                        
                            size=4,
                            color=self.METADATA.DATATABLE[f[fieldNames[i]] == 1, fieldNames[i]].to_list()[0],
                            colorscale=['lightgrey', 'green'],
                            showscale=False

                        ),

                        hoverinfo='text',
                        hovertext=tip2,

                        showlegend=False
                    ),

                    2, i - 1
                )


        self.FIGURE.update_xaxes(matches='x')
        self.FIGURE.update_yaxes(matches='y')

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                x=0.5,

                text='Exp. of <i>' + fieldNames[0] + '</i> & Double Positive with Others', 
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE

                )

            )
            
        )