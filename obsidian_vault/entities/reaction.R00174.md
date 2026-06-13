---
entity_id: "reaction.R00174"
entity_type: "reaction"
name: "ATP:pyridoxal 5'-phosphotransferase"
source_database: "KEGG"
source_id: "R00174"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00174"
---

# ATP:pyridoxal 5'-phosphotransferase

`reaction.R00174`

## Static

- Type: `reaction`
- Source: `KEGG:R00174`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Pyridoxal ADP + Pyridoxal phosphate

## Biological Role

Catalyzed by pdxK (protein.P40191), pdxY (protein.P77150). Substrates: ATP (molecule.C00002), Pyridoxal (molecule.C00250). Products: ADP (molecule.C00008), Pyridoxal phosphate (molecule.C00018).

## Annotation

ATP + Pyridoxal <=> ADP + Pyridoxal phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P40191|protein.P40191]] `KEGG` `database` - via EC:2.7.1.35
- `catalyzes` <-- [[protein.P77150|protein.P77150]] `KEGG` `database` - via EC:2.7.1.35
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00250 <=> C00008 + C00018
- `is_product_of` <-- [[molecule.C00018|molecule.C00018]] `KEGG` `database` - C00002 + C00250 <=> C00008 + C00018
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00250 <=> C00008 + C00018
- `is_substrate_of` <-- [[molecule.C00250|molecule.C00250]] `KEGG` `database` - C00002 + C00250 <=> C00008 + C00018

## External IDs

- `KEGG:R00174`

## Notes

EQUATION: C00002 + C00250 <=> C00008 + C00018
