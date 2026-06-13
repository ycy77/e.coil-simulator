---
entity_id: "reaction.R00443"
entity_type: "reaction"
name: "UTP:RNA uridylyltransferase"
source_database: "KEGG"
source_id: "R00443"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00443"
---

# UTP:RNA uridylyltransferase

`reaction.R00443`

## Static

- Type: `reaction`
- Source: `KEGG:R00443`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UTP + RNA Diphosphate + RNA

## Biological Role

Catalyzed by rpoA (protein.P0A7Z4), rpoZ (protein.P0A800), rpoC (protein.P0A8T7), rpoB (protein.P0A8V2). Substrates: RNA (molecule.C00046), UTP (molecule.C00075). Products: Diphosphate (molecule.C00013), RNA (molecule.C00046).

## Annotation

UTP + RNA <=> Diphosphate + RNA

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0A7Z4|protein.P0A7Z4]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A800|protein.P0A800]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A8T7|protein.P0A8T7]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A8V2|protein.P0A8V2]] `KEGG` `database` - via EC:2.7.7.6
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00075 + C00046 <=> C00013 + C00046
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00075 + C00046 <=> C00013 + C00046
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00075 + C00046 <=> C00013 + C00046
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `KEGG` `database` - C00075 + C00046 <=> C00013 + C00046

## External IDs

- `KEGG:R00443`

## Notes

EQUATION: C00075 + C00046 <=> C00013 + C00046
