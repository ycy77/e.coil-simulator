---
entity_id: "reaction.R00442"
entity_type: "reaction"
name: "CTP:RNA cytidylyltransferase (DNA-directed);"
source_database: "KEGG"
source_id: "R00442"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00442"
---

# CTP:RNA cytidylyltransferase (DNA-directed);

`reaction.R00442`

## Static

- Type: `reaction`
- Source: `KEGG:R00442`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CTP + RNA Diphosphate + RNA

## Biological Role

Catalyzed by rpoA (protein.P0A7Z4), rpoZ (protein.P0A800), rpoC (protein.P0A8T7), rpoB (protein.P0A8V2). Substrates: RNA (molecule.C00046), CTP (molecule.C00063). Products: Diphosphate (molecule.C00013), RNA (molecule.C00046).

## Annotation

CTP + RNA <=> Diphosphate + RNA

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0A7Z4|protein.P0A7Z4]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A800|protein.P0A800]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A8T7|protein.P0A8T7]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A8V2|protein.P0A8V2]] `KEGG` `database` - via EC:2.7.7.6
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00063 + C00046 <=> C00013 + C00046
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00063 + C00046 <=> C00013 + C00046
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00063 + C00046 <=> C00013 + C00046
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `KEGG` `database` - C00063 + C00046 <=> C00013 + C00046

## External IDs

- `KEGG:R00442`

## Notes

EQUATION: C00063 + C00046 <=> C00013 + C00046
