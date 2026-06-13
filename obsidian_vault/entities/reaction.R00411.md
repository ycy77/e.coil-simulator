---
entity_id: "reaction.R00411"
entity_type: "reaction"
name: "N-succinyl-L-glutamate amidohydrolase"
source_database: "KEGG"
source_id: "R00411"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00411"
---

# N-succinyl-L-glutamate amidohydrolase

`reaction.R00411`

## Static

- Type: `reaction`
- Source: `KEGG:R00411`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-Succinyl-L-glutamate + H2O L-Glutamate + Succinate

## Biological Role

Catalyzed by astE (protein.P76215). Substrates: H2O (molecule.C00001), N-Succinyl-L-glutamate (molecule.C05931). Products: L-Glutamate (molecule.C00025), Succinate (molecule.C00042).

## Annotation

N-Succinyl-L-glutamate + H2O <=> L-Glutamate + Succinate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76215|protein.P76215]] `KEGG` `database` - via EC:3.5.1.96
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C05931 + C00001 <=> C00025 + C00042
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `KEGG` `database` - C05931 + C00001 <=> C00025 + C00042
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05931 + C00001 <=> C00025 + C00042
- `is_substrate_of` <-- [[molecule.C05931|molecule.C05931]] `KEGG` `database` - C05931 + C00001 <=> C00025 + C00042

## External IDs

- `KEGG:R00411`

## Notes

EQUATION: C05931 + C00001 <=> C00025 + C00042
