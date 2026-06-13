---
entity_id: "gene.b4241"
entity_type: "gene"
name: "treR"
source_database: "NCBI RefSeq"
source_id: "gene-b4241"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4241"
  - "treR"
---

# treR

`gene.b4241`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4241`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

treR (gene.b4241) is a gene entity. It encodes treR (protein.P36673). Encoded protein function: FUNCTION: Repressor of the treBC operon. It is able to bind trehalose-6-phosphate and trehalose. {ECO:0000269|PubMed:7608078, ECO:0000269|PubMed:9148912}. EcoCyc product frame: EG12202-MONOMER. Genomic coordinates: 4466299-4467246.

## Biological Role

Repressed by phoP (protein.P23836). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36673|protein.P36673]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=treR; function=+
- `represses` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `C` - regulator=PhoP; target=treR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013875,ECOCYC:EG12202,GeneID:948760`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4466299-4467246:-; feature_type=gene
