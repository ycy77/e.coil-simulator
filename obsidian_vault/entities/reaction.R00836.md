---
entity_id: "reaction.R00836"
entity_type: "reaction"
name: "UDP-glucose:D-glucose-6-phosphate 1-alpha-D-glucosyltransferase"
source_database: "KEGG"
source_id: "R00836"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00836"
---

# UDP-glucose:D-glucose-6-phosphate 1-alpha-D-glucosyltransferase

`reaction.R00836`

## Static

- Type: `reaction`
- Source: `KEGG:R00836`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-glucose + D-Glucose 6-phosphate UDP + alpha,alpha'-Trehalose 6-phosphate

## Biological Role

Catalyzed by otsA (protein.P31677). Substrates: UDP-glucose (molecule.C00029), D-Glucose 6-phosphate (molecule.C00092). Products: UDP (molecule.C00015), alpha,alpha'-Trehalose 6-phosphate (molecule.C00689).

## Annotation

UDP-glucose + D-Glucose 6-phosphate <=> UDP + alpha,alpha'-Trehalose 6-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P31677|protein.P31677]] `KEGG` `database` - via EC:2.4.1.15
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `KEGG` `database` - C00029 + C00092 <=> C00015 + C00689
- `is_product_of` <-- [[molecule.C00689|molecule.C00689]] `KEGG` `database` - C00029 + C00092 <=> C00015 + C00689
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `KEGG` `database` - C00029 + C00092 <=> C00015 + C00689
- `is_substrate_of` <-- [[molecule.C00092|molecule.C00092]] `KEGG` `database` - C00029 + C00092 <=> C00015 + C00689

## External IDs

- `KEGG:R00836`

## Notes

EQUATION: C00029 + C00092 <=> C00015 + C00689
