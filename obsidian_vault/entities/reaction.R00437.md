---
entity_id: "reaction.R00437"
entity_type: "reaction"
name: "polyribonucleotide:phosphate adenylyltransferase"
source_database: "KEGG"
source_id: "R00437"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00437"
---

# polyribonucleotide:phosphate adenylyltransferase

`reaction.R00437`

## Static

- Type: `reaction`
- Source: `KEGG:R00437`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNA + Orthophosphate RNA + ADP

## Biological Role

Catalyzed by pnp (protein.P05055). Substrates: Orthophosphate (molecule.C00009), RNA (molecule.C00046). Products: ADP (molecule.C00008), RNA (molecule.C00046).

## Annotation

RNA + Orthophosphate <=> RNA + ADP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P05055|protein.P05055]] `KEGG` `database` - via EC:2.7.7.8
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00008
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00008
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00008
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00008

## External IDs

- `KEGG:R00437`

## Notes

EQUATION: C00046 + C00009 <=> C00046 + C00008
