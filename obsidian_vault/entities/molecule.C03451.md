---
entity_id: "molecule.C03451"
entity_type: "small_molecule"
name: "(R)-S-Lactoylglutathione"
source_database: "KEGG"
source_id: "C03451"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(R)-S-Lactoylglutathione"
  - "S-D-Lactoylglutathione"
---

# (R)-S-Lactoylglutathione

`molecule.C03451`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03451`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (R)-S-Lactoylglutathione; S-D-Lactoylglutathione

## Biological Role

Consumed as substrate in 4 reaction(s).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)

## Annotation

KEGG compound: (R)-S-Lactoylglutathione; S-D-Lactoylglutathione

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.R01736|reaction.R01736]] `KEGG` `database` - C03451 + C00001 <=> C00051 + C00256
- `is_substrate_of` --> [[reaction.ecocyc.GLYOXI-RXN|reaction.ecocyc.GLYOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYOXII-RXN|reaction.ecocyc.GLYOXII-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN2PN3-45|reaction.ecocyc.RXN2PN3-45]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03451`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
