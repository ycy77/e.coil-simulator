---
entity_id: "reaction.R00287"
entity_type: "reaction"
name: "UDP-glucose glucophosphohydrolase"
source_database: "KEGG"
source_id: "R00287"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00287"
---

# UDP-glucose glucophosphohydrolase

`reaction.R00287`

## Static

- Type: `reaction`
- Source: `KEGG:R00287`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-glucose + H2O UMP + D-Glucose 1-phosphate

## Biological Role

Catalyzed by ushA (protein.P07024), mazG (protein.P0AEY3). Substrates: H2O (molecule.C00001), UDP-glucose (molecule.C00029). Products: D-Glucose 1-phosphate (molecule.C00103), UMP (molecule.C00105).

## Annotation

UDP-glucose + H2O <=> UMP + D-Glucose 1-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P07024|protein.P07024]] `KEGG` `database` - via EC:3.6.1.45
- `catalyzes` <-- [[protein.P0AEY3|protein.P0AEY3]] `KEGG` `database` - via EC:3.6.1.9
- `is_product_of` <-- [[molecule.C00103|molecule.C00103]] `KEGG` `database` - C00029 + C00001 <=> C00105 + C00103
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `KEGG` `database` - C00029 + C00001 <=> C00105 + C00103
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00029 + C00001 <=> C00105 + C00103
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `KEGG` `database` - C00029 + C00001 <=> C00105 + C00103

## External IDs

- `KEGG:R00287`

## Notes

EQUATION: C00029 + C00001 <=> C00105 + C00103
