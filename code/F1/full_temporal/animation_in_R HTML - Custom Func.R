library(gpclib)       # loads polygon clipping library
library(maptools)     # loads sp library too
library(RColorBrewer) # creates nice color schemes
library(classInt)     # finds class intervals for continuous variables
library(shape)
library(rgdal)
library(animation)

mypath <- ("C:\\Python27\\final_mengproject\\data\\F1\\full_temporal\\")
oopt = ani.options(outdir = getwd(),interval = 0.2, nmax = 50, ani.dev = png, ani.type = "png",
    ani.height = 700, ani.width = 700,
    title = "Mapping Scientific Networks-Geographic Overlay Maps",
    description = "Overlay maps that visualize the 
    interdisciplinarity and the geographic spread of 
research activities.")
ani.start()
opar = par(mar = c(3, 3, 1, 0.5), mgp = c(2, .5, 0), tcl = -0.3,
cex.axis = 0.8, cex.lab = 0.8, cex.main = 1)
mappath <- paste(mypath,"world.shp",sep="")
world.shp <- readShapePoly(mappath,proj4string=CRS("+proj=longlat"))
scientometric.ani <- function()
{
    for (i in 1991:2009)
    {
       genericfilename <- paste (mypath,"filecitiescount",sep="")
	 filename <- paste(genericfilename,i,sep="")
       name <-paste(filename,".csv",sep="")
       final_coordinates <- read.csv(name)
       plot(world.shp)
       symbol.size <- final_coordinates$CNT
	 plotclr <- brewer.pal(nclr,"BuPu")
	 plotclr <- plotclr[nclr:1] # reorder colors
	 class <- classIntervals(plotvar, nclr, style="equal")
 	 colcode <- findColours(class, plotclr)
	 points(final_coordinates$lon, final_coordinates$lat,pch=16, col=colcode, cex=symbol.size)
       mytitle <- paste("Geographic overlay map - ",i,sep="")
       title(mytitle,sub="Equal-Interval Class Intervals")
    }
}

saveHTML(scientometric.ani(), interval = 0.5, outdir = mypath) 

ani.options(oopt)