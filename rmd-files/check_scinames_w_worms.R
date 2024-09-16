library(tidyverse)
library(worrms)
library(obistools)

## Lire dans le fichier et la feuille excel à comparer

scinames_df <- readxl::read_excel('data/nafo2016presencedata.xlsx', sheet='IDmatch')

# Vérifier la colonne des noms
names(scinames_df)

## Récupérer le nom scientifique unique
names_to_search <- scinames_df %>% distinct(`Scientific Name`)

## Vérifier.
names_to_search

## Dans cet exemple, ils étaient déjà uniques! 
#    Faire une requête WoRMS pour les sciname et aphiaID de chacun.

scinames_matched <- scinames_df %>% 
                      mutate(sciNameID = obistools::match_taxa(`Scientific Name`, ask=FALSE)$scientificNameID) %>%
                      mutate(aphiaID = paste0('urn:lsid:marinespecies.org:taxname:', aphiaID))

## Comparer les aphiaID avec les aphiaID récupérés
##   Y a t il des résultats multiples accepted/unaccepted, voir les possibles corrections

View(scinames_matched)

scinames_matched %>% filter(aphiaID != sciNameID | is.na(sciNameID)) %>% write_csv('data/questionable_sciname_aphiaID_pairs.csv')

## HORS SCRIPT: testing match_taxa - pour la beauté du geste.

obistools::match_taxa('Hymenodora glacialis', ask=FALSE)
## Verifier que le status == accepted pour chacun

## Verifier aue les noms cientifiques et vernaculaires sdu fichier excel correspondent aux valeurs récupérées
