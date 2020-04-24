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
            return 'Copyright for CDCP group of BGI in ' + time.strftime("%Y", time.localtime())




        @self.FRAMEWORK.app.callback(
            Output('geneList', 'id'), 
            [Input('geneList', 'data')])
        def loading_geneList(DUMP):
            return 'geneList'

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
            Output('geneList', 'data'), 
            [Input('selectDataSet', 'value')])
        def update_geneList(value):
            
            if value is None:
                value = self.CONFIG.CONF['data_set'][0]

            return [
                {'Pos %': '%0.2f' % metadataPool[value].FEATURE['posExpRate'][_], 'Gene List': _} 
                for _ in metadataPool[value].FEATURE['geneList']
            ]




        ## 更新Plots ##
        @self.FRAMEWORK.app.callback(
            Output('mainPlot', 'figure'), 
            [Input('selectDataSet', 'value'), 
             Input('selectClusterMode', 'value'),
             Input('co-expButton', 'n_clicks')],
            [State('geneList', 'selected_rows')])
        def update_mainPlot(value1, value2, DUMP, value3):
            
            if value1 is None:
                value1 = self.CONFIG.CONF['data_set'][0]

            PS = basicComparison.Parser(metadataPool[value1])

            if value3 is None or value3 == []:

                if value2 == 'CT':
                    return plotPool[value1]['celltype']

                if value2 == 'SO':
                    return plotPool[value1]['source']

            else:
                
                gene_list = [metadataPool[value1].FEATURE['geneList'][_] for _ in value3]

                if len(value3) == 1:

                    PL = scatterHeatmapPlot.Illustration(metadataPool[value1])
                    PL.drawScatterHeatmap(gene_list[0])

                    return PL.FIGURE

                if 4 >= len(value3) > 1:

                    comp_list = [gene_list[0]]

                    for i in range(1, len(gene_list)):
                        PS.genePairCoExp(gene_list[0], gene_list[i])
                        comp_list.append(gene_list[0] + '/' + gene_list[i])

                    PL = scatterHeatmapMultiPlot.Illustration(metadataPool[value1])
                    PL.drawMultiScatterHeatmap(comp_list)

                    return PL.FIGURE

                if len(value3) > 4:

                    PS.multiGenesExpCor(gene_list)

                    PL = heatmapPlot_expCorrelation.Illustration(metadataPool[value1])
                    PL.drawHeatmap(gene_list)

                    return PL.FIGURE


        @self.FRAMEWORK.app.callback(
            Output('supplementaryPlot1', 'figure'), 
            [Input('selectDataSet', 'value'), 
             Input('selectClusterMode', 'value'),
             Input('co-expButton', 'n_clicks')],
            [State('geneList', 'selected_rows')])
        def update_supplementaryPlot1(value1, value2, DUMP, value3):
            
            if value3 is None or value3 == []:

                if value2 == 'CT':
                    return plotPool[value1]['num_celltype']

                if value2 == 'SO':
                    return plotPool[value1]['num_source']

            else:

                if len(value3) == 1:

                    gene_list = metadataPool[value1].FEATURE['geneList'][value3[0]]

                    PL = violinPlot.Illustration(metadataPool[value1])
                    PL.drawViolin(gene_list)

                    return PL.FIGURE

                else:

                    gene_list1 = metadataPool[value1].FEATURE['geneList'][value3[0]]
                    gene_list2 = metadataPool[value1].FEATURE['geneList'][value3[1]]

                    PL = violinSplitPlot.Illustration(metadataPool[value1])
                    PL.drawSplitViolin(gene_list1, gene_list2)

                    return PL.FIGURE




        
        
        ## 其他 ##
        @self.FRAMEWORK.app.callback(   
            Output('selectDataSet', 'disabled'), 
            [Input('geneList', 'selected_rows')])
        def disable_selectDataSet(value):

            if value is not None and len(value) > 0:
                return True


        @self.FRAMEWORK.app.callback(   
            Output('selectClusterMode', 'disabled'), 
            [Input('geneList', 'selected_rows')])
        def disable_selectClusterMode(value):

            if value is not None and len(value) > 0:
                return True


        @self.FRAMEWORK.app.callback(   
            Output('co-expButton', 'disabled'), 
            [Input('geneList', 'selected_rows')])
        def disable_coExpButton(value):

            if value is None or value == []:
                return True


        @self.FRAMEWORK.app.callback(   
            Output('cleanButton', 'disabled'), 
            [Input('geneList', 'selected_rows')])
        def disable_cleanButton(value):

            if value is None or value == []:
                return True


        @self.FRAMEWORK.app.callback(   
            Output('geneList', 'selected_rows'), 
            [Input('cleanButton', 'n_clicks')])
        def clean_selectGene(DUMP):
            return []




        #### 调用反馈函数并赋予None参数，用于满足语法检查需求 ####
        loading_framework(None)

        loading_geneList(None)
        loading_mainPlot(None)
        loading_supplementaryPlot1(None)

        update_geneList(None)
        update_mainPlot(None, None, None, None)
        update_supplementaryPlot1(None, None, None, None)

        disable_selectDataSet(None)
        disable_selectClusterMode(None)

        disable_coExpButton(None)
        disable_cleanButton(None)

        clean_selectGene(None)