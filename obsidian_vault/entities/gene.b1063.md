---
entity_id: "gene.b1063"
entity_type: "gene"
name: "yceB"
source_database: "NCBI RefSeq"
source_id: "gene-b1063"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1063"
  - "yceB"
---

# yceB

`gene.b1063`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1063`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yceB (gene.b1063) is a gene entity. It encodes yceB (protein.P0AB26). Encoded protein function: Uncharacterized lipoprotein YceB EcoCyc product frame: EG11117-MONOMER. Genomic coordinates: 1122713-1123273. EcoCyc protein note: YceB belongs to the superfamily of tubular lipid-binding proteins (TULIPs) . YceB is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ).

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB26|protein.P0AB26]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003611,ECOCYC:EG11117,GeneID:947377`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1122713-1123273:-; feature_type=gene
