#Rules based on measurements only

RS_Improved <- data.frame(yyy$ID,yyy$ID2,yyy$Service,yyy$processing.level.x,yyy$measurements.x,yyy$time.interval.x,yyy$spatial.resolution.x,yyy$instrument.x,yyy$processing.level.y,yyy$measurements.y,yyy$time.interval.y,yyy$spatial.resolution.y,yyy$instrument.y,yyy$product.x,yyy$product.y)

RS_Improved$VolcanicEruption <- 0
RS_Improved$Hurricane <-0 
RS_Improved$Flood <- 0
RS_Improved$Fire <- 0

colnames(RS_Improved)[1] <- "ID1"
colnames(RS_Improved)[2] <- "ID2"
colnames(RS_Improved)[3] <- "Service"
colnames(RS_Improved)[4] <- "Processing_Level1"
colnames(RS_Improved)[5] <- "Measurement1"
colnames(RS_Improved)[6] <- "Time_Interval1"
colnames(RS_Improved)[7] <- "Spatial_Resolution1"
colnames(RS_Improved)[8] <- "Instrument1"
colnames(RS_Improved)[9] <- "Processing_Level2"
colnames(RS_Improved)[10] <- "Measurement2"
colnames(RS_Improved)[11] <- "Time_Interval2"
colnames(RS_Improved)[12] <- "Spatial_Resolution2"
colnames(RS_Improved)[13] <- "Instrument2"
colnames(RS_Improved)[16] <- "VolcanicEruption"
colnames(RS_Improved)[17] <- "Hurricane"
colnames(RS_Improved)[14] <- "Product1"
colnames(RS_Improved)[15] <- "Product2"

Fire <- read.delim("/Users/anirudhprabhu/PycharmProjects/dark-data-rules-generation/DarkData_Python/Fire_ranking_result_optimal_Ensemble.txt.GIOVANNI.collection_parameter-1.txt", dec=".",sep = '#')
Flood <- read.delim("/Users/anirudhprabhu/PycharmProjects/dark-data-rules-generation/DarkData_Python/Flood_ranking_result_optimal_Ensemble.txt.GIOVANNI.collection_parameter.txt", dec=".",sep = '#')
Volcano <- read.delim("/Users/anirudhprabhu/PycharmProjects/dark-data-rules-generation/DarkData_Python/Volcano_ranking_result_optimal_Ensemble.txt.GIOVANNI.collection_parameter.txt", dec=".",sep = '#')
Hurricane <- read.delim("/Users/anirudhprabhu/PycharmProjects/dark-data-rules-generation/DarkData_Python/Hurricane_ranking_result_optimal_Ensemble.txt.GIOVANNI.collection_parameter.txt", dec=".",sep = '#')

len <- nrow(Volcano)

for (x in 1:len)
{RS_Improved$VolcanicEruption[grep(Volcano$dataFieldId[x],RS_Improved$ID1)]<-1}

len <- nrow(Hurricane)
for (x in 1:len)
{RS_Improved$Hurricane[grep(Hurricane$dataFieldId[x],RS_Improved$ID1,ignore.case = TRUE)]<-1}

len <- nrow(Flood)
for (x in 1:len)
{RS_Improved$Flood[grep(Flood$dataFieldId[x],RS_Improved$ID1,ignore.case = TRUE)]<-1}

len <- nrow(Fire)
for (x in 1:len)
{RS_Improved$Fire[grep(Fire$dataFieldId[x],RS_Improved$ID1,ignore.case = TRUE)]<-1}

#Tests?
library(plyr)
count(RS_Improved$VolcanicEruption)
count(RS_Improved$Hurricane)
count(RS_Improved$Flood)
count(RS_Improved$Fire)


RS_Improved$VolcanicEruption <- as.factor(RS_Improved$VolcanicEruption)
RS_Improved$Hurricane <- as.factor(RS_Improved$Hurricane)
RS_Improved$Flood <- as.factor(RS_Improved$Flood)
RS_Improved$Fire <- as.factor(RS_Improved$Fire)

#Removing the IDs

RS_Improved_less <- RS_Improved

RS_Improved_less$ID1 <- NULL
RS_Improved_less$ID2 <- NULL
RS_Improved_less$Product1<-NULL
RS_Improved_less$Product2<-NULL


rules <- apriori(data = RS_Improved_less, parameter = list(supp = 0.0000001, conf = 0.1,target = "rules"))

rules.sub.predict <- subset(rules, subset = ((rhs %pin% "Service")))

rules.with.events <- subset(rules.sub.predict,subset = ((lhs %pin% "VolcanicEruption=1")|(lhs %pin% "Hurricane=1")|(lhs %pin% "Fire=1")|(lhs %pin% "Flood=1")))

rules.sub.AP <- subset(rules.with.events, subset = ((lhs %pin% "Measurement1")&(lhs %pin% "Measurement2")&(lhs %pin% "Spatial_Resolution2")&(lhs %pin% "Spatial_Resolution1")&(lhs %pin% "Time_Interval1")&(lhs %pin% "Time_Interval2")))

rules.sub.one.var <- subset(rules.with.events, subset = (((lhs %pin% "Measurement1")|(lhs %pin% "Instrument1")|(lhs %pin% "Time_Interval1")|(lhs %pin% "Spatial_Resolution1"))&(!(lhs %pin% "Measurement2"))&(!(lhs %pin% "Spatial_Resolution2"))&(!(lhs %pin% "Time_Interval2"))&(!(lhs %pin% "Instrument2"))&(!(lhs %pin% "Processing_Level2"))))

rules.sub.only.second.var <- subset(rules.with.events, subset = (((lhs %pin% "Measurement2")|(lhs %pin% "Instrument2")|(lhs %pin% "Time_Interval2")|(lhs %pin% "Spatial_Resolution2"))&(!(lhs %pin% "Measurement1"))&(!(lhs %pin% "Spatial_Resolution1"))&(!(lhs %pin% "Time_Interval1"))&(!(lhs %pin% "Instrument1"))&(!(lhs %pin% "Processing_Level1"))))


inspect((rules.sub.AP))
inspect(rules.sub.one.var)

write(rules.sub.AP, file = "/Users/anirudhprabhu/PycharmProjects/dark-data-rules-generation/DarkData_Python/DarkData_Rules_Improved_two_var.txt", sep = "\t")
write(rules.sub.one.var, file = "/Users/anirudhprabhu/PycharmProjects/dark-data-rules-generation/DarkData_Python/DarkData_Rules_Improved_one_var.txt", sep = "\t")
write(rules.sub.only.second.var, file = "/Users/anirudhprabhu/PycharmProjects/dark-data-rules-generation/DarkData_Python/DarkData_Rules_Improved_only_second_var.txt", sep = "\t")

#Stop here and run the python script

write.xlsx(DarkData_Rules_Improved_AP, file = "DarkData_Rules_Improved_AP.xlsx")

plot(rules.sub.AP, method="graph", control=list(type="items"))
plot(rules.sub.AP)

#BadRules

BadTimeRes<-DarkData_Rules_Improved_AP[(DarkData_Rules_Improved_AP$Time_Interval1 != DarkData_Rules_Improved_AP$Time_Interval2),]
BadSpatialRes<-DarkData_Rules_Improved_AP[(DarkData_Rules_Improved_AP$Spatial_Resolution1 != DarkData_Rules_Improved_AP$Spatial_Resolution2),]

write.xlsx(BadSpatialRes, file = "BadSpace.xlsx")
write.xlsx(BadTimeRes, file = "BadTime.xlsx")
