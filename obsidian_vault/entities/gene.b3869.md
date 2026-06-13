---
entity_id: "gene.b3869"
entity_type: "gene"
name: "glnL"
source_database: "NCBI RefSeq"
source_id: "gene-b3869"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3869"
  - "glnL"
---

# glnL

`gene.b3869`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3869`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnL (gene.b3869) is a gene entity. It encodes glnL (protein.P0AFB5). Encoded protein function: FUNCTION: Member of the two-component regulatory system NtrB/NtrC, which controls expression of the nitrogen-regulated (ntr) genes in response to nitrogen limitation. Under conditions of nitrogen limitation, NtrB autophosphorylates and transfers the phosphoryl group to NtrC. In the presence of nitrogen, acts as a phosphatase that dephosphorylates and inactivates NtrC. {ECO:0000269|PubMed:10074086, ECO:0000269|PubMed:2574599, ECO:0000269|PubMed:2874557, ECO:0000269|PubMed:3304660}. EcoCyc product frame: PROTEIN-NRII. EcoCyc synonyms: glnR, ntrB. Genomic coordinates: 4055290-4056339.

## Biological Role

Repressed by glnG (protein.P0AFB8). Activated by fis (protein.P0A6R3), lrp (protein.P0ACJ0), glnG (protein.P0AFB8), rpoN (protein.P24255).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFB5|protein.P0AFB5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=glnL; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=glnL; function=-+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=glnL; function=+
- `represses` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=glnL; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0012634,ECOCYC:EG10387,GeneID:948360`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4055290-4056339:-; feature_type=gene
