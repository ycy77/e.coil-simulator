---
entity_id: "gene.b3555"
entity_type: "gene"
name: "yiaG"
source_database: "NCBI RefSeq"
source_id: "gene-b3555"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3555"
  - "yiaG"
---

# yiaG

`gene.b3555`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3555`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiaG (gene.b3555) is a gene entity. It encodes yiaG (protein.P0A9V5). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YiaG EcoCyc product frame: EG12624-MONOMER. Genomic coordinates: 3719478-3719768. EcoCyc protein note: YiaG, which contains a helix-turn-helix motif to bind DNA in its C-terminal domain, appears to belong to the Xre family of transcription factors, and it was predicted to regulate genes related to protein export . The transcription of the yiaG gene is affected by stress, stringent response, and glucose-lactose shift .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9V5|protein.P0A9V5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yiaG; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011612,ECOCYC:EG12624,GeneID:948071`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3719478-3719768:+; feature_type=gene
