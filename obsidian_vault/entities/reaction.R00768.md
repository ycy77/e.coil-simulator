---
entity_id: "reaction.R00768"
entity_type: "reaction"
name: "L-glutamine:D-fructose-6-phosphate isomerase (deaminating);"
source_database: "KEGG"
source_id: "R00768"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00768"
---

# L-glutamine:D-fructose-6-phosphate isomerase (deaminating);

`reaction.R00768`

## Static

- Type: `reaction`
- Source: `KEGG:R00768`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Glutamine + D-Fructose 6-phosphate L-Glutamate + D-Glucosamine 6-phosphate

## Biological Role

Catalyzed by glmS (protein.P17169). Substrates: L-Glutamine (molecule.C00064), D-Fructose 6-phosphate (molecule.C00085). Products: L-Glutamate (molecule.C00025), D-Glucosamine 6-phosphate (molecule.C00352).

## Annotation

L-Glutamine + D-Fructose 6-phosphate <=> L-Glutamate + D-Glucosamine 6-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P17169|protein.P17169]] `KEGG` `database` - via EC:2.6.1.16
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00064 + C00085 <=> C00025 + C00352
- `is_product_of` <-- [[molecule.C00352|molecule.C00352]] `KEGG` `database` - C00064 + C00085 <=> C00025 + C00352
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `KEGG` `database` - C00064 + C00085 <=> C00025 + C00352
- `is_substrate_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00064 + C00085 <=> C00025 + C00352

## External IDs

- `KEGG:R00768`

## Notes

EQUATION: C00064 + C00085 <=> C00025 + C00352
