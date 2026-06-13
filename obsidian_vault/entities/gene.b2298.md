---
entity_id: "gene.b2298"
entity_type: "gene"
name: "yfcC"
source_database: "NCBI RefSeq"
source_id: "gene-b2298"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2298"
  - "yfcC"
---

# yfcC

`gene.b2298`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2298`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfcC (gene.b2298) is a gene entity. It encodes yfcC (protein.P39263). Encoded protein function: FUNCTION: Metabolomic profiling of different yfcC over-expression and deletion strains suggests that it may affect the glyoxylate shunt. {ECO:0000305|PubMed:24513124}. EcoCyc product frame: G7190-MONOMER. Genomic coordinates: 2417081-2418601. EcoCyc protein note: Metabolomic profiling of various yfcC expression strains suggests that it may affect the glyoxylate shunt . In the Transporter Classification Database, YfcC is a member of the the Basic Amino Acid Antiporter (ArcD) Family within the Ion Transporter (IT) superfamily .

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39263|protein.P39263]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=yfcC; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yfcC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007585,ECOCYC:G7190,GeneID:946780`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2417081-2418601:+; feature_type=gene
