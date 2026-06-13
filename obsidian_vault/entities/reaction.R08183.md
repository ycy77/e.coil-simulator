---
entity_id: "reaction.R08183"
entity_type: "reaction"
name: "R08183"
source_database: "KEGG"
source_id: "R08183"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08183"
---

# R08183

`reaction.R08183`

## Static

- Type: `reaction`
- Source: `KEGG:R08183`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Arachidonyl-CoA + H2O CoA + Arachidonate

## Biological Role

Catalyzed by tesA (protein.P0ADA1). Substrates: H2O (molecule.C00001), Arachidonyl-CoA (molecule.C02249). Products: CoA (molecule.C00010), Arachidonate (molecule.C00219).

## Annotation

Arachidonyl-CoA + H2O <=> CoA + Arachidonate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ADA1|protein.P0ADA1]] `KEGG` `database` - via EC:3.1.2.2
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C02249 + C00001 <=> C00010 + C00219
- `is_product_of` <-- [[molecule.C00219|molecule.C00219]] `KEGG` `database` - C02249 + C00001 <=> C00010 + C00219
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C02249 + C00001 <=> C00010 + C00219
- `is_substrate_of` <-- [[molecule.C02249|molecule.C02249]] `KEGG` `database` - C02249 + C00001 <=> C00010 + C00219

## External IDs

- `KEGG:R08183`

## Notes

EQUATION: C02249 + C00001 <=> C00010 + C00219
