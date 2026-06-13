---
entity_id: "gene.b3895"
entity_type: "gene"
name: "fdhD"
source_database: "NCBI RefSeq"
source_id: "gene-b3895"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3895"
  - "fdhD"
---

# fdhD

`gene.b3895`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3895`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdhD (gene.b3895) is a gene entity. It encodes fdhD (protein.P32177). Encoded protein function: FUNCTION: Required for formate dehydrogenase (FDH) activity (PubMed:22194618, PubMed:25649206, PubMed:3077634, PubMed:8522521). Acts as a sulfur carrier protein that transfers sulfur from IscS to the molybdenum cofactor prior to its insertion into FDH. Specifically interacts with IscS and stimulates its cysteine desulfurase activity. Also binds the molybdenum cofactor (PubMed:22194618, PubMed:25649206). Required for activity of formate dehydrogenase N (FDH-N), formate dehydrogenase O (FDH-O) and formate dehydrogenase H (FDH-H) (PubMed:22194618, PubMed:3077634, PubMed:8522521). {ECO:0000269|PubMed:22194618, ECO:0000269|PubMed:25649206, ECO:0000269|PubMed:3077634, ECO:0000269|PubMed:8522521}. EcoCyc product frame: EG11859-MONOMER. Genomic coordinates: 4086016-4086849.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32177|protein.P32177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=fdhD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012714,ECOCYC:EG11859,GeneID:948393`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4086016-4086849:+; feature_type=gene
