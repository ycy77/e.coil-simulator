---
entity_id: "gene.b4018"
entity_type: "gene"
name: "iclR"
source_database: "NCBI RefSeq"
source_id: "gene-b4018"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4018"
  - "iclR"
---

# iclR

`gene.b4018`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4018`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iclR (gene.b4018) is a gene entity. It encodes iclR (protein.P16528). Encoded protein function: FUNCTION: Regulation of the glyoxylate bypass operon (aceBAK), which encodes isocitrate lyase, malate synthase as well as isocitrate dehydrogenase kinase/phosphorylase. Glyoxylate disrupts the interaction with the promoter by favoring the inactive dimeric form. Pyruvate enhances promoter binding by stabilizing the tetrameric form. EcoCyc product frame: PD04099. Genomic coordinates: 4222804-4223628.

## Biological Role

Repressed by iclR (protein.P16528). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930), fadR (protein.P0A8V6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16528|protein.P16528]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `C` - regulator=FadR; target=iclR; function=+
- `represses` <-- [[protein.P16528|protein.P16528]] `RegulonDB` `S` - regulator=IclR; target=iclR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013136,ECOCYC:EG10491,GeneID:948524`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4222804-4223628:-; feature_type=gene
