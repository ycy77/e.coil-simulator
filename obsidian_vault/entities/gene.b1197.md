---
entity_id: "gene.b1197"
entity_type: "gene"
name: "treA"
source_database: "NCBI RefSeq"
source_id: "gene-b1197"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1197"
  - "treA"
---

# treA

`gene.b1197`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1197`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

treA (gene.b1197) is a gene entity. It encodes treA (protein.P13482). Encoded protein function: FUNCTION: Provides the cells with the ability to utilize trehalose at high osmolarity by splitting it into glucose molecules that can subsequently be taken up by the phosphotransferase-mediated uptake system. EcoCyc product frame: TREHALAPERI-MONOMER. EcoCyc synonyms: osmA, tre. Genomic coordinates: 1245679-1247376. EcoCyc protein note: E. coli contains two trehalases: the periplasmic TreA (discussed here) and the cytoplasmic TREHALACYTO-MONOMER "TreF". Both enzymes catalyze the hydrolysis of trehalose into two molecules of D-glucose. Crystal structures of the enzyme alone and complexed with inhibitors have been solved . Expression of periplasmic trehalase is increased under conditions of high osmolarity and during the transition to stationary phase . TreA-mediated periplasmic trehalose recycling during nutrient stress is proposed to have regulatory implications via glucose-flux sensing . treA mutants accumulate extracellular trehalose under osmotic stress conditions . Reviews:

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13482|protein.P13482]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=treA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004021,ECOCYC:EG11017,GeneID:945757`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1245679-1247376:-; feature_type=gene
