---
entity_id: "gene.b4393"
entity_type: "gene"
name: "trpR"
source_database: "NCBI RefSeq"
source_id: "gene-b4393"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4393"
  - "trpR"
---

# trpR

`gene.b4393`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4393`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trpR (gene.b4393) is a gene entity. It encodes trpR (protein.P0A881). Encoded protein function: FUNCTION: This protein is an aporepressor. When complexed with L-tryptophan it binds the operator region of the trp operon (5'-ACTAGT-'3') and prevents the initiation of transcription. The complex also regulates trp repressor biosynthesis by binding to its regulatory region. EcoCyc product frame: PD00423. EcoCyc synonyms: rtrY. Genomic coordinates: 4632760-4633086.

## Biological Role

Repressed by trpR (protein.P0A881). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A881|protein.P0A881]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=trpR; function=+
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `S` - regulator=TrpR; target=trpR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014408,ECOCYC:EG11029,GeneID:948917`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4632760-4633086:+; feature_type=gene
