---
entity_id: "gene.b2671"
entity_type: "gene"
name: "ygaC"
source_database: "NCBI RefSeq"
source_id: "gene-b2671"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2671"
  - "ygaC"
---

# ygaC

`gene.b2671`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2671`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygaC (gene.b2671) is a gene entity. It encodes ygaC (protein.P0AD53). Encoded protein function: Uncharacterized protein YgaC EcoCyc product frame: EG12201-MONOMER. Genomic coordinates: 2799650-2799994. EcoCyc protein note: Expression of ygaC is upregulated in response to cytoplasmic pH stress and is regulated by Fur .

## Biological Role

Repressed by fur (protein.P0A9A9), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD53|protein.P0AD53]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=ygaC; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygaC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008795,ECOCYC:EG12201,GeneID:947156`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2799650-2799994:-; feature_type=gene
