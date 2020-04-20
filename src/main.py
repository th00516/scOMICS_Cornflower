#!/usr/bin/env python3




from CDCP.model import prepareTsv

from CDCP.component import scatterPlot
from CDCP.component import scatterVariablePlot
from CDCP.component import scatterHeatmapPlot
from CDCP.component import scatterMultiPlot
from CDCP.component import scatterHeatmapMultiPlot
from CDCP.component import barPlot_cellNumber
from CDCP.component import violinPlot

from CDCP.framework import frameworkDeploy, frameworkBuilding1

from CDCP.action import frameworkAction1




if __name__ == '__main__':

    DT = prepareTsv.Metadata()
    DT.formatData('data')
    

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


    # PL = scatterVariablePlot.Illustration(DT)
    
    # PL.drawVariableScatter()
    # P.append(PL.FIGURE)

    # PL = scatterHeatmapPlot.Illustration(DT)

    # PL.drawScatterHeatmap('PGBD2')
    # P.append(PL.FIGURE)


    # PL = scatterMultiPlot.Illustration(DT)

    # PL.drawMultiScatter(['Liver', 'Kidney'])
    # P.append(PL.FIGURE)


    # PL = scatterHeatmapMultiPlot.Illustration(DT)

    # PL.drawMultiScatterHeatmap(['PGBD2', 'PGBD2/ZNF692', 'PGBD2/ZNF672'])
    # P.append(PL.FIGURE)

    # PL = violinPlot.Illustration(DT)

    # PL.drawViolin('PGBD2')
    # P.update(PL.FIGURE)




    APP = frameworkDeploy.WebCDCP(None, None)

    BF1 = frameworkBuilding1.WebFramework(APP)
    BF1.build(DT)

    ABF1 = frameworkAction1.WebFrameworkAction(APP)
    ABF1.activate(DT, P)

    APP.deploy(None)