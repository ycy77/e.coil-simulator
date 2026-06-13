---
entity_id: "gene.b3690"
entity_type: "gene"
name: "cbrA"
source_database: "NCBI RefSeq"
source_id: "gene-b3690"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3690"
  - "cbrA"
---

# cbrA

`gene.b3690`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3690`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cbrA (gene.b3690) is a gene entity. It encodes cbrA (protein.P31456). Encoded protein function: Protein CbrA (CreB-regulated gene A protein) EcoCyc product frame: EG11714-MONOMER. EcoCyc synonyms: yidS. Genomic coordinates: 3869377-3870441. EcoCyc protein note: Overproduction of CbrA confers resistance to colicin M . Transcription of cbrA is induced by the CreBC two-component system by minimal media growth conditions , and in a luxS mutant . In a phenotype microarray measuring respiration, a cbrA mutant shows higher resistance to hydroxylamine and hypersensitivity to ofloxacin, a lipophilic chelator, and an ionophore . CbrA: "creB-regulated A"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31456|protein.P31456]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012068,ECOCYC:EG11714,GeneID:948197`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3869377-3870441:+; feature_type=gene
