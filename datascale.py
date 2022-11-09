import sys
import warnings
import matplotlib.pyplot as plt
import numpy as np

def plotdatasize(axobj=None,mult=1,axis='y',plottype='line'):
    """  
    Returns a value for linewidth/markersize or size that is scaled to plotted data units 
        Note that this function must be used after any figure/axis alterations (axes limits, aspect ratio, etc.)
        Note that scaling is to data units and not axis size - if a y axis ranges from 0 to 3 and mult=1, the produced line will be 1 unit thick, or 1/3 the height of the y axis

    Inputs (Required):
        none

    Inputs (Optional):
        axobj - axes object to scale to, default=plt.gca() (current pyplot axes object)
        mult - A float multiplier for output, default=1
            e.g. to get a linewidth 1/10 the scale of the plotted units, mult=0.1
        axis ('x','y','xy') - axis to use for data scaling, default='y'
            Note that if x and y axes do not have an equal aspect ratio (e.g. axobj.set_aspect('equal')), 'xy' will attempt to average the scaling retrieved by 'x' and 'y', and will produce a warning if unequal
        plottype ('line'/'scatter') - plot type for use with output, default='line'
            Note that for lines and line markers (pyplot.plot) linewidth and markersize scale linearly, while for s (pyplot.scatter), markers scale with the square of size
            Note that using output for s will be correct in a scatter only if linewidth=0 (marker edge)

    Outputs:
        plotdatasize - linewidth/markersize/s to be used as a direct input to pyplot.plot, pyplot.scatter, etc.        
    """
    if axobj is None:
        axobj=plt.gca()
    fig=axobj.get_figure()
    pointwidth=72*fig.bbox_inches.width*axobj.get_position().width
    pointheight=72*fig.bbox_inches.height*axobj.get_position().height
    widthrange=np.diff(axobj.get_xlim())[0]
    heightrange=np.diff(axobj.get_ylim())[0]
    plotdatawidth=pointwidth/widthrange
    plotdataheight=pointheight/heightrange
    if axis=='y':
        plotdatasize=plotdataheight
    elif axis=='x':
        plotdatasize=plotdatawidth
    elif axis=='xy':
        if plotdataheight!=plotdatawidth:
            if not np.allclose(plotdataheight,plotdatawidth):
                warnings.warn('WARNING - x and y axes not scaled equally, output will not be precise')
        plotdatasize=(plotdataheight+plotdatawidth)/2
    else:
        sys.exit('ERROR - \''+axis+'\' is invalid input, select \'x\',\'y\', or \'xy\'')
    if plottype=='line':
        return mult*plotdatasize
    elif plottype=='scatter':
        return (mult*plotdatasize)**2
    else:
        sys.exit('ERROR - \''+plottype+'\' is invalid input, select \'line\' or \'scatter\'')

def plotdatadpi(axobj=None,mult=1,axis='y',rangelim='auto'):
    """
    Returns a value for output dpi that is scaled to plotted data units
        Note that this function must be used after any figure/axis alterations (axes limits, aspect ratio, etc.)
        Note that scaling is to data units and not axis size - if a y axis ranges from 0 to 3 and mult=10, the produced plot will have 10 pixels per unit, or 30 pixels along the y axis

    Inputs (Required):
        none

    Inputs (Optional):
        axobj - axes object to scale to, default=plt.gca() (current pyplot axes object)
        mult - A float multiplier for output, default=1
            e.g. to get a linewidth 1/10 the scale of the plotted units, mult=0.1
        axis ('x','y','xy') - axis to use for data scaling, default='y'
            Note that if x and y axes do not have an equal aspect ratio (e.g. axobj.set_aspect('equal')), 'xy' will attempt to average the scaling retrieved by 'x' and 'y', and will produce a warning if unequal
        rangelim ('auto','warn') - select behaviour for when output dpi is below 150 or above 1000, default='auto'
            'auto' will clip output to be 150 if lower or 1000 if highter
            'warn' will output the calculated value, but will also produce a warning

    Outputs:
        plotdatadpi - dpi value to be used as a direct input when saving figures
            e.g. fig.savefig(...,dpi=plotdatadpi,...)
    """
    if axobj is None:
        axobj=plt.gca()
    fig=axobj.get_figure()
    pointwidth=72*fig.bbox_inches.width*axobj.get_position().width
    pointheight=72*fig.bbox_inches.height*axobj.get_position().height
    widthrange=np.diff(axobj.get_xlim())[0]
    heightrange=np.diff(axobj.get_ylim())[0]
    plotdatawidth=pointwidth/widthrange
    plotdataheight=pointheight/heightrange
    if axis=='y':
        plotdatadpi=plotdataheight
    elif axis=='x':
        plotdatadpi=plotdatawidth
    elif axis=='xy':
        if plotdataheight!=plotdatawidth:
            if not np.allclose(plotdataheight,plotdatawidth):
                warnings.warn('WARNING - x and y axes not scaled equally, output will not be precise')
        plotdatadpi=(plotdataheight+plotdatawidth)/2
    else:
        sys.exit('ERROR - \''+axis+'\' is invalid input, select \'x\',\'y\', or \'xy\'')
    plotdatadpi*=mult*36*72/plotdatadpi
    if rangelim=='auto':
        if plotdatadpi<150:
            plotdatadpi=150
        if plotdatadpi>1000:
            plotdatadpi=1000
    elif rangelim=='warn':
        if plotdatadpi<150:
            warnings.warn('WARNING - output dpi is less than 150, figure will be very low resolution')
        if plotdatadpi>1000:
            warnings.warn('WARNING - output dpi is more than 1000, figure will be very large')
    else:
        sys.exit('ERROR - \''+rangelim+'\' is invalid input, select \'auto\' or \'warn\'')
    return plotdatadpi
