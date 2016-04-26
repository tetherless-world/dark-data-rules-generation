#______________________________________________

#Improved Dataset

rm(log_parsed_new)
log_parsed_new <- read.delim("~/Downloads/log_parsed_new.csv", dec=".")
nrows <- nrow(log_parsed_new) 


log_parsed_new$ID <- paste(log_parsed_new$GCMD_ID.1,log_parsed_new$Variable.1,sep = '_')
log_parsed_new$ID2 <- paste(log_parsed_new$GCMD_ID.2,log_parsed_new$Variable.2,sep = '_')


for(i in 1:nrows)
{if((log_parsed_new$GCMD_ID.1[i])==""||is.na(log_parsed_new$GCMD_ID.1[i]))
{
 log_parsed_new$ID[i] <- paste(log_parsed_new$Dataset.1[i], log_parsed_new$Version.1[i], log_parsed_new$Variable.1[i], sep='_')
}}

for(i in 1:nrows)
{if((log_parsed_new$GCMD_ID.2[i])==""||is.na(log_parsed_new$GCMD_ID.2[i]))
{
  log_parsed_new$ID2[i] <- paste(log_parsed_new$Dataset.2[i], log_parsed_new$Version.2[i], log_parsed_new$Variable.2[i], sep='_')
}}


log_parsed_new$ID <- as.factor(log_parsed_new$ID)
log_parsed_new$ID2 <- as.factor(log_parsed_new$ID2)

g3_datafields <- read.delim("~/Downloads/g3_datafields.csv", dec=".",sep = ",")
g3_datafields$measurements <- gsub(',', '/', g3_datafields$measurements)

g3_datafields$ID <- paste(g3_datafields$product.gcmd.id,g3_datafields$sds.name,sep='_')
g3_datafields$processing.level <- as.factor(g3_datafields$processing.level)
g3_datafields$ID <- as.factor(g3_datafields$ID)
summary(g3_datafields)
#g3_datafields[,14]<-NULL
colnames(g3_datafields)[14]<-"ID"


yy = merge(log_parsed_new,g3_datafields,by="ID",all.x = TRUE)
colnames(g3_datafields)[14]<-"ID2"
yyy = merge(yy,g3_datafields,by="ID2",all.x = TRUE)

missing_logvalues <- yyy[is.na(yyy$platform.instrument.x),]

x<-levels(missing_logvalues$ID)
write.table(x,"missingvariable_list.txt")

warnings()
