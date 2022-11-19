import sys
import warnings
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
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

def plotdatadpi(axobj=None,mult=1,axis='y',rangelim='warn'):
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
        rangelim ('warn','auto') - select behaviour for when output dpi is below 100 or above 1000, default='warn'
            'warn' will output the calculated value, but will also produce a warning
            'auto' will clip output to be 100 if lower or 1000 if highter

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
        dpidiv=plotdataheight
    elif axis=='x':
        dpidiv=plotdatawidth
    elif axis=='xy':
        if plotdataheight!=plotdatawidth:
            if not np.allclose(plotdataheight,plotdatawidth):
                warnings.warn('WARNING - x and y axes not scaled equally, output will not be precise')
        dpidiv=(plotdataheight+plotdatawidth)/2
    else:
        sys.exit('ERROR - \''+axis+'\' is invalid input, select \'x\',\'y\', or \'xy\'')
    plotdatadpi=mult*72/dpidiv
    if rangelim=='auto':
        if plotdatadpi<100:
            plotdatadpi=100
        if plotdatadpi>1000:
            plotdatadpi=1000
    elif rangelim=='warn':
        if plotdatadpi<100:
            warnings.warn('WARNING - output dpi is less than 100, figure will be very low resolution')
        if plotdatadpi>1000:
            warnings.warn('WARNING - output dpi is more than 1000, figure will be very large')
    else:
        sys.exit('ERROR - \''+rangelim+'\' is invalid input, select \'auto\' or \'warn\'')
    return plotdatadpi

def test():
    print('Running datascale test\nTest images will be output to current directory')
    plt.ioff()
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlim([0,5])
    ax.set_ylim([0,12])
    lwy=plotdatasize()
    lwy2=plotdatasize(mult=2)
    lwx=plotdatasize(axis='x')
    msy=plotdatasize(plottype='scatter')
    msy2=plotdatasize(plottype='scatter',mult=2)
    msx=plotdatasize(plottype='scatter',axis='x')
    ax.plot([2,4.5],[11,11],linewidth=lwy,c='C0')
    ax.plot([2,4.5],[9,9],linewidth=lwy2,c='C0')
    ax.plot([2],[7],linewidth=0,marker='o',markersize=lwy,c='C1')
    ax.plot([2],[5],linewidth=0,marker='o',markersize=lwy2,c='C1')
    ax.plot([3],[6],linewidth=0,marker='o',markersize=lwx,c='C1')
    ax.scatter([2],[3],s=msy,linewidth=0,c='C2',zorder=2)
    ax.scatter([2],[1],s=msy2,linewidth=0,c='C2',zorder=2)
    ax.scatter([3],[2],s=msx,linewidth=0,c='C2',zorder=2)
    ax.xaxis.set_major_locator(tck.MultipleLocator(0.5))
    ax.yaxis.set_major_locator(tck.MultipleLocator(1))
    ax.grid(which='both')
    fs='x-small'
    boxprops=dict(facecolor='white',alpha=1)
    ax.text(0.2,11,'linewidth of 1 y data unit',fontsize=fs,bbox=boxprops,va='center')
    ax.text(0.2,9,'linewidth of 2 y data units',fontsize=fs,bbox=boxprops,va='center')
    ax.text(0.2,7,'line marker with linewidth\nof 1 y data unit',fontsize=fs,bbox=boxprops,va='center')
    ax.text(0.2,5,'line marker with linewidth\nof 2 y data units',fontsize=fs,bbox=boxprops,va='center')
    ax.text(0.2,3,'scatter marker with size\nof 1 y data unit',fontsize=fs,bbox=boxprops,va='center')
    ax.text(0.2,1,'scatter marker with size\nof 2 y data units',fontsize=fs,bbox=boxprops,va='center')
    ax.text(3.6,6,'line marker with linewidth\nof 1 x data unit',fontsize=fs,bbox=boxprops,va='center')
    ax.text(3.6,2,'scatter marker with size\nof 1 x data unit',fontsize=fs,bbox=boxprops,va='center')
    ax.set_title('Linewidth and Markerwidth Set With Datascale')
    fig.savefig('datascale_plotdatasize_test',bbox_inches='tight')
    print('Test figure saved as \'datascale_plotdatasize_test\'')
    plt.close()
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlim([0,100])
    ax.set_ylim([0,100])
    ax.set_aspect('equal')
    lwp5=plotdatasize(axis='xy',mult=0.5)
    lw=plotdatasize(axis='xy')
    lw2=plotdatasize(axis='xy',mult=2)
    lw4=plotdatasize(axis='xy',mult=4)
    ax.plot([0,100],[0,100],linewidth=lwp5)
    ax.plot([20,120],[0,100],linewidth=lw)
    ax.plot([40,140],[0,100],linewidth=lw2)
    ax.plot([60,160],[0,100],linewidth=lw4)
    ax.xaxis.set_minor_locator(tck.MultipleLocator(1))
    ax.yaxis.set_minor_locator(tck.MultipleLocator(1))
    ax.grid(which='both',linewidth=0.1*lw)
    ax.set_title('Output DPI Set With Datascale')
    outdpi=plotdatadpi(mult=5)
    ax.text(5,95,'Set to resolve 5 pixels per data unit\nCalculated '+str('%3.2f' % outdpi)+' dpi\n*zoom to see detail',bbox=dict(facecolor='white'),va='top')
    fig.savefig('datascale_plotdatadpi_test',dpi=outdpi,bbox_inches='tight')
    print('Test figure saved as \'datascale_plotdatadpi_test\'')
    plt.close()
