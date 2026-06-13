---
entity_id: "reaction.R00985"
entity_type: "reaction"
name: "chorismate pyruvate-lyase (amino-accepting; anthranilate-forming)"
source_database: "KEGG"
source_id: "R00985"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00985"
---

# chorismate pyruvate-lyase (amino-accepting; anthranilate-forming)

`reaction.R00985`

## Static

- Type: `reaction`
- Source: `KEGG:R00985`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Chorismate + Ammonia Anthranilate + Pyruvate + H2O

## Biological Role

Catalyzed by trpE (protein.P00895), trpGD (protein.P00904). Substrates: Ammonia (molecule.C00014), Chorismate (molecule.C00251). Products: H2O (molecule.C00001), Pyruvate (molecule.C00022), Anthranilate (molecule.C00108).

## Annotation

Chorismate + Ammonia <=> Anthranilate + Pyruvate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P00895|protein.P00895]] `KEGG` `database` - via EC:4.1.3.27
- `catalyzes` <-- [[protein.P00904|protein.P00904]] `KEGG` `database` - via EC:4.1.3.27
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00251 + C00014 <=> C00108 + C00022 + C00001
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00251 + C00014 <=> C00108 + C00022 + C00001
- `is_product_of` <-- [[molecule.C00108|molecule.C00108]] `KEGG` `database` - C00251 + C00014 <=> C00108 + C00022 + C00001
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00251 + C00014 <=> C00108 + C00022 + C00001
- `is_substrate_of` <-- [[molecule.C00251|molecule.C00251]] `KEGG` `database` - C00251 + C00014 <=> C00108 + C00022 + C00001

## External IDs

- `KEGG:R00985`

## Notes

EQUATION: C00251 + C00014 <=> C00108 + C00022 + C00001
