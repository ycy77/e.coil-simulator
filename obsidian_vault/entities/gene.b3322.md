---
entity_id: "gene.b3322"
entity_type: "gene"
name: "gspB"
source_database: "NCBI RefSeq"
source_id: "gene-b3322"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3322"
  - "gspB"
---

# gspB

`gene.b3322`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3322`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gspB (gene.b3322) is a gene entity. It encodes gspB (protein.P03825). Encoded protein function: FUNCTION: Part of a cryptic operon that encodes proteins involved in type II secretion pathway in other organisms, but is not expressed in strain K12 under standard laboratory conditions (PubMed:8655552). May play a regulatory role under conditions of derepressed gsp gene expression (PubMed:11118204). {ECO:0000269|PubMed:11118204, ECO:0000305|PubMed:8655552}. EcoCyc product frame: EG11263-MONOMER. EcoCyc synonyms: pioO, pinO. Genomic coordinates: 3453508-3453927. EcoCyc protein note: E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system (T2SS); the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . The inner membrane proteins GspA and GspB contribute to G7703-MONOMER secretin assembly and transport in some gram-negative T2SSs (see ). Comment from EcoGene: gspB was initially identified as an ORF that might be the 11.3 kDa "initiation protein" PinO synthesized in the absence of isoleucine in relA stains ()...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03825|protein.P03825]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gspB; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=gspB; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gspB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010865,ECOCYC:EG11263,GeneID:947826`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3453508-3453927:-; feature_type=gene
