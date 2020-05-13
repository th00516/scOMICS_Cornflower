#!/usr/bin/env python3


"""

    Author: Hao Yu (yuhao@genomics.cn)
    Date:   2020-04-24
    
"""




import time

from dash.dependencies import Input, Output, State
from . import basicComparison

from CDCP.component import scatterHeatmapPlot
from CDCP.component import scatterHeatmapMultiPlot
from CDCP.component import heatmapPlot_expCorrelation

from CDCP.component import violinPlot
from CDCP.component import violinSplitPlot




class WebFrameworkAction():
    """"""

    def __init__(self, frameworkObj, configObj):
        """"""

        self.FRAMEWORK = frameworkObj
        self.CONFIG = configObj


    def activate(self, metadataPool, plotPool):
        """"""

        ## 初始化 ##
        @self.FRAMEWORK.app.callback(
            Output('time', 'children'), 
            [Input('mainPlot', 'figure')])
        def loading_framework(DUMP):
            return 'Copyright for ' + self.CONFIG.CONF['our_group'][0] + ' group of BGI in ' + \
                    time.strftime('%Y', time.localtime()) + '. Support by CDCP project of BGI.'


        @self.FRAMEWORK.app.callback(
            Output('mainPlot', 'id'), 
            [Input('mainPlot', 'figure')])
        def loading_mainPlot(DUMP):
            return 'mainPlot'


        @self.FRAMEWORK.app.callback(
            Output('supplementaryPlot1', 'id'), 
            [Input('supplementaryPlot1', 'figure')])
        def loading_supplementaryPlot1(DUMP):
            return 'supplementaryPlot1'




        ## 更新Gene List ##
        @self.FRAMEWORK.app.callback(
            Output('primaryGeneList', 'options'), 
            [Input('selectDataSet', 'value')])
        def update_primaryGeneList(value):

            if value is None:
                value = self.CONFIG.CONF['data_set'][0]

            return [{'label': _, 'value': _} for _ in metadataPool[value].FEATURE['geneList']]


        @self.FRAMEWORK.app.callback(
            Output('supplementaryGeneList', 'options'), 
            [Input('selectDataSet', 'value')])
        def update_supplementaryGeneList(value):

            if value is None:
                value = self.CONFIG.CONF['data_set'][0]

            return [{'label': _, 'value': _} for _ in metadataPool[value].FEATURE['geneList']]


        @self.FRAMEWORK.app.callback(
            Output('analysisButton', 'children'), 
            [Input('supplementaryGeneList', 'value')])
        def update_analysisButton(value):

            if value is None or len(value) == 0:
                return 'EXHIBIT ...'

            if value is not None and 4 > len(value) > 0:
                return 'EXHIBIT Double-positive'

            if value is not None and len(value) >= 4:
                return 'EXHIBIT Expression-correlation'




        ## 更新Plots ##
        @self.FRAMEWORK.app.callback(
            Output('mainPlot', 'figure'), 
            [Input('selectDataSet', 'value'), 
             Input('selectClusterMode', 'value'),
             Input('primaryGeneList', 'value'),
             Input('analysisButton', 'n_clicks')],
            [State('supplementaryGeneList', 'value')])
        def update_mainPlot(value1, value2, value3, DUMP, value4):
            
            if value1 is None:
                value1 = self.CONFIG.CONF['data_set'][0]

            if value3 is None or value3 == []:

                if value2 == 'CT':
                    return plotPool[value1]['celltype']

                if value2 == 'SO':
                    return plotPool[value1]['tissue']

            else:
                
                if value4 is None or value4 == []:

                    PL = scatterHeatmapPlot.Illustration(metadataPool[value1])
                    PL.drawScatterHeatmap(value3)

                    return PL.FIGURE

                else:
                    
                    PS = basicComparison.Parser(metadataPool[value1])
                    
                    if 4 > len(value4) > 0:

                        compListLabel = [value3]

                        for i in range(0, len(value4)):

                            PS.genePairDoPos(value3, value4[i])
                            compListLabel.append(value3 + '/' + value4[i])

                        PL = scatterHeatmapMultiPlot.Illustration(metadataPool[value1])
                        PL.drawMultiScatterHeatmap(compListLabel)

                        return PL.FIGURE

                    else:

                        geneList = [value3] + [_ for _ in value4]

                        PS.multiGenesExpCor(geneList)

                        PL = heatmapPlot_expCorrelation.Illustration(metadataPool[value1])
                        PL.drawHeatmap(geneList)

                        return PL.FIGURE


        @self.FRAMEWORK.app.callback(
            Output('supplementaryPlot1', 'figure'), 
            [Input('selectDataSet', 'value'), 
             Input('selectClusterMode', 'value'),
             Input('primaryGeneList', 'value'),
             Input('analysisButton', 'n_clicks')],
            [State('supplementaryGeneList', 'value')])
        def update_supplementaryPlot1(value1, value2, value3, DUMP, value4):

            if value1 is None:
                value1 = self.CONFIG.CONF['data_set'][0]
            
            if value3 is None or value3 == []:

                if value2 == 'CT':
                    return plotPool[value1]['num_celltype']

                if value2 == 'SO':
                    return plotPool[value1]['num_tissue']

            else:

                if value4 is None or value4 == []:

                    PL = violinPlot.Illustration(metadataPool[value1])
                    PL.drawViolin(value3)

                    return PL.FIGURE

                else:

                    PL = violinSplitPlot.Illustration(metadataPool[value1])
                    PL.drawSplitViolin(value3, value4[0])

                    return PL.FIGURE




        
        
        ## 其他 ##
        @self.FRAMEWORK.app.callback(   
            Output('selectClusterMode', 'disabled'), 
            [Input('primaryGeneList', 'value')])
        def disable_selectClusterMode(value):

            if value is not None and len(value) > 0:
                return True
        

        @self.FRAMEWORK.app.callback(   
            Output('supplementaryGeneList', 'disabled'), 
            [Input('primaryGeneList', 'value')])
        def disable_supplementaryGeneList(value):

            if value is None or len(value) == 0:
                return True

        
        @self.FRAMEWORK.app.callback(   
            Output('supplementaryGeneList', 'value'), 
            [Input('primaryGeneList', 'value')])
        def cleanUp_supplementaryGeneList(value):

            if value is None or len(value) == 0:
                return []

        
        @self.FRAMEWORK.app.callback(   
            Output('analysisButton', 'disabled'), 
            [Input('supplementaryGeneList', 'value')])
        def disable_analysisButton(value):

            if value is None or len(value) == 0:
                return True