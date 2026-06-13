---
entity_id: "protein.P0DPC7"
entity_type: "protein"
name: "rseD"
source_database: "UniProt"
source_id: "P0DPC7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rseD orf51 b4725"
---

# rseD

`protein.P0DPC7`

## Static

- Type: `protein`
- Source: `UniProt:P0DPC7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A short protein whose stop codon overlaps with the start codon of downstream rpoE; a premature stop codon at position 12 results in decreased expression of ECF sigma factor RpoE, thus they are translationally coupled (PubMed:28924029). {ECO:0000269|PubMed:28924029}. Translation of rpoE, which encodes the extracytoplasmic stress response sigma factor σE, is coupled to the translation of the rpoE leader peptide, RseD. If translational coupling is eliminated, translation of rpoE is reduced by more than 50% .

## Annotation

FUNCTION: A short protein whose stop codon overlaps with the start codon of downstream rpoE; a premature stop codon at position 12 results in decreased expression of ECF sigma factor RpoE, thus they are translationally coupled (PubMed:28924029). {ECO:0000269|PubMed:28924029}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4725|gene.b4725]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DPC7`
- `KEGG:ecoc:C3026_14255;`
- `GeneID:93774517;`
- `GO:GO:0006417`

## Notes

rpoE leader peptide
