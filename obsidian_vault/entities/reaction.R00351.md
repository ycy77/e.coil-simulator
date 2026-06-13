---
entity_id: "reaction.R00351"
entity_type: "reaction"
name: "acetyl-CoA:oxaloacetate C-acetyltransferase (thioester-hydrolysing)"
source_database: "KEGG"
source_id: "R00351"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00351"
---

# acetyl-CoA:oxaloacetate C-acetyltransferase (thioester-hydrolysing)

`reaction.R00351`

## Static

- Type: `reaction`
- Source: `KEGG:R00351`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Citrate + CoA Acetyl-CoA + H2O + Oxaloacetate

## Biological Role

Catalyzed by gltA (protein.P0ABH7), prpC (protein.P31660). Substrates: CoA (molecule.C00010), Citrate (molecule.C00158). Products: H2O (molecule.C00001), Acetyl-CoA (molecule.C00024), Oxaloacetate (molecule.C00036).

## Annotation

Citrate + CoA <=> Acetyl-CoA + H2O + Oxaloacetate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0ABH7|protein.P0ABH7]] `KEGG` `database` - via EC:2.3.3.1
- `catalyzes` <-- [[protein.P31660|protein.P31660]] `KEGG` `database` - via EC:2.3.3.5
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00158 + C00010 <=> C00024 + C00001 + C00036
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00158 + C00010 <=> C00024 + C00001 + C00036
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00158 + C00010 <=> C00024 + C00001 + C00036
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00158 + C00010 <=> C00024 + C00001 + C00036
- `is_substrate_of` <-- [[molecule.C00158|molecule.C00158]] `KEGG` `database` - C00158 + C00010 <=> C00024 + C00001 + C00036

## External IDs

- `KEGG:R00351`

## Notes

EQUATION: C00158 + C00010 <=> C00024 + C00001 + C00036
