library(gpclib)       # loads polygon clipping library
library(maptools)     # loads sp library too
library(RColorBrewer) # creates nice color schemes
library(classInt)     # finds class intervals for continuous variables
library(shape)
library(rgdal)
mypath <- ("/Users/theresavelden/Networks/StudentProjects/git/geomaps-project-files/geomaps/data/F1/static/")
mappath <- paste(mypath,"world.shp",sep="")
world.shp <- readShapePoly(mappath,proj4string=CRS("+proj=longlat"))

genericfilename <- paste (mypath,"sixth_cluster",sep="")
	   name <-paste(genericfilename,".csv",sep="")
       final_coordinates <- read.csv(name)


plotvar <- final_coordinates$CNT
nclr <- 7
plotclr <- brewer.pal(nclr,"BuPu")
plotclr <- plotclr[nclr:1] # reorder colors
class <- classIntervals(plotvar, nclr, style="equal")
colcode <- findColours(class, plotclr)

symbol.size <- final_coordinates$CNT


plot(world.shp)
points(final_coordinates$lon, final_coordinates$lat, pch=19, col=colcode, cex=symbol.size)
title("Geographic overlay map",
    sub="Equal-Interval Class Intervals")

