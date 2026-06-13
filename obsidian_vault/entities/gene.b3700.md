---
entity_id: "gene.b3700"
entity_type: "gene"
name: "recF"
source_database: "NCBI RefSeq"
source_id: "gene-b3700"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3700"
  - "recF"
---

# recF

`gene.b3700`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3700`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recF (gene.b3700) is a gene entity. It encodes recF (protein.P0A7H0). Encoded protein function: FUNCTION: The RecF protein is involved in DNA metabolism; it is required for DNA replication and normal SOS inducibility. RecF binds preferentially to single-stranded, linear DNA. It also seems to bind ATP. EcoCyc product frame: EG10828-MONOMER. EcoCyc synonyms: uvrF. Genomic coordinates: 3880148-3881221.

## Biological Role

Repressed by dnaA (protein.P03004), fis (protein.P0A6R3). Activated by rpoD (protein.P00579), dnaA (protein.P03004), argP (protein.P0A8S1), rpoS (protein.P13445).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7H0|protein.P0A7H0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=recF; function=+
- `activates` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `S` - regulator=DnaA; target=recF; function=-+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `S` - regulator=ArgP; target=recF; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=recF; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `S` - regulator=DnaA; target=recF; function=-+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=recF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012095,ECOCYC:EG10828,GeneID:948209`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3880148-3881221:-; feature_type=gene
