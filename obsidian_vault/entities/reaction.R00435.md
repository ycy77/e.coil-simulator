---
entity_id: "reaction.R00435"
entity_type: "reaction"
name: "ATP:polynucleotide adenylyltransferase;"
source_database: "KEGG"
source_id: "R00435"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00435"
---

# ATP:polynucleotide adenylyltransferase;

`reaction.R00435`

## Static

- Type: `reaction`
- Source: `KEGG:R00435`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + RNA Diphosphate + RNA

## Biological Role

Catalyzed by rpoA (protein.P0A7Z4), rpoZ (protein.P0A800), rpoC (protein.P0A8T7), rpoB (protein.P0A8V2), pcnB (protein.P0ABF1). Substrates: ATP (molecule.C00002), RNA (molecule.C00046). Products: Diphosphate (molecule.C00013), RNA (molecule.C00046).

## Annotation

ATP + RNA <=> Diphosphate + RNA

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A7Z4|protein.P0A7Z4]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A800|protein.P0A800]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A8T7|protein.P0A8T7]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A8V2|protein.P0A8V2]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0ABF1|protein.P0ABF1]] `KEGG` `database` - via EC:2.7.7.19
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00046 <=> C00013 + C00046
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00002 + C00046 <=> C00013 + C00046
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00046 <=> C00013 + C00046
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00002 + C00046 <=> C00013 + C00046

## External IDs

- `KEGG:R00435`

## Notes

EQUATION: C00002 + C00046 <=> C00013 + C00046
