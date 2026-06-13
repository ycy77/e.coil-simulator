---
entity_id: "reaction.R00439"
entity_type: "reaction"
name: "polyribonucleotide:phosphate guanylyltransferase"
source_database: "KEGG"
source_id: "R00439"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00439"
---

# polyribonucleotide:phosphate guanylyltransferase

`reaction.R00439`

## Static

- Type: `reaction`
- Source: `KEGG:R00439`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNA + Orthophosphate RNA + GDP

## Biological Role

Catalyzed by pnp (protein.P05055). Substrates: Orthophosphate (molecule.C00009), RNA (molecule.C00046). Products: GDP (molecule.C00035), RNA (molecule.C00046).

## Annotation

RNA + Orthophosphate <=> RNA + GDP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P05055|protein.P05055]] `KEGG` `database` - via EC:2.7.7.8
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00035
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00035
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00035
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00046 + C00009 <=> C00046 + C00035

## External IDs

- `KEGG:R00439`

## Notes

EQUATION: C00046 + C00009 <=> C00046 + C00035
