---
entity_id: "gene.b4452"
entity_type: "gene"
name: "gadY"
source_database: "NCBI RefSeq"
source_id: "gene-b4452"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4452"
  - "gadY"
---

# gadY

`gene.b4452`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4452`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gadY (gene.b4452) is a gene entity. EcoCyc product frame: IS183-RNA. EcoCyc synonyms: IS183. Genomic coordinates: 3664864-3664969.

## Biological Role

Activated by DNA-binding transcriptional dual regulator LldR-S-lactate (complex.ecocyc.CPLX0-7689), lrp (protein.P0ACJ0), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7689|complex.ecocyc.CPLX0-7689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=gadY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0047272,ECOCYC:G0-8914,GeneID:2847729`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3664864-3664969:+; feature_type=gene
