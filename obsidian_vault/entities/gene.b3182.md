---
entity_id: "gene.b3182"
entity_type: "gene"
name: "dacB"
source_database: "NCBI RefSeq"
source_id: "gene-b3182"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3182"
  - "dacB"
---

# dacB

`gene.b3182`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3182`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dacB (gene.b3182) is a gene entity. It encodes dacB (protein.P24228). Encoded protein function: FUNCTION: Not involved in transpeptidation but exclusively catalyzes a DD-carboxypeptidase and DD-endopeptidase reaction. {ECO:0000269|PubMed:2046551}. EcoCyc product frame: EG10202-MONOMER. Genomic coordinates: 3328963-3330396.

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24228|protein.P24228]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010458,ECOCYC:EG10202,GeneID:947693`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3328963-3330396:+; feature_type=gene
