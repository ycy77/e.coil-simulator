---
entity_id: "protein.P0AFK4"
entity_type: "protein"
name: "potB"
source_database: "UniProt"
source_id: "P0AFK4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "potB b1125 JW1111"
---

# potB

`protein.P0AFK4`

## Static

- Type: `protein`
- Source: `UniProt:P0AFK4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Required for the activity of the bacterial periplasmic transport system of putrescine and spermidine. potB encodes one of two integral membrane subunits of an ATP-dependent spermidine uptake system; PotB is predicted to contain 6 transmembrane regions . An alternative translation initiation codon 27 nt upstream of the annotated translation initiation site appears to be used .

## Biological Role

Component of spermidine preferential ABC transporter (complex.ecocyc.ABC-24-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Required for the activity of the bacterial periplasmic transport system of putrescine and spermidine.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-24-CPLX|complex.ecocyc.ABC-24-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1125|gene.b1125]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFK4`
- `KEGG:ecj:JW1111;eco:b1125;`
- `GeneID:945692;`
- `GO:GO:0005886; GO:0015417; GO:0015847; GO:0016020; GO:0043190; GO:1903711`

## Notes

Spermidine/putrescine transport system permease protein PotB
