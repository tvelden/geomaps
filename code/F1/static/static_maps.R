library(gpclib)       # loads polygon clipping library
library(maptools)     # loads sp library too
library(RColorBrewer) # creates nice color schemes
library(classInt)     # finds class intervals for continuous variables
library(shape)
library(rgdal)
mypath <- ("C:\\Python27\\final_mengproject\\data\\F1\\static\\")
mappath <- paste(mypath,"world.shp",sep="")
world.shp <- readShapePoly(mappath,proj4string=CRS("+proj=longlat"))

genericfilename <- paste (mypath,"fifth_cluster",sep="")
	   name <-paste(genericfilename,".csv",sep="")
       final_coordinates <- read.csv(name)

symbol.size <- final_coordinates$CNT


plot(world.shp)
points(final_coordinates$lon, final_coordinates$lat, pch=19,  cex=symbol.size)
title("Geographic overlay map",
    sub="Equal-Interval Class Intervals")
