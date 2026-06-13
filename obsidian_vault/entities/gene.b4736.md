---
entity_id: "gene.b4736"
entity_type: "gene"
name: "yliM"
source_database: "NCBI RefSeq"
source_id: "gene-b4736"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4736"
  - "yliM"
---

# yliM

`gene.b4736`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4736`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yliM (gene.b4736) is a gene entity. It encodes yliM (protein.P0DPN6). Encoded protein function: Protein YliM EcoCyc product frame: MONOMER0-4413. Genomic coordinates: 850332-850397. EcoCyc protein note: YliM was identified as a previously unannotated small protein; its expression is higher during exponential phase than during stationary phase .

## Biological Role

Repressed by micA (gene.b4442). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPN6|protein.P0DPN6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yliM; function=+
- `represses` <-- [[gene.b4442|gene.b4442]] `RegulonDB` `S` - regulator=MicA; target=yliM; function=-

## External IDs

- `Dbxref:ECOCYC:G0-16731,GeneID:38094946`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:850332-850397:+; feature_type=gene
