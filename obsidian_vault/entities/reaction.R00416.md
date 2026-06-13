---
entity_id: "reaction.R00416"
entity_type: "reaction"
name: "UTP:N-acetyl-alpha-D-glucosamine-1-phosphate uridylyltransferase"
source_database: "KEGG"
source_id: "R00416"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00416"
---

# UTP:N-acetyl-alpha-D-glucosamine-1-phosphate uridylyltransferase

`reaction.R00416`

## Static

- Type: `reaction`
- Source: `KEGG:R00416`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UTP + N-Acetyl-alpha-D-glucosamine 1-phosphate Diphosphate + UDP-N-acetyl-alpha-D-glucosamine

## Biological Role

Catalyzed by glmU (protein.P0ACC7). Substrates: UTP (molecule.C00075), N-Acetyl-alpha-D-glucosamine 1-phosphate (molecule.C04501). Products: Diphosphate (molecule.C00013), UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043).

## Annotation

UTP + N-Acetyl-alpha-D-glucosamine 1-phosphate <=> Diphosphate + UDP-N-acetyl-alpha-D-glucosamine

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ACC7|protein.P0ACC7]] `KEGG` `database` - via EC:2.7.7.23
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00075 + C04501 <=> C00013 + C00043
- `is_product_of` <-- [[molecule.C00043|molecule.C00043]] `KEGG` `database` - C00075 + C04501 <=> C00013 + C00043
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `KEGG` `database` - C00075 + C04501 <=> C00013 + C00043
- `is_substrate_of` <-- [[molecule.C04501|molecule.C04501]] `KEGG` `database` - C00075 + C04501 <=> C00013 + C00043

## External IDs

- `KEGG:R00416`

## Notes

EQUATION: C00075 + C04501 <=> C00013 + C00043
