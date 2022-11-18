# datascale

Functions for automatic scaling of matplotlib plot axes/resolution to data

## plotdatasize()

Scale line width or marker width for line plots and scatter plots to correspond directly to the scale of data on either/both plot axes.

![plotdatasize() example](/images/datascale_plotdatasize_test.png?raw=true)

Reproduce this image:

```python
import datascale as ds 
import matplotlib.pyplot as plt 
import matplotlib.ticker as tck 
plt.ioff()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim([0,5])
ax.set_ylim([0,12])
lwy=ds.plotdatasize()
lwy2=ds.plotdatasize(mult=2)
lwx=ds.plotdatasize(axis='x')
msy=ds.plotdatasize(plottype='scatter')
msy2=ds.plotdatasize(plottype='scatter',mult=2)
msx=ds.plotdatasize(plottype='scatter',axis='x')
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
```

## plotdatadpi()

Scale dpi of output image to produce a certain number of pixels per data unit on either/both plot axis/axes. Useful for plots that need a certain amount of detail per axis unit (e.g. geographic projections).

![plotdatadpi() example](/images/datascale_plotdatadpi_test.png?raw=true)

Reproduce this image:

```python
import datascale as ds 
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
plt.ioff()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlim([0,100])
ax.set_ylim([0,100])
ax.set_aspect('equal')
lwp5=ds.plotdatasize(axis='xy',mult=0.5)
lw=ds.plotdatasize(axis='xy')
lw2=ds.plotdatasize(axis='xy',mult=2)
lw4=ds.plotdatasize(axis='xy',mult=4)
ax.plot([0,100],[0,100],linewidth=lwp5)
ax.plot([20,120],[0,100],linewidth=lw)
ax.plot([40,140],[0,100],linewidth=lw2)
ax.plot([60,160],[0,100],linewidth=lw4)
ax.xaxis.set_minor_locator(tck.MultipleLocator(1))
ax.yaxis.set_minor_locator(tck.MultipleLocator(1))
ax.grid(which='both',linewidth=0.1*lw)
ax.set_title('Output DPI Set With Datascale')
outdpi=ds.plotdatadpi(mult=5)
ax.text(5,95,'Set to resolve 5 pixels per data unit\nCalculated '+str('%3.2f' % outdpi)+' dpi\n*zoom to see detail',bbox=dict(facecolor='white'),va='top')
fig.savefig('datascale_plotdatadpi_test',dpi=outdpi,bbox_inches='tight')
print('Test figure saved as \'datascale_plotdatadpi_test\'')
```

