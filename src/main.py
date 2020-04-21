#!/usr/bin/env python3




from CDCP.model import prepareTsv

from CDCP.component import scatterPlot
from CDCP.component import barPlot_cellNumber

from CDCP.framework import frameworkDeploy, frameworkBuilding1

from CDCP.action import frameworkAction1




if __name__ == '__main__':

    ## 导入并解析数据 ##
    DT = prepareTsv.Metadata()
    DT.formatData('data/All')
    



    ## 预置的Plots ##
    P = {}

    PL = scatterPlot.Illustration(DT)
    
    PL.drawScatter('Cell Type')
    P.update({'celltype': PL.FIGURE})

    PL.drawScatter('Source')
    P.update({'source': PL.FIGURE})

    PL = barPlot_cellNumber.Illustration(DT)

    PL.drawBar('Cell Type')
    P.update({'num_celltype': PL.FIGURE})

    PL.drawBar('Source')
    P.update({'num_source': PL.FIGURE})




    ## 启动服务器，构建WebApp ##
    APP = frameworkDeploy.WebCDCP(None, None)

    BF1 = frameworkBuilding1.WebFramework(APP)
    BF1.build(DT)

    ABF1 = frameworkAction1.WebFrameworkAction(APP)
    ABF1.activate(DT, P)

    APP.deploy(None)