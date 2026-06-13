---
entity_id: "reaction.R00986"
entity_type: "reaction"
name: "chorismate pyruvate-lyase (amino-accepting)"
source_database: "KEGG"
source_id: "R00986"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00986"
---

# chorismate pyruvate-lyase (amino-accepting)

`reaction.R00986`

## Static

- Type: `reaction`
- Source: `KEGG:R00986`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Chorismate + L-Glutamine Anthranilate + Pyruvate + L-Glutamate

## Biological Role

Catalyzed by trpE (protein.P00895), trpGD (protein.P00904). Substrates: L-Glutamine (molecule.C00064), Chorismate (molecule.C00251). Products: Pyruvate (molecule.C00022), L-Glutamate (molecule.C00025), Anthranilate (molecule.C00108).

## Annotation

Chorismate + L-Glutamine <=> Anthranilate + Pyruvate + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P00895|protein.P00895]] `KEGG` `database` - via EC:4.1.3.27
- `catalyzes` <-- [[protein.P00904|protein.P00904]] `KEGG` `database` - via EC:4.1.3.27
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00251 + C00064 <=> C00108 + C00022 + C00025
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00251 + C00064 <=> C00108 + C00022 + C00025
- `is_product_of` <-- [[molecule.C00108|molecule.C00108]] `KEGG` `database` - C00251 + C00064 <=> C00108 + C00022 + C00025
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `KEGG` `database` - C00251 + C00064 <=> C00108 + C00022 + C00025
- `is_substrate_of` <-- [[molecule.C00251|molecule.C00251]] `KEGG` `database` - C00251 + C00064 <=> C00108 + C00022 + C00025

## External IDs

- `KEGG:R00986`

## Notes

EQUATION: C00251 + C00064 <=> C00108 + C00022 + C00025
