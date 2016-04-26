### dark-data-rules-generation

##Scripts to be run in the following order to generate Jena rules :

#1)Merging_Datasets_DarkData.R
Uses Raw Giovanni Log data and Solr Mappings File to create the dataset for Rule Generation.

#2)Rules_Gen.R
Combines Variable to Event Mappings with the above dataset to generate Association Rules

#3)RulesFormatting.py
Converts Association Rules generated in R to Human Readable Excel Worksheet.

#4)ImprovedRulesGen.py
Converts Excel Sheet Mentioned above into Jena Rules.
