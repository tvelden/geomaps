library(calibrate)

mypath <- ("/Users/theresavelden/Networks/StudentProjects/git/geomaps-project-files/geomaps/data/F1_F2_indicator/plots/")
year <- c(1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010)
firstfile <-("/Users/theresavelden/Networks/StudentProjects/git/geomaps-project-files/geomaps/data/F1_F2_indicator/plots/0.csv")

values <- read.csv(firstfile)

values <- values$CNT

#label1
#label2
plot(year,values,type="o", col="orange", axes= FALSE, ylim = c(0,15000), lwd=2)
axis(1, at = year)
axis(2)
myseq <- c("blue")
for (i in 1:1)
{
	 genericfilename <- paste (mypath,i,sep="")
       name <-paste(genericfilename,".csv",sep="")
name
       values <- read.csv(name)
	 values <- values$CNT
       lines(year,values,type="o", col=myseq[i], lwd = 2) 
 	 

}
legend("topleft",
       legend = c("Field 1","Field 2"),
       fill = c("orange","blue"),
       bg = "white", ncol = 2)




# Create a title with a red, bold/italic font
title(main="Indicator - Field 1 & Field 2", col.main="red", font.main=4)