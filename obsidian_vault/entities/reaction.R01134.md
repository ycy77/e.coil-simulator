---
entity_id: "reaction.R01134"
entity_type: "reaction"
name: "inosine-5'-phosphate:NADP+ oxidoreductase (aminating);"
source_database: "KEGG"
source_id: "R01134"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01134"
---

# inosine-5'-phosphate:NADP+ oxidoreductase (aminating);

`reaction.R01134`

## Static

- Type: `reaction`
- Source: `KEGG:R01134`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

IMP + Ammonia + NADP+ GMP + NADPH + H+

## Biological Role

Catalyzed by guaC (protein.P60560). Substrates: NADP+ (molecule.C00006), Ammonia (molecule.C00014), IMP (molecule.C00130). Products: NADPH (molecule.C00005), H+ (molecule.C00080), GMP (molecule.C00144).

## Annotation

IMP + Ammonia + NADP+ <=> GMP + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P60560|protein.P60560]] `KEGG` `database` - via EC:1.7.1.7
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00130 + C00014 + C00006 <=> C00144 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00130 + C00014 + C00006 <=> C00144 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `KEGG` `database` - C00130 + C00014 + C00006 <=> C00144 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00130 + C00014 + C00006 <=> C00144 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00130 + C00014 + C00006 <=> C00144 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00130|molecule.C00130]] `KEGG` `database` - C00130 + C00014 + C00006 <=> C00144 + C00005 + C00080

## External IDs

- `KEGG:R01134`

## Notes

EQUATION: C00130 + C00014 + C00006 <=> C00144 + C00005 + C00080
