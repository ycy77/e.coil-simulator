---
entity_id: "reaction.R00438"
entity_type: "reaction"
name: "polyribonucleotide:phosphate uridylyltransferase"
source_database: "KEGG"
source_id: "R00438"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00438"
---

# polyribonucleotide:phosphate uridylyltransferase

`reaction.R00438`

## Static

- Type: `reaction`
- Source: `KEGG:R00438`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNA + Orthophosphate RNA + UDP

## Biological Role

Catalyzed by pnp (protein.P05055). Substrates: Orthophosphate (molecule.C00009), RNA (molecule.C00046). Products: UDP (molecule.C00015), RNA (molecule.C00046).

## Annotation

RNA + Orthophosphate <=> RNA + UDP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P05055|protein.P05055]] `KEGG` `database` - via EC:2.7.7.8
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00015
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00015
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00015
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00015

## External IDs

- `KEGG:R00438`

## Notes

EQUATION: C00046 + C00009 <=> C00046 + C00015
