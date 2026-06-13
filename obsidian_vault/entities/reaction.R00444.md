---
entity_id: "reaction.R00444"
entity_type: "reaction"
name: "nucleoside-triphosphate:RNA nucleotidyltransferase (DNA-directed);"
source_database: "KEGG"
source_id: "R00444"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00444"
---

# nucleoside-triphosphate:RNA nucleotidyltransferase (DNA-directed);

`reaction.R00444`

## Static

- Type: `reaction`
- Source: `KEGG:R00444`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nucleoside triphosphate + RNA Diphosphate + RNA

## Biological Role

Catalyzed by rpoA (protein.P0A7Z4), rpoZ (protein.P0A800), rpoC (protein.P0A8T7), rpoB (protein.P0A8V2). Substrates: RNA (molecule.C00046). Products: Diphosphate (molecule.C00013), RNA (molecule.C00046).

## Annotation

Nucleoside triphosphate + RNA <=> Diphosphate + RNA

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A7Z4|protein.P0A7Z4]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A800|protein.P0A800]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A8T7|protein.P0A8T7]] `KEGG` `database` - via EC:2.7.7.6
- `catalyzes` <-- [[protein.P0A8V2|protein.P0A8V2]] `KEGG` `database` - via EC:2.7.7.6
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00201 + C00046 <=> C00013 + C00046
- `is_product_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00201 + C00046 <=> C00013 + C00046
- `is_substrate_of` <-- [[molecule.C00046|molecule.C00046]] `KEGG` `database` - C00201 + C00046 <=> C00013 + C00046

## External IDs

- `KEGG:R00444`

## Notes

EQUATION: C00201 + C00046 <=> C00013 + C00046
