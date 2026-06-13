---
entity_id: "reaction.R00150"
entity_type: "reaction"
name: "ATP:carbamate phosphotransferase"
source_database: "KEGG"
source_id: "R00150"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00150"
---

# ATP:carbamate phosphotransferase

`reaction.R00150`

## Static

- Type: `reaction`
- Source: `KEGG:R00150`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Ammonia + HCO3- ADP + Carbamoyl phosphate + H2O

## Biological Role

Catalyzed by allK (protein.P37306), yahI (protein.P77624), yqeA (protein.Q46807). Substrates: ATP (molecule.C00002), Ammonia (molecule.C00014), HCO3- (molecule.C00288). Products: H2O (molecule.C00001), ADP (molecule.C00008), Carbamoyl phosphate (molecule.C00169).

## Annotation

ATP + Ammonia + HCO3- <=> ADP + Carbamoyl phosphate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P37306|protein.P37306]] `KEGG` `database` - via EC:2.7.2.2
- `catalyzes` <-- [[protein.P77624|protein.P77624]] `KEGG` `database` - via EC:2.7.2.2
- `catalyzes` <-- [[protein.Q46807|protein.Q46807]] `KEGG` `database` - via EC:2.7.2.2
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00002 + C00014 + C00288 <=> C00008 + C00169 + C00001
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00014 + C00288 <=> C00008 + C00169 + C00001
- `is_product_of` <-- [[molecule.C00169|molecule.C00169]] `KEGG` `database` - C00002 + C00014 + C00288 <=> C00008 + C00169 + C00001
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00014 + C00288 <=> C00008 + C00169 + C00001
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00002 + C00014 + C00288 <=> C00008 + C00169 + C00001
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `KEGG` `database` - C00002 + C00014 + C00288 <=> C00008 + C00169 + C00001

## External IDs

- `KEGG:R00150`

## Notes

EQUATION: C00002 + C00014 + C00288 <=> C00008 + C00169 + C00001
