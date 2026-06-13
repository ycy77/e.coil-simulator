---
entity_id: "gene.b0468"
entity_type: "gene"
name: "ybaN"
source_database: "NCBI RefSeq"
source_id: "gene-b0468"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0468"
  - "ybaN"
---

# ybaN

`gene.b0468`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0468`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybaN (gene.b0468) is a gene entity. It encodes ybaN (protein.P0AAR5). Encoded protein function: Inner membrane protein YbaN EcoCyc product frame: EG12843-MONOMER. Genomic coordinates: 490882-491259. EcoCyc protein note: YbaN is an inner membrane protein with four predicted transmembrane domains. The C terminus is located in the cytoplasm .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAR5|protein.P0AAR5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=ybaN; function=-
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=ybaN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001625,ECOCYC:EG12843,GeneID:945558`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:490882-491259:+; feature_type=gene
