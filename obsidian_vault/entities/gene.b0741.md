---
entity_id: "gene.b0741"
entity_type: "gene"
name: "pal"
source_database: "NCBI RefSeq"
source_id: "gene-b0741"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0741"
  - "pal"
---

# pal

`gene.b0741`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0741`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pal (gene.b0741) is a gene entity. It encodes pal (protein.P0A912). Encoded protein function: FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:11115123, PubMed:17233825). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). {ECO:0000269|PubMed:11115123, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098}. EcoCyc product frame: EG10684-MONOMER. EcoCyc synonyms: excC. Genomic coordinates: 779067-779588. EcoCyc protein note: Pal is an outer membrane component of the Tol-Pal system - a group of interacting proteins which span the cell envelope in E. coli K-12. The Tol-Pal system plays a role in outer membrane invagination and septal peptidoglycan processing during cell division and is important for maintaining outer membrane integrity via lipid homeostasis. It also has a role in facilitating phage infection and colicin uptake. Pal is a peptidoglycan-associated outer membrane lipoprotein . Pal interacts with TolA in vivo; this interaction requires the proton motive force . Pal interacts with TolB in vivo...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A912|protein.P0A912]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002521,ECOCYC:EG10684,GeneID:945004`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:779067-779588:+; feature_type=gene
