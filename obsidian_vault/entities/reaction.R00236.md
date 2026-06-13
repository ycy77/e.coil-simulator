---
entity_id: "reaction.R00236"
entity_type: "reaction"
name: "acetyl adenylate:CoA acetyltransferase"
source_database: "KEGG"
source_id: "R00236"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00236"
---

# acetyl adenylate:CoA acetyltransferase

`reaction.R00236`

## Static

- Type: `reaction`
- Source: `KEGG:R00236`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl adenylate + CoA AMP + Acetyl-CoA

## Biological Role

Catalyzed by acs (protein.P27550). Substrates: CoA (molecule.C00010), Acetyl adenylate (molecule.C05993). Products: AMP (molecule.C00020), Acetyl-CoA (molecule.C00024).

## Annotation

Acetyl adenylate + CoA <=> AMP + Acetyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27550|protein.P27550]] `KEGG` `database` - via EC:6.2.1.1
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C05993 + C00010 <=> C00020 + C00024
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C05993 + C00010 <=> C00020 + C00024
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C05993 + C00010 <=> C00020 + C00024
- `is_substrate_of` <-- [[molecule.C05993|molecule.C05993]] `KEGG` `database` - C05993 + C00010 <=> C00020 + C00024

## External IDs

- `KEGG:R00236`

## Notes

EQUATION: C05993 + C00010 <=> C00020 + C00024
