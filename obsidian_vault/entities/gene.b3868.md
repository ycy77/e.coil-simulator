---
entity_id: "gene.b3868"
entity_type: "gene"
name: "glnG"
source_database: "NCBI RefSeq"
source_id: "gene-b3868"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3868"
  - "glnG"
---

# glnG

`gene.b3868`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3868`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnG (gene.b3868) is a gene entity. It encodes glnG (protein.P0AFB8). Encoded protein function: FUNCTION: Member of the two-component regulatory system NtrB/NtrC, which controls expression of the nitrogen-regulated (ntr) genes in response to nitrogen limitation. Phosphorylated NtrC binds directly to DNA and stimulates the formation of open promoter-sigma54-RNA polymerase complexes (PubMed:1350679, PubMed:2574599, PubMed:2874557, PubMed:3304660). Activates transcription of many genes and operons whose products minimize the slowing of growth under nitrogen-limiting conditions, including genes coding for glutamine synthetase (glnA), transporters, amino acid permeases and catabolic enzymes (PubMed:11121068). {ECO:0000269|PubMed:11121068, ECO:0000269|PubMed:1350679, ECO:0000269|PubMed:2574599, ECO:0000269|PubMed:2874557, ECO:0000269|PubMed:3304660}. EcoCyc product frame: PROTEIN-NRI. EcoCyc synonyms: glnT, ntrC. Genomic coordinates: 4053869-4055278.

## Biological Role

Repressed by glnG (protein.P0AFB8). Activated by fis (protein.P0A6R3), glnG (protein.P0AFB8), rpoN (protein.P24255).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFB8|protein.P0AFB8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=glnG; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=glnG; function=-+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=glnG; function=+
- `represses` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=glnG; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0012632,ECOCYC:EG10385,GeneID:948361`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4053869-4055278:-; feature_type=gene
