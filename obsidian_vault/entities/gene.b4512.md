---
entity_id: "gene.b4512"
entity_type: "gene"
name: "ybdD"
source_database: "NCBI RefSeq"
source_id: "gene-b4512"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4512"
  - "ybdD"
---

# ybdD

`gene.b4512`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4512`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybdD (gene.b4512) is a gene entity. It encodes ybdD (protein.P0AAS9). Encoded protein function: Uncharacterized protein YbdD EcoCyc product frame: MONOMER0-2660. Genomic coordinates: 632182-632379. EcoCyc protein note: The small protein YbdD and the inner membrane protein CstA are implicated in constitutive pyruvate import; ybdD and cstA transposon mutants are enriched in the presence of the toxic pyruvate analog, 3 fluoropyruvate (3FP); ΔybdD and ΔcstA strains avoid 3FP-induced growth inhibition (under pyruvate non-induced conditions) and import significantly less pyruvate than wild-type strains (under pyruvate induced conditions) .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAS9|protein.P0AAS9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285033,ECOCYC:G0-10438,GeneID:949021`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:632182-632379:+; feature_type=gene
