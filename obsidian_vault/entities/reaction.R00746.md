---
entity_id: "reaction.R00746"
entity_type: "reaction"
name: "ethanol:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R00746"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00746"
---

# ethanol:NADP+ oxidoreductase

`reaction.R00746`

## Static

- Type: `reaction`
- Source: `KEGG:R00746`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ethanol + NADP+ Acetaldehyde + NADPH + H+

## Biological Role

Catalyzed by ahr (protein.P27250), yahK (protein.P75691). Substrates: NADP+ (molecule.C00006), Ethanol (molecule.C00469). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Acetaldehyde (molecule.C00084).

## Annotation

Ethanol + NADP+ <=> Acetaldehyde + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P27250|protein.P27250]] `KEGG` `database` - via EC:1.1.1.2
- `catalyzes` <-- [[protein.P75691|protein.P75691]] `KEGG` `database` - via EC:1.1.1.2
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00469 + C00006 <=> C00084 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00469 + C00006 <=> C00084 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `KEGG` `database` - C00469 + C00006 <=> C00084 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00469 + C00006 <=> C00084 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00469|molecule.C00469]] `KEGG` `database` - C00469 + C00006 <=> C00084 + C00005 + C00080

## External IDs

- `KEGG:R00746`

## Notes

EQUATION: C00469 + C00006 <=> C00084 + C00005 + C00080
