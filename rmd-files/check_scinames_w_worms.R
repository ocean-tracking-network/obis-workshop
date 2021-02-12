library(tidyverse)
library(worrms)
library(obistools)

## Read in the Excel file and sheet that we need to compare

scinames_df <- readxl::read_excel('data/nafo2016presencedata.xlsx', sheet='IDmatch')

# check the column names
names(scinames_df)

## Get the unique scientificnames
names_to_search <- scinames_df %>% distinct(`Scientific Name`)

## Check they're ok.
names_to_search

## This time they were already unique! 
#    Query WoRMS for the sciname and aphiaID for each.

scinames_matched <- scinames_df %>% 
                      mutate(sciNameID = obistools::match_taxa(`Scientific Name`, ask=FALSE)$scientificNameID) %>%
                      mutate(aphiaID = paste0('urn:lsid:marinespecies.org:taxname:', aphiaID))

## Compare the aphiaID to the returned aphiaID 
##    (did it return multiple accepted/unaccepted? may have to fix)

View(scinames_matched)

scinames_matched %>% filter(aphiaID != sciNameID | is.na(sciNameID)) %>% write_csv('data/questionable_sciname_aphiaID_pairs.csv')

## NOT PART OF SCRIPT: testing match_taxa - it was being funny.

obistools::match_taxa('Hymenodora glacialis', ask=FALSE)
## Verify that status == accepted for each

## Verify that scinames and vernaculars in excel file match the returned values