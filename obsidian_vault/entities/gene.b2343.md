---
entity_id: "gene.b2343"
entity_type: "gene"
name: "yfcZ"
source_database: "NCBI RefSeq"
source_id: "gene-b2343"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2343"
  - "yfcZ"
---

# yfcZ

`gene.b2343`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2343`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfcZ (gene.b2343) is a gene entity. It encodes yfcZ (protein.P0AD33). Encoded protein function: UPF0381 protein YfcZ EcoCyc product frame: G7214-MONOMER. Genomic coordinates: 2460650-2460934. EcoCyc protein note: Expression of yfcZ is activated by FNR . The half life of yfcZ mRNA is substantially longer in cells lacking G7459-MONOMER RppH than in wild type cells .

## Biological Role

Repressed by lrp (protein.P0ACJ0), rpoN (protein.P24255). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD33|protein.P0AD33]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=yfcZ; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yfcZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P24255|protein.P24255]] `RegulonDB|EcoCyc` `S` - regulator=RpoN; target=yfcZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007731,ECOCYC:G7214,GeneID:948817`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2460650-2460934:-; feature_type=gene
