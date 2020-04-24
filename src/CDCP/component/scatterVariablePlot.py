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


    def drawVariableScatter(self):
        """"""

        fig1 = []

        for trace in self.METADATA.FEATURE['typeSet']:

            X = self.METADATA.DATATABLE[f.TYPE == trace, 'UMAP1'].to_list()[0]
            Y = self.METADATA.DATATABLE[f.TYPE == trace, 'UMAP2'].to_list()[0]

            fig1.append(
                go.Scattergl(
                    name=trace,

                    x=X,
                    y=Y,

                    mode='markers',
                    marker=dict(
                    
                        size=2,
                        color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],

                    ),

                    hoverinfo='text',
                    hovertext=trace
                )
            )

        fig2 = []

        for trace in self.METADATA.FEATURE['sourceSet']:

            X = self.METADATA.DATATABLE[f.SOURCE == trace, 'UMAP1'].to_list()[0]
            Y = self.METADATA.DATATABLE[f.SOURCE == trace, 'UMAP2'].to_list()[0]

            fig2.append(
                go.Scattergl(
                    name=trace,

                    x=X,
                    y=Y,

                    mode='markers',
                    marker=dict(
                    
                        size=2,
                        color=self.METADATA.COLOR[f.GROUP == trace, 'COLOR'][0, 0],

                    ),

                    hoverinfo='text',
                    hovertext=trace
                )
            )

        self.FIGURE=go.Figure(data=fig1+fig2)

        self.FIGURE.update_layout(

            template='plotly_white',

            title=dict(

                text='Cluster by Cell Type',
                font=dict(

                    family='Arial', 
                    size=self.TITLE_SIZE

                )

            ),

            legend=dict(

                itemsizing='constant'

            ),

        )

        self.FIGURE.update_layout(

            updatemenus=[

                dict(

                    buttons=list([
                        
                        dict(

                            args=[
                                {
                                
                                    'visible': [True] * len(self.METADATA.FEATURE['typeSet']) + \
                                              [False] * len(self.METADATA.FEATURE['sourceSet'])

                                },

                                {

                                    'title.text': 'Cluster by Cell Type'

                                }
                            ],

                            label='by Cell Type',
                            method='update'

                        ),

                        dict(

                            args=[
                                {
                                
                                    'visible': [False] * len(self.METADATA.FEATURE['typeSet']) + \
                                                [True] * len(self.METADATA.FEATURE['sourceSet'])

                                },

                                {

                                    'title.text': 'Cluster by Source'
                                    
                                }
                            ],

                            label='by Source',
                            method='update'

                        )

                    ]),

                    type = 'buttons',
                    direction = 'right',
                    
                    x=1.0,
                    y=1.2,

                    pad=dict(

                        r=5,
                        t=5

                    ),

                    showactive=True

                )

            ]

        )