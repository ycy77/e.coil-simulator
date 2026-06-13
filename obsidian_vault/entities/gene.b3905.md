---
entity_id: "gene.b3905"
entity_type: "gene"
name: "rhaS"
source_database: "NCBI RefSeq"
source_id: "gene-b3905"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3905"
  - "rhaS"
---

# rhaS

`gene.b3905`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3905`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhaS (gene.b3905) is a gene entity. It encodes rhaS (protein.P09377). Encoded protein function: FUNCTION: Activates expression of the rhaBAD and rhaT operons. {ECO:0000255|HAMAP-Rule:MF_01534, ECO:0000269|PubMed:8230210, ECO:0000269|PubMed:8757746}. EcoCyc product frame: PD00221. EcoCyc synonyms: rhaC2. Genomic coordinates: 4097736-4098572.

## Biological Role

Activated by rpoD (protein.P00579), rhaS (protein.P09377), rhaR (protein.P09378), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09377|protein.P09377]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rhaS; function=+
- `activates` <-- [[protein.P09377|protein.P09377]] `RegulonDB` `S` - regulator=RhaS; target=rhaS; function=+
- `activates` <-- [[protein.P09378|protein.P09378]] `RegulonDB` `C` - regulator=RhaR; target=rhaS; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=rhaS; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rhaS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012745,ECOCYC:EG10843,GeneID:948397`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4097736-4098572:+; feature_type=gene
