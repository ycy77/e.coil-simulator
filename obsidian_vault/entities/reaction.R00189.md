---
entity_id: "reaction.R00189"
entity_type: "reaction"
name: "deamido-NAD+:ammonia ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R00189"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00189"
---

# deamido-NAD+:ammonia ligase (AMP-forming)

`reaction.R00189`

## Static

- Type: `reaction`
- Source: `KEGG:R00189`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Deamino-NAD+ + Ammonia AMP + Diphosphate + NAD+

## Biological Role

Catalyzed by nadE (protein.P18843). Substrates: ATP (molecule.C00002), Ammonia (molecule.C00014), Deamino-NAD+ (molecule.C00857). Products: NAD+ (molecule.C00003), Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

ATP + Deamino-NAD+ + Ammonia <=> AMP + Diphosphate + NAD+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P18843|protein.P18843]] `KEGG` `database` - via EC:6.3.1.5
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00002 + C00857 + C00014 <=> C00020 + C00013 + C00003
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00857 + C00014 <=> C00020 + C00013 + C00003
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00857 + C00014 <=> C00020 + C00013 + C00003
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00857 + C00014 <=> C00020 + C00013 + C00003
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00002 + C00857 + C00014 <=> C00020 + C00013 + C00003
- `is_substrate_of` <-- [[molecule.C00857|molecule.C00857]] `KEGG` `database` - C00002 + C00857 + C00014 <=> C00020 + C00013 + C00003

## External IDs

- `KEGG:R00189`

## Notes

EQUATION: C00002 + C00857 + C00014 <=> C00020 + C00013 + C00003
