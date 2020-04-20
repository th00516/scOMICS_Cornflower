#!/usr/bin/env python3




import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt

from . import frameworkDeploy

from dash.dependencies import Input, Output
import time


class WebFramework():
    """"""

    def __init__(self, frameworkObj):
        """"""

        self.FRAMEWORK = frameworkObj

    def build(self, metadataObj, plotObjs):
        """"""

        self.FRAMEWORK.app.layout = html.Div(
            html.Div(
                [
                    html.Img(
                        src='',

                        id='logo',

                        style=dict(

                            border='1px solid black',
                            margin=5,

                            width=1100,
                            height=80

                        )
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.P(
                                                'control panel'
                                            )
                                        ],

                                        id='controlPanel',
                                        
                                        style=dict(

                                            border='1px solid black',
                                            margin=5,
                                            padding=10

                                        )
                                    ),
                                    
                                    dt.DataTable(
                                        data=[{'Gene List': g} for g in metadataObj.DATATABLE.keys()[6:6 + metadataObj.FEATURE['numGene']]],
                                        columns=[{'name': 'Gene List', 'id': 'Gene List'}],

                                        id = 'geneList',

                                        filter_action='native',

                                        row_selectable=True,

                                        fixed_rows={'headers': True},

                                        style_table=dict(

                                            margin=5,

                                            width=190,
                                            height=200

                                        ),

                                        style_header=dict(
                                            
                                            fontFamily='Arial',
                                            fontStyle='normal',
                                            fontWeight='bold',
                                            fontSize=18

                                        ),

                                        style_cell=dict(

                                            fontFamily='Arial',
                                            fontStyle='italic',

                                            cursor='default'

                                        )

                                    )
                                ],

                                id='toolbox',

                                style=dict(

                                    display='flex',
                                    flexWrap='nowrap',
                                    flexDirection='column',
                                    justifyContent='flex-start',

                                    # border='1px solid black',
                                    margin=5,

                                    width=200

                                )
                            ),

                            html.Div(
                                dcc.Loading(
                                    dcc.Graph(
                                        figure=plotObjs[0],

                                        id='mainPlot',

                                        style=dict(

                                            height=600

                                        )
                                    ),

                                    type='circle'
                                ),

                                style=dict(

                                    display='flex',
                                    flexWrap='nowrap',
                                    flexDirection='row',
                                    justifyContent='space-around',

                                    width=900,
                                    height=600

                                )
                            )
                        ],

                        id='L1',

                        style=dict(

                            display='flex',
                            flexWrap='nowrap',
                            flexDirection='row',
                            justifyContent='space-around',

                            border='1px solid black',
                            margin=5,

                            width=1100

                        )
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    # dcc.Loading(
                                    #     dcc.Graph(
                                    #         figure=plotObjs[1],

                                    #         id='supplementaryPlot1'
                                    #     )
                                    # ),

                                    # dcc.Loading(
                                    #     dcc.Graph(
                                    #         figure=plotObjs[2],

                                    #         id='supplementaryPlot2'
                                    #     )
                                    # )
                                ],

                                style=dict(

                                    display='flex',
                                    flexWrap='nowrap',
                                    flexDirection='column',
                                    justifyContent='space-around',
                                    alignContent='space-around',

                                    border='1px solid black'

                                )
                            )
                        ],

                        id='L2',

                        style=dict(

                            display='flex',
                            flexWrap='nowrap',
                            flexDirection='row',
                            justifyContent='space-around',

                            border='1px solid black',
                            margin=5,

                            width=1100

                        )
                    )
                ],

                id='main',

                style=dict(

                    display='flex',
                    flexDirection='column',
                    justifyContent='flex-start',

                    fontFamily='Arial'

                )
            ),

            style=dict(

                display='flex',
                flexDirection='row',
                justifyContent='center',

            )
        )




        @self.FRAMEWORK.app.callback(Output("mainPlot", "id"), [Input("L1", "children")])
        def loading_mainPlot(DUMP):
            time.sleep(2)
            return 'mainPlot'

        # @self.FRAMEWORK.app.callback(Output("supplementaryPlot1", "id"), [Input("L2", "children")])
        # def loading_supplementaryPlot1(DUMP):
        #     time.sleep(2)
        #     return 'supplementaryPlot1'

        # @self.FRAMEWORK.app.callback(Output("supplementaryPlot2", "id"), [Input("L2", "children")])
        # def loading_supplementaryPlot2(DUMP):
        #     time.sleep(2)
        #     return 'supplementaryPlot2'