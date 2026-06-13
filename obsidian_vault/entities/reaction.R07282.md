---
entity_id: "reaction.R07282"
entity_type: "reaction"
name: "polyribonucleotide:phosphate nucleotidyltransferase"
source_database: "KEGG"
source_id: "R07282"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07282"
---

# polyribonucleotide:phosphate nucleotidyltransferase

`reaction.R07282`

## Static

- Type: `reaction`
- Source: `KEGG:R07282`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNA + Orthophosphate RNA + NDP

## Biological Role

Catalyzed by pnp (protein.P05055). Substrates: Orthophosphate (molecule.C00009), RNA (molecule.C00046). Products: RNA (molecule.C00046).

## Annotation

RNA + Orthophosphate <=> RNA + NDP

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P05055|protein.P05055]] `KEGG` `database` - via EC:2.7.7.8
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00454
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00454
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00454

## External IDs

- `KEGG:R07282`

## Notes

EQUATION: C00046 + C00009 <=> C00046 + C00454
