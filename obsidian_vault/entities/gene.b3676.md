---
entity_id: "gene.b3676"
entity_type: "gene"
name: "yidH"
source_database: "NCBI RefSeq"
source_id: "gene-b3676"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3676"
  - "yidH"
---

# yidH

`gene.b3676`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3676`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yidH (gene.b3676) is a gene entity. It encodes yidH (protein.P0ADM0). Encoded protein function: Inner membrane protein YidH EcoCyc product frame: EG11696-MONOMER. Genomic coordinates: 3855960-3856307. EcoCyc protein note: YidH is an inner membrane protein with three predicted transmembrane domains. The C terminus is located in the periplasm . yidH shows differential codon adaptation, resulting in differential translation efficiency signatures, in aerotolerant compared to obligate anaerobic microbes. It was therefore predicted to play a role in the oxidative stress response. A yidH deletion mutant was shown to be more sensitive than wild-type specifically to hydrogen peroxide exposure, but not other stresses .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADM0|protein.P0ADM0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012018,ECOCYC:EG11696,GeneID:948190`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3855960-3856307:-; feature_type=gene
