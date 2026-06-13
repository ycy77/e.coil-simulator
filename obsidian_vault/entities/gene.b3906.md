---
entity_id: "gene.b3906"
entity_type: "gene"
name: "rhaR"
source_database: "NCBI RefSeq"
source_id: "gene-b3906"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3906"
  - "rhaR"
---

# rhaR

`gene.b3906`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3906`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhaR (gene.b3906) is a gene entity. It encodes rhaR (protein.P09378). Encoded protein function: FUNCTION: Activates expression of the rhaSR operon in response to L-rhamnose. {ECO:0000255|HAMAP-Rule:MF_01533, ECO:0000269|PubMed:8230210, ECO:0000269|PubMed:8757746}. EcoCyc product frame: PD00222. EcoCyc synonyms: rhaC1. Genomic coordinates: 4098646-4099494.

## Biological Role

Activated by rpoD (protein.P00579), rhaS (protein.P09377), rhaR (protein.P09378), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09378|protein.P09378]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rhaR; function=+
- `activates` <-- [[protein.P09377|protein.P09377]] `RegulonDB` `S` - regulator=RhaS; target=rhaR; function=+
- `activates` <-- [[protein.P09378|protein.P09378]] `RegulonDB` `C` - regulator=RhaR; target=rhaR; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=rhaR; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rhaR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012747,ECOCYC:EG10842,GeneID:948396`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4098646-4099494:+; feature_type=gene
