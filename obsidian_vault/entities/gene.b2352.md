---
entity_id: "gene.b2352"
entity_type: "gene"
name: "yfdI"
source_database: "NCBI RefSeq"
source_id: "gene-b2352"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2352"
  - "yfdI"
---

# yfdI

`gene.b2352`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2352`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdI (gene.b2352) is a gene entity. It encodes yfdI (protein.P76507). Encoded protein function: Uncharacterized protein YfdI EcoCyc product frame: G7221-MONOMER. EcoCyc synonyms: gtrS, gtrIV. Genomic coordinates: 2469131-2470462. EcoCyc protein note: yfdG, yfdH and yfdI constitute a three gene cluster within the CPS-53/KpLE1 cryptic prophage . yfdI (also called GtrIVEC) shows significant homology (41% identity and 63% similarity) with gtrIV, encoding a type IV-specific glucosyltransferase in the genome of Shigella flexneri NCTC 8296 . yfdG, yfdH and yfdI mediate partial O-antigen modification when introduced together into S. flexneri serotype Y strain SFL124; yfdI may encode a glucosyltransferase that is specific for the E. coli K-12 O16 O antigen (which differs from the S. flexneri O antigen) . yfdI contains a predicted PD00214 "OxyR" target site; DNase footprinting showed strong binding by oxidized OxyR and weak binding by reduced OxyR to the predicted site within yfdI but no OxyR-regulated transcript was detected . Please note: E. coli K-12 does not produce an O-antigen due to mutations in the rfb region; a reconstructed strain with all rfb genes intact produces an O16 antigen .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76507|protein.P76507]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007765,ECOCYC:G7221,GeneID:946822`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2469131-2470462:+; feature_type=gene
