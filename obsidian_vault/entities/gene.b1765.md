---
entity_id: "gene.b1765"
entity_type: "gene"
name: "ydjA"
source_database: "NCBI RefSeq"
source_id: "gene-b1765"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1765"
  - "ydjA"
---

# ydjA

`gene.b1765`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1765`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydjA (gene.b1765) is a gene entity. It encodes ydjA (protein.P0ACY1). Encoded protein function: Putative NAD(P)H nitroreductase YdjA (EC 1.-.-.-) EcoCyc product frame: EG11134-MONOMER. Genomic coordinates: 1848125-1848676. EcoCyc protein note: Crystal structures of YdjA alone and with the FMN cofactor have been solved. The enzyme forms a homodimer in the crystal, and two molecules of FMN are bound at the dimer interface . Overexpressed YdjA does not appear to reduce the prodrugs CB1954 and PR-104A and was used by as a negative control for nitroreductase activity. A ydjA null mutant was reported to produce less hydrogen than wild type under fermentation conditions . No attempt to complement the mutant phenotype with wild-type ydjA was reported.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACY1|protein.P0ACY1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005875,ECOCYC:EG11134,GeneID:945964`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1848125-1848676:-; feature_type=gene
