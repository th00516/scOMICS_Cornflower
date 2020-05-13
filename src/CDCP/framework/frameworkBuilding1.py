#!/usr/bin/env python3


"""

    Author: Hao Yu (yuhao@genomics.cn)
    Date:   2020-04-24
    
"""




import dash_table as dt
import dash_html_components as html
import dash_core_components as dcc

from . import frameworkDeploy




class WebFramework():
    """"""

    def __init__(self, frameworkObj, configObj):
        """"""

        self.FRAMEWORK = frameworkObj
        self.CONFIG = configObj


    def build(self):
        """"""

        self.FRAMEWORK.app.layout = html.Div(
            html.Div(
                [
                    html.Img(
                        src=self.FRAMEWORK.app.get_asset_url('Logo.jpg'),

                        id='LOGO',

                        style=dict(

                            border='1px solid #D3D3D3',
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
                                            html.Div('Select a Tissue', style=dict(padding=10)),

                                            dcc.Dropdown(
                                                options=self.CONFIG.CONF['options'],
                                                value=self.CONFIG.CONF['options'][0]['value'],

                                                id='selectDataSet',

                                                clearable=False,
                                                searchable=False
                                            )
                                        ],

                                        id='selectDataSetRegion',

                                        style=dict(

                                            border='1px solid #D3D3D3',
                                            margin=5,
                                            padding=10,

                                            width=300

                                        )
                                    ),

                                    html.Div(
                                        [
                                            html.Div('Color mode', style=dict(padding=10)),
                                            
                                            dcc.Dropdown(
                                                options=[

                                                    {'label': 'Coloring by Cell Type', 'value': 'CT'},
                                                    {'label': 'Coloring by Tissue', 'value': 'SO'},
                                                    
                                                ],
                                                value='CT',

                                                id='selectColorMode',

                                                clearable=False,
                                                searchable=False
                                            )
                                        ],

                                        id='selectColorModeRegion',

                                        style=dict(

                                            border='1px solid #D3D3D3',
                                            margin=5,
                                            padding=10,

                                            width=300

                                        )
                                    ),
                                    
                                    html.Div(
                                        [
                                            html.Div('Analysis of Expression', style=dict(padding=10)),

                                            html.Div(
                                                [
                                                    html.Div('Primary Gene List', style=dict(padding=10)),

                                                    dcc.Dropdown(
                                                        id='primaryGeneList',

                                                        placeholder="Search a Primary Gene",

                                                        style=dict(

                                                            zIndex=2

                                                        )

                                                    )
                                                ],

                                                style=dict(

                                                    border='1px solid #D3D3D3',
                                                    margin=5,
                                                    padding=10

                                                )
                                            ),

                                            html.Div(
                                                [
                                                    html.Div('Supplementary Gene List', style=dict(padding=10)),

                                                    html.Button(
                                                        id='analysisButton',

                                                        n_clicks=0,

                                                        style=dict(

                                                            border='1px solid #D3D3D3',
                                                            margin=10,
                                                            padding=5,

                                                            width=250,
                                                            height=30

                                                        )
                                                    ),

                                                    dcc.Dropdown(
                                                        id='supplementaryGeneList',

                                                        multi=True,

                                                        placeholder="Search Supplementary Genes",

                                                        style=dict(

                                                            height=95

                                                        )
                                                    )
                                                ],

                                                style=dict(

                                                    border='1px solid #D3D3D3',
                                                    margin=5,
                                                    padding=10,

                                                    height=185

                                                )
                                            )
                                        ],

                                        id='geneListRegion',

                                        style=dict(

                                            border='1px solid #D3D3D3',
                                            margin=5,
                                            padding=10,

                                            width=300,
                                            height=350

                                        )
                                    )
                                ],

                                id='toolbox',

                                style=dict(

                                    display='flex',
                                    flexWrap='nowrap',
                                    flexDirection='column',
                                    justifyContent='flex-start',

                                    margin=5,

                                    width=300

                                )
                            ),

                            html.Div(
                                dcc.Loading(
                                    dcc.Graph(
                                        id='mainPlot',

                                        style=dict(

                                            height=600

                                        )
                                    ),

                                    type='circle'
                                ),

                                id='mainPlotRegion',

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

                            border='1px solid #D3D3D3',
                            margin=5,

                            width=1100,

                            zIndex=1

                        )
                    ),

                    html.Div(
                        [
                            html.Div(
                                dcc.Loading(
                                    dcc.Graph(                                            
                                        id='supplementaryPlot1',

                                        style=dict(

                                            width=1100,
                                            height=600

                                        )
                                    ),

                                    type='circle'
                                ),

                                id='supplementaryPlotRegion'
                            )
                        ],

                        id='L2',

                        style=dict(

                            display='flex',
                            flexWrap='nowrap',
                            flexDirection='row',
                            justifyContent='space-around',

                            border='1px solid #D3D3D3',
                            margin=5,

                            width=1100,
                            height=600

                        )
                    ),

                    html.Div(
                        [

                            html.H5(id='time')

                        ],

                        id='BOTTOM',

                        style=dict(

                            display='flex',
                            flexWrap='nowrap',
                            flexDirection='row',
                            justifyContent='center',

                            margin=5,

                            width=1100,
                            height=50

                        )
                    )
                ],

                id='MAIN',

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