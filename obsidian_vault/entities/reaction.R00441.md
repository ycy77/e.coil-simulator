---
entity_id: "reaction.R00441"
entity_type: "reaction"
name: "GTP:RNA guanylyltransferase (DNA-directed);"
source_database: "KEGG"
source_id: "R00441"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00441"
---

# GTP:RNA guanylyltransferase (DNA-directed);

`reaction.R00441`

## Static

- Type: `reaction`
- Source: `KEGG:R00441`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + RNA Diphosphate + RNA

## Biological Role

Catalyzed by rpoA (protein.P0A7Z4), rpoZ (protein.P0A800), rpoC (protein.P0A8T7), rpoB (protein.P0A8V2). Substrates: GTP (molecule.C00044), RNA (molecule.C00046). Products: Diphosphate (molecule.C00013), RNA (molecule.C00046).

## Annotation

GTP + RNA <=> Diphosphate + RNA

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0A7Z4|protein.P0A7Z4]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A800|protein.P0A800]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A8T7|protein.P0A8T7]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A8V2|protein.P0A8V2]] `KEGG` `database` - via EC:2.7.7.6
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00044 + C00046 <=> C00013 + C00046
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00044 + C00046 <=> C00013 + C00046
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00044 + C00046 <=> C00013 + C00046
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00044 + C00046 <=> C00013 + C00046

## External IDs

- `KEGG:R00441`

## Notes

EQUATION: C00044 + C00046 <=> C00013 + C00046
