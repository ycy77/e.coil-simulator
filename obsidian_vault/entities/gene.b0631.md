---
entity_id: "gene.b0631"
entity_type: "gene"
name: "ybeD"
source_database: "NCBI RefSeq"
source_id: "gene-b0631"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0631"
  - "ybeD"
---

# ybeD

`gene.b0631`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0631`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybeD (gene.b0631) is a gene entity. It encodes ybeD (protein.P0A8J4). Encoded protein function: UPF0250 protein YbeD EcoCyc product frame: EG11592-MONOMER. Genomic coordinates: 662379-662642. EcoCyc protein note: YbeD is involved in the response to high-temperature stress. A ΔybeD strain grows more slowly and to a lower cell density than wild type, while overexpression of ybeD enhances growth at 46°C and alleviates the growth phenotypes of several chaperone mutants . A solution structure of YbeD shows structural similarity to small-molecule binding ACT domains . In E. coli BL21(DE3), ybeD expression increases significantly after a shift from 37°C to 42°C or 46°C .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8J4|protein.P0A8J4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002162,ECOCYC:EG11592,GeneID:945220`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:662379-662642:-; feature_type=gene
