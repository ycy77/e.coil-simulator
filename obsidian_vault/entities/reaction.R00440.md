---
entity_id: "reaction.R00440"
entity_type: "reaction"
name: "polyribonucleotide:phosphate cytidylyltransferase"
source_database: "KEGG"
source_id: "R00440"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00440"
---

# polyribonucleotide:phosphate cytidylyltransferase

`reaction.R00440`

## Static

- Type: `reaction`
- Source: `KEGG:R00440`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNA + Orthophosphate RNA + CDP

## Biological Role

Catalyzed by pnp (protein.P05055). Substrates: Orthophosphate (molecule.C00009), RNA (molecule.C00046). Products: RNA (molecule.C00046), CDP (molecule.C00112).

## Annotation

RNA + Orthophosphate <=> RNA + CDP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P05055|protein.P05055]] `KEGG` `database` - via EC:2.7.7.8
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00112
- `is_product_of` <-- [[molecule.C00112|molecule.C00112]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00112
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00112
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00112

## External IDs

- `KEGG:R00440`

## Notes

EQUATION: C00046 + C00009 <=> C00046 + C00112
