---
entity_id: "gene.b3828"
entity_type: "gene"
name: "metR"
source_database: "NCBI RefSeq"
source_id: "gene-b3828"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3828"
  - "metR"
---

# metR

`gene.b3828`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3828`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metR (gene.b3828) is a gene entity. It encodes metR (protein.P0A9F9). Encoded protein function: FUNCTION: Control of the last step in methionine biosynthesis; MetR is a positive activator of the metA, metE and metH genes. MetR is also a negative regulator of its own expression. Binds homocysteine as an inducer. EcoCyc product frame: PD03938. Genomic coordinates: 4011863-4012816.

## Biological Role

Repressed by metJ (protein.P0A8U6), metR (protein.P0A9F9), nac (protein.Q47005). Activated by oxyR (protein.P0ACQ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9F9|protein.P0A9F9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=metR; function=+
- `represses` <-- [[protein.P0A8U6|protein.P0A8U6]] `RegulonDB` `S` - regulator=MetJ; target=metR; function=-
- `represses` <-- [[protein.P0A9F9|protein.P0A9F9]] `RegulonDB` `S` - regulator=MetR; target=metR; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=metR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012506,ECOCYC:EG10591,GeneID:948310`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4011863-4012816:-; feature_type=gene
