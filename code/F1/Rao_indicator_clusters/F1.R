mypath <- ("C:\\Python27\\final_mengproject\\data\\F1\\Rao_indicator_clusters\\plots\\")
year <- c(1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010)
firstfile <-("C:\\Python27\\final_mengproject\\data\\F1\\Rao_indicator_clusters\\plots\\0.csv")
values <- read.csv(firstfile)
values <- values$CNT
values
plot(year,values,type="o", col="orange", axes= FALSE, ylim = c(0,20000), lwd=2)
axis(1, at = year)
axis(2)
myseq <- c("blue","red","black","green","yellow","pink","purple")
for (i in 1:7)
{
	 genericfilename <- paste (mypath,i,sep="")
       name <-paste(genericfilename,".csv",sep="")
       values <- read.csv(name)
	 values <- values$CNT
	 values
	 lines(year,values,type="o", col=myseq[i], lwd = 2)

}
legend("topright",
       legend = c("top1","top2","top3","top4","top5","top6","top7","top8"),
       fill = c("orange","blue","red","black","green","yellow","pink","purple"),
       bg = "white", ncol = 4)




# Create a title with a red, bold/italic font
title(main="Indicator - Field 1", col.main="red", font.main=4)