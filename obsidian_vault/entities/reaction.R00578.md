---
entity_id: "reaction.R00578"
entity_type: "reaction"
name: "L-aspartate:L-glutamine amido-ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R00578"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00578"
---

# L-aspartate:L-glutamine amido-ligase (AMP-forming)

`reaction.R00578`

## Static

- Type: `reaction`
- Source: `KEGG:R00578`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Aspartate + L-Glutamine + H2O AMP + Diphosphate + L-Asparagine + L-Glutamate

## Biological Role

Catalyzed by asnB (protein.P22106). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Aspartate (molecule.C00049), L-Glutamine (molecule.C00064). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Glutamate (molecule.C00025), L-Asparagine (molecule.C00152).

## Annotation

ATP + L-Aspartate + L-Glutamine + H2O <=> AMP + Diphosphate + L-Asparagine + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P22106|protein.P22106]] `KEGG` `database` - via EC:6.3.5.4
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_product_of` <-- [[molecule.C00152|molecule.C00152]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `KEGG` `database` - C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025

## External IDs

- `KEGG:R00578`

## Notes

EQUATION: C00002 + C00049 + C00064 + C00001 <=> C00020 + C00013 + C00152 + C00025
