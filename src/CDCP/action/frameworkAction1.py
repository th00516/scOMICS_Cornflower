#!/usr/bin/env python3




from dash.dependencies import Input, Output




class WebFrameworkAction():
    """"""

    def __init__(self, frameworkObj):
        """"""

        self.FRAMEWORK = frameworkObj


    def activate(self, metadataObj, plotDict):
        """"""

        @self.FRAMEWORK.app.callback(
            Output('geneList', 'id'), 
            [Input('geneListRegion', 'children')])
        def loading_geneList(DUMP):
            return 'geneList'


        @self.FRAMEWORK.app.callback(
            Output('mainPlot', 'id'), 
            [Input('mainPlotRegion', 'children')])
        def loading_mainPlot(DUMP):
            return 'mainPlot'


        @self.FRAMEWORK.app.callback(
            Output('supplementaryPlot1', 'id'), 
            [Input('supplementaryPlotRegion', 'children')])
        def loading_supplementaryPlot1(DUMP):
            return 'supplementaryPlot1'




        @self.FRAMEWORK.app.callback(
            Output('mainPlot', 'figure'), 
            [Input('selectDataSet', 'value'), Input('selectClusterMode', 'value')])
        def update_mainPlot(value1, value2):
            if value1 == 'All':
                if value2 == 'CT':
                    return plotDict['celltype']

                if value2 == 'SO':
                    return plotDict['source']

            else:
                return plotDict['celltype']


        @self.FRAMEWORK.app.callback(
            Output('supplementaryPlot1', 'figure'), 
            [Input('selectDataSet', 'value'), Input('selectClusterMode', 'value')])
        def update_supplementaryPlot1(value1, value2):
            if value1 == 'All':
                if value2 == 'CT':
                    return plotDict['num_celltype']

                if value2 == 'SO':
                    return plotDict['num_source']

            else:
                return plotDict['num_celltype']




        @self.FRAMEWORK.app.callback(   
            Output('selectClusterMode', 'disabled'), 
            [Input('selectDataSet', 'value')])
        def disable_selectClusterMode(value):
            if value != 'All':
                return 'CT'




        loading_geneList(None)
        loading_mainPlot(None)
        loading_supplementaryPlot1(None)

        update_mainPlot(None, None)
        update_supplementaryPlot1(None, None)

        disable_selectClusterMode(None)