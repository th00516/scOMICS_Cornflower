#!/usr/bin/env python3




from CDCP.model import prepareTsv

from CDCP.component import scatterPlot
from CDCP.component import barPlot_cellNumber

from CDCP.framework import frameworkDeploy, frameworkBuilding1

from CDCP.action import frameworkAction1




if __name__ == '__main__':

    ## 导入并解析数据 ##
    P = {}
    D = {}

    for dataset in ['All', 'Aorta', 'Kidney', 'Liver', 'Lung', 'Neocortex', 'PBMC', 'Pancreas', 'Parotid', 'Thyroid']:

        P.update({dataset:{}})
        D.update({dataset:{}})

        D[dataset] = prepareTsv.Metadata()
        D[dataset].formatData('data/' + dataset)
    
        ## 预置的Plots ##
        PL = scatterPlot.Illustration(D[dataset])
        
        PL.drawScatter('Cell Type')
        P[dataset].update({'celltype': PL.FIGURE})

        PL.drawScatter('Source')
        P[dataset].update({'source': PL.FIGURE})

        PL = barPlot_cellNumber.Illustration(D[dataset])

        PL.drawBar('Cell Type')
        P[dataset].update({'num_celltype': PL.FIGURE})

        PL.drawBar('Source')
        P[dataset].update({'num_source': PL.FIGURE})




    ## 启动服务器，构建WebApp ##
    APP = frameworkDeploy.WebCDCP(None, None)

    BF1 = frameworkBuilding1.WebFramework(APP)
    BF1.build()

    ABF1 = frameworkAction1.WebFrameworkAction(APP)
    ABF1.activate(D, P)

    APP.deploy(None)