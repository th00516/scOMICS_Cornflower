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
                        src='http://172.17.14.1/Logo.jpg',

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
                                            html.Div('Select a data set', style=dict(padding=10)),

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

                                            width=250

                                        )
                                    ),

                                    html.Div(
                                        [
                                            html.Div('Select a cluster mode', style=dict(padding=10)),
                                            
                                            dcc.Dropdown(
                                                options=[

                                                    {'label': 'by Cell Type', 'value': 'CT'},
                                                    {'label': 'by Source', 'value': 'SO'},
                                                    
                                                ],
                                                value='CT',

                                                id='selectClusterMode',

                                                clearable=False,
                                                searchable=False
                                            )
                                        ],

                                        id='selectClusterModeRegion',

                                        style=dict(

                                            border='1px solid #D3D3D3',
                                            margin=5,
                                            padding=10,

                                            width=250

                                        )
                                    ),
                                    
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Button(
                                                        'Co-Exp.',

                                                        id='co-expButton',

                                                        n_clicks=0,

                                                        style=dict(

                                                            border='1px solid #D3D3D3',
                                                            margin=5,
                                                            padding=5,

                                                            width=100,
                                                            height=30

                                                        )
                                                    ),

                                                    html.Button(
                                                        'CLEAN',

                                                        id='cleanButton',

                                                        n_clicks=0,

                                                        style=dict(

                                                            border='1px solid #D3D3D3',
                                                            margin=5,
                                                            padding=5,

                                                            width=100,
                                                            height=30

                                                        )
                                                    )
                                                ],

                                                id='controlPanelRegion',
                                                
                                                style=dict(

                                                    display='flex',
                                                    flexWrap='nowrap',
                                                    flexDirection='row',
                                                    justifyContent='space-around',

                                                    margin=5,
                                                    padding=10

                                                )
                                            ),

                                            dt.DataTable(
                                                columns=[{'name':'Pos %', 'id':'Pos %'}, {'name': 'Gene List', 'id': 'Gene List'}],

                                                id = 'geneList',

                                                filter_action='native',

                                                row_selectable='multi',

                                                fixed_rows={'headers': True},

                                                page_size=6,

                                                style_table=dict(

                                                    height=250

                                                ),

                                                style_header=dict(
                                                    
                                                    fontFamily='Arial',
                                                    fontStyle='normal',
                                                    fontWeight='bold',
                                                    fontSize=18

                                                ),

                                                style_cell=dict(

                                                    padding=5,

                                                    maxWidth=100,
                                                    minWidth=100,

                                                    fontFamily='Arial',
                                                    fontStyle='italic',

                                                    cursor='default'

                                                )
                                            )
                                        ],

                                        id='geneListRegion',

                                        style=dict(

                                            border='1px solid #D3D3D3',
                                            margin=5,
                                            padding=10,

                                            width=250,
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

                                    width=250

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

                            width=1100

                        )
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    dcc.Loading(
                                        dcc.Graph(                                            
                                            id='supplementaryPlot1',

                                            style=dict(

                                                width=1100,
                                                height=600

                                            )
                                        ),

                                        type='circle'
                                    )
                                ],

                                id='supplementaryPlotRegion',

                                style=dict(

                                    display='flex',
                                    flexWrap='nowrap',
                                    flexDirection='column',
                                    justifyContent='space-around',
                                    alignContent='space-around'

                                )
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