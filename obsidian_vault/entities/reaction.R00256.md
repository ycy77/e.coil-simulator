---
entity_id: "reaction.R00256"
entity_type: "reaction"
name: "L-glutamine amidohydrolase"
source_database: "KEGG"
source_id: "R00256"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00256"
---

# L-glutamine amidohydrolase

`reaction.R00256`

## Static

- Type: `reaction`
- Source: `KEGG:R00256`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Glutamine + H2O L-Glutamate + Ammonia

## Biological Role

Catalyzed by pabA (protein.P00903), carB (protein.P00968), guaA (protein.P04079), pabB (protein.P05041), gltB (protein.P09831), gltD (protein.P09832), carA (protein.P0A6F1), glsA2 (protein.P0A6W0), and 5 more. Substrates: H2O (molecule.C00001), L-Glutamine (molecule.C00064). Products: Ammonia (molecule.C00014), L-Glutamate (molecule.C00025).

## Annotation

L-Glutamine + H2O <=> L-Glutamate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (17)

- `catalyzes` <-- [[protein.P00903|protein.P00903]] `KEGG` `database` - via EC:2.6.1.85
- `catalyzes` <-- [[protein.P00968|protein.P00968]] `KEGG` `database` - via EC:6.3.5.5
- `catalyzes` <-- [[protein.P04079|protein.P04079]] `KEGG` `database` - via EC:6.3.5.2
- `catalyzes` <-- [[protein.P05041|protein.P05041]] `KEGG` `database` - via EC:2.6.1.85
- `catalyzes` <-- [[protein.P09831|protein.P09831]] `KEGG` `database` - via EC:1.4.1.13
- `catalyzes` <-- [[protein.P09832|protein.P09832]] `KEGG` `database` - via EC:1.4.1.13
- `catalyzes` <-- [[protein.P0A6F1|protein.P0A6F1]] `KEGG` `database` - via EC:6.3.5.5
- `catalyzes` <-- [[protein.P0A6W0|protein.P0A6W0]] `KEGG` `database` - via EC:3.5.1.2
- `catalyzes` <-- [[protein.P0A7E5|protein.P0A7E5]] `KEGG` `database` - via EC:6.3.4.2
- `catalyzes` <-- [[protein.P22106|protein.P22106]] `KEGG` `database` - via EC:6.3.5.4
- `catalyzes` <-- [[protein.P60595|protein.P60595]] `KEGG` `database` - via EC:4.3.2.10
- `catalyzes` <-- [[protein.P60664|protein.P60664]] `KEGG` `database` - via EC:4.3.2.10
- `catalyzes` <-- [[protein.P77454|protein.P77454]] `KEGG` `database` - via EC:3.5.1.2
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00064 + C00001 <=> C00025 + C00014
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00064 + C00001 <=> C00025 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00064 + C00001 <=> C00025 + C00014
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `KEGG` `database` - C00064 + C00001 <=> C00025 + C00014

## External IDs

- `KEGG:R00256`

## Notes

EQUATION: C00064 + C00001 <=> C00025 + C00014
