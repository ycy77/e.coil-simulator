---
entity_id: "gene.b1604"
entity_type: "gene"
name: "ydgH"
source_database: "NCBI RefSeq"
source_id: "gene-b1604"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1604"
  - "ydgH"
---

# ydgH

`gene.b1604`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1604`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydgH (gene.b1604) is a gene entity. It encodes ydgH (protein.P76177). Encoded protein function: Protein YdgH EcoCyc product frame: G6860-MONOMER. Genomic coordinates: 1678427-1679371. EcoCyc protein note: Deletion of ydgH in E. coli K-12 strain BW25113 increases resistance to the beta-lactam antibiotic, CPD-9233 .

## Biological Role

Repressed by nac (protein.Q47005). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76177|protein.P76177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ydgH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005359,ECOCYC:G6860,GeneID:945117`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1678427-1679371:+; feature_type=gene
