---
entity_id: "reaction.R00226"
entity_type: "reaction"
name: "pyruvate:pyruvate acetaldehydetransferase (decarboxylating);"
source_database: "KEGG"
source_id: "R00226"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00226"
---

# pyruvate:pyruvate acetaldehydetransferase (decarboxylating);

`reaction.R00226`

## Static

- Type: `reaction`
- Source: `KEGG:R00226`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-2-Acetolactate + CO2 2 Pyruvate

## Biological Role

Catalyzed by ilvI (protein.P00893), ilvH (protein.P00894), ilvB (protein.P08142), ilvN (protein.P0ADF8), ilvM (protein.P0ADG1). Substrates: CO2 (molecule.C00011), (S)-2-Acetolactate (molecule.C06010). Products: Pyruvate (molecule.C00022).

## Annotation

(S)-2-Acetolactate + CO2 <=> 2 Pyruvate

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P00893|protein.P00893]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P00894|protein.P00894]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P08142|protein.P08142]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P0ADF8|protein.P0ADF8]] `KEGG` `database` - via EC:2.2.1.6
- `catalyzes` <-- [[protein.P0ADG1|protein.P0ADG1]] `KEGG` `database` - via EC:2.2.1.6
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C06010 + C00011 <=> 2 C00022
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C06010 + C00011 <=> 2 C00022
- `is_substrate_of` <-- [[molecule.C06010|molecule.C06010]] `KEGG` `database` - C06010 + C00011 <=> 2 C00022

## External IDs

- `KEGG:R00226`

## Notes

EQUATION: C06010 + C00011 <=> 2 C00022
