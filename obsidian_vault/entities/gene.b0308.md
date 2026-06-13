---
entity_id: "gene.b0308"
entity_type: "gene"
name: "ykgG"
source_database: "NCBI RefSeq"
source_id: "gene-b0308"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0308"
  - "ykgG"
---

# ykgG

`gene.b0308`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0308`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ykgG (gene.b0308) is a gene entity. It encodes ykgG (protein.P77433). Encoded protein function: Uncharacterized protein YkgG EcoCyc product frame: G6178-MONOMER. Genomic coordinates: 323758-324453. EcoCyc protein note: While their physiological role in E. coli remains unknown, the ykgEFG genes are homologous to newly identified lactate utilization genes in Shewanella oneidensis. Low-copy expression of E. coli ykgEFG in S. oneidensis complements the ability of the Δdld-II ΔlldF double mutant for growth on L-lactate, but not D-lactate . Overexpression of ykgEFG in E. coli restores the ability of a EG10231 dld mutant to grow on D-lactate; crude extracts of an overexpressing strain contain elevated levels of both L- and D-lactate dehydrogenase activity .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77433|protein.P77433]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001062,ECOCYC:G6178,GeneID:945906`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:323758-324453:+; feature_type=gene
