---
entity_id: "gene.b0209"
entity_type: "gene"
name: "yafD"
source_database: "NCBI RefSeq"
source_id: "gene-b0209"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0209"
  - "yafD"
---

# yafD

`gene.b0209`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0209`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafD (gene.b0209) is a gene entity. It encodes yafD (protein.P0A8U2). Encoded protein function: UPF0294 protein YafD EcoCyc product frame: EG11650-MONOMER. Genomic coordinates: 231122-231922. EcoCyc protein note: YafD has similarity to E. coli YadD, which is encoded within the panBCD gene cluster .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoH (protein.P0AGB3), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8U2|protein.P0A8U2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=yafD; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yafD; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yafD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0000700,ECOCYC:EG11650,GeneID:946286`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:231122-231922:+; feature_type=gene
