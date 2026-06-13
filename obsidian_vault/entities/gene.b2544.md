---
entity_id: "gene.b2544"
entity_type: "gene"
name: "yphB"
source_database: "NCBI RefSeq"
source_id: "gene-b2544"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2544"
  - "yphB"
---

# yphB

`gene.b2544`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2544`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yphB (gene.b2544) is a gene entity. It encodes yphB (protein.P76584). Encoded protein function: Uncharacterized protein YphB EcoCyc product frame: G7338-MONOMER. Genomic coordinates: 2673816-2674688. EcoCyc protein note: YphB may be a sulfoquinovose mutarotase. The gene cluster encoding enzymes of the sulfoquinovose degradation pathway is conserved, and a putative epimerase is encoded by EG11844-MONOMER YihR within the gene cluser. The YihR homolog of Herbaspirillum seropedicaea was shown to have sulfoquinovose mutarotase activity . However, the best BLAST hit of the H. seropedicaea protein in the E. coli genome is YphB rather than YihR.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76584|protein.P76584]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008368,ECOCYC:G7338,GeneID:947017`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2673816-2674688:-; feature_type=gene
