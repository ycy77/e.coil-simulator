---
entity_id: "gene.b3743"
entity_type: "gene"
name: "asnC"
source_database: "NCBI RefSeq"
source_id: "gene-b3743"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3743"
  - "asnC"
---

# asnC

`gene.b3743`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3743`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

asnC (gene.b3743) is a gene entity. It encodes asnC (protein.P0ACI6). Encoded protein function: FUNCTION: Activator of asnA transcription; autogenous regulator of its own transcription; and repressor of the expression of gidA at a post-transcriptional level. {ECO:0000269|PubMed:2836709, ECO:0000269|PubMed:2864330, ECO:0000269|PubMed:3909107}. EcoCyc product frame: PD00250. Genomic coordinates: 3926545-3927003.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACI6|protein.P0ACI6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=asnC; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=asnC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012237,ECOCYC:EG10093,GeneID:948259`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3926545-3927003:-; feature_type=gene
