---
entity_id: "reaction.R00832"
entity_type: "reaction"
name: "succinyl-CoA:L-arginine N2-succinyltransferase"
source_database: "KEGG"
source_id: "R00832"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00832"
---

# succinyl-CoA:L-arginine N2-succinyltransferase

`reaction.R00832`

## Static

- Type: `reaction`
- Source: `KEGG:R00832`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Succinyl-CoA + L-Arginine CoA + N2-Succinyl-L-arginine

## Biological Role

Catalyzed by astA (protein.P0AE37). Substrates: L-Arginine (molecule.C00062), Succinyl-CoA (molecule.C00091). Products: CoA (molecule.C00010), N2-Succinyl-L-arginine (molecule.C03296).

## Annotation

Succinyl-CoA + L-Arginine <=> CoA + N2-Succinyl-L-arginine

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AE37|protein.P0AE37]] `KEGG` `database` - via EC:2.3.1.109
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00091 + C00062 <=> C00010 + C03296
- `is_product_of` <-- [[molecule.C03296|molecule.C03296]] `KEGG` `database` - C00091 + C00062 <=> C00010 + C03296
- `is_substrate_of` <-- [[molecule.C00062|molecule.C00062]] `KEGG` `database` - C00091 + C00062 <=> C00010 + C03296
- `is_substrate_of` <-- [[molecule.C00091|molecule.C00091]] `KEGG` `database` - C00091 + C00062 <=> C00010 + C03296

## External IDs

- `KEGG:R00832`

## Notes

EQUATION: C00091 + C00062 <=> C00010 + C03296
