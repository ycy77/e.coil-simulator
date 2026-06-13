---
entity_id: "reaction.R00190"
entity_type: "reaction"
name: "AMP:diphosphate phospho-D-ribosyltransferase"
source_database: "KEGG"
source_id: "R00190"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00190"
---

# AMP:diphosphate phospho-D-ribosyltransferase

`reaction.R00190`

## Static

- Type: `reaction`
- Source: `KEGG:R00190`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AMP + Diphosphate Adenine + 5-Phospho-alpha-D-ribose 1-diphosphate

## Biological Role

Catalyzed by apt (protein.P69503). Substrates: Diphosphate (molecule.C00013), AMP (molecule.C00020). Products: 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), Adenine (molecule.C00147).

## Annotation

AMP + Diphosphate <=> Adenine + 5-Phospho-alpha-D-ribose 1-diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P69503|protein.P69503]] `KEGG` `database` - via EC:2.4.2.7
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `KEGG` `database` - C00020 + C00013 <=> C00147 + C00119
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `KEGG` `database` - C00020 + C00013 <=> C00147 + C00119
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00020 + C00013 <=> C00147 + C00119
- `is_substrate_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00020 + C00013 <=> C00147 + C00119

## External IDs

- `KEGG:R00190`

## Notes

EQUATION: C00020 + C00013 <=> C00147 + C00119
