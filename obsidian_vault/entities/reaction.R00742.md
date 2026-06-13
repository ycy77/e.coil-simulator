---
entity_id: "reaction.R00742"
entity_type: "reaction"
name: "acetyl-CoA:carbon-dioxide ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R00742"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00742"
---

# acetyl-CoA:carbon-dioxide ligase (ADP-forming)

`reaction.R00742`

## Static

- Type: `reaction`
- Source: `KEGG:R00742`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Acetyl-CoA + HCO3- ADP + Orthophosphate + Malonyl-CoA

## Biological Role

Catalyzed by accD (protein.P0A9Q5), accA (protein.P0ABD5), accC (protein.P24182). Substrates: ATP (molecule.C00002), Acetyl-CoA (molecule.C00024), HCO3- (molecule.C00288). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), Malonyl-CoA (molecule.C00083).

## Annotation

ATP + Acetyl-CoA + HCO3- <=> ADP + Orthophosphate + Malonyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A9Q5|protein.P0A9Q5]] `KEGG` `database` - via EC:6.4.1.2
- `catalyzes` <-- [[protein.P0ABD5|protein.P0ABD5]] `KEGG` `database` - via EC:6.4.1.2
- `catalyzes` <-- [[protein.P24182|protein.P24182]] `KEGG` `database` - via EC:6.4.1.2
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00024 + C00288 <=> C00008 + C00009 + C00083
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C00024 + C00288 <=> C00008 + C00009 + C00083
- `is_product_of` <-- [[molecule.C00083|molecule.C00083]] `KEGG` `database` - C00002 + C00024 + C00288 <=> C00008 + C00009 + C00083
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00024 + C00288 <=> C00008 + C00009 + C00083
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00002 + C00024 + C00288 <=> C00008 + C00009 + C00083
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `KEGG` `database` - C00002 + C00024 + C00288 <=> C00008 + C00009 + C00083

## External IDs

- `KEGG:R00742`

## Notes

EQUATION: C00002 + C00024 + C00288 <=> C00008 + C00009 + C00083
