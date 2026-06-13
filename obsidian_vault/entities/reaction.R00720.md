---
entity_id: "reaction.R00720"
entity_type: "reaction"
name: "inosine 5'-triphosphate pyrophosphohydrolase"
source_database: "KEGG"
source_id: "R00720"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00720"
---

# inosine 5'-triphosphate pyrophosphohydrolase

`reaction.R00720`

## Static

- Type: `reaction`
- Source: `KEGG:R00720`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ITP + H2O IMP + Diphosphate

## Biological Role

Catalyzed by rdgB (protein.P52061). Substrates: H2O (molecule.C00001), ITP (molecule.C00081). Products: Diphosphate (molecule.C00013), IMP (molecule.C00130).

## Annotation

ITP + H2O <=> IMP + Diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P52061|protein.P52061]] `KEGG` `database` - via EC:3.6.1.66
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00081 + C00001 <=> C00130 + C00013
- `is_product_of` <-- [[molecule.C00130|molecule.C00130]] `KEGG` `database` - C00081 + C00001 <=> C00130 + C00013
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00081 + C00001 <=> C00130 + C00013
- `is_substrate_of` <-- [[molecule.C00081|molecule.C00081]] `KEGG` `database` - C00081 + C00001 <=> C00130 + C00013

## External IDs

- `KEGG:R00720`

## Notes

EQUATION: C00081 + C00001 <=> C00130 + C00013
