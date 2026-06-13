---
entity_id: "reaction.R13097"
entity_type: "reaction"
name: "N-acetyl-glutamate racemase"
source_database: "KEGG"
source_id: "R13097"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R13097"
---

# N-acetyl-glutamate racemase

`reaction.R13097`

## Static

- Type: `reaction`
- Source: `KEGG:R13097`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-Acetyl-D-glutamate N-Acetyl-L-glutamate

## Biological Role

Catalyzed by ycjG (protein.P51981). Substrates: N-Acetyl-D-glutamate (molecule.C22611). Products: N-Acetyl-L-glutamate (molecule.C00624).

## Annotation

N-Acetyl-D-glutamate <=> N-Acetyl-L-glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P51981|protein.P51981]] `KEGG` `database` - via EC:5.1.1.25
- `is_product_of` <-- [[molecule.C00624|molecule.C00624]] `KEGG` `database` - C22611 <=> C00624
- `is_substrate_of` <-- [[molecule.C22611|molecule.C22611]] `KEGG` `database` - C22611 <=> C00624

## External IDs

- `KEGG:R13097`

## Notes

EQUATION: C22611 <=> C00624
