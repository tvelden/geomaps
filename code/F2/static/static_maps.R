library(gpclib)       # loads polygon clipping library
library(maptools)     # loads sp library too
library(RColorBrewer) # creates nice color schemes
library(classInt)     # finds class intervals for continuous variables
library(shape)
library(rgdal)
mypath <- ("C:\\Python27\\final_mengproject\\data\\F2\\static\\")
mappath <- paste(mypath,"world.shp",sep="")
world.shp <- readShapePoly(mappath,proj4string=CRS("+proj=longlat"))

genericfilename <- paste (mypath,"fifth_cluster",sep="")
	   name <-paste(genericfilename,".csv",sep="")
       final_coordinates <- read.csv(name)

#plotvar <- orstationc$tann
#nclr <- 8
plotclr <- brewer.pal(nclr,"BuPu")
plotclr <- plotclr[nclr:1] # reorder colors
class <- classIntervals(plotvar, nclr, style="equal")
colcode <- findColours(class, plotclr)

#family <- as.factor(final_coordinates$lat)

symbol.size <- final_coordinates$CNT


plot(world.shp)
points(final_coordinates$lon, final_coordinates$lat, pch=19, col=colcode, cex=symbol.size)
#points(final_coordinates$lon, final_coordinates$lat, cex=symbol.size)
title("Geographic overlay map",
    sub="Equal-Interval Class Intervals")
#legend(-117, 44, legend=names(attr(colcode, "table")), 
 #   fill=attr(colcode, "palette"), cex=0.6, bty="n")

