---
entity_id: "molecule.C00818"
entity_type: "small_molecule"
name: "D-Glucarate"
source_database: "KEGG"
source_id: "C00818"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glucarate"
  - "D-Glucaric acid"
  - "L-Gularic acid"
  - "D-Saccharic acid"
  - "D-Glucosaccharic acid"
  - "Glucaric acid"
  - "Glucarate"
---

# D-Glucarate

`molecule.C00818`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00818`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glucarate; D-Glucaric acid; L-Gularic acid; D-Saccharic acid; D-Glucosaccharic acid; Glucaric acid; Glucarate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Annotation

KEGG compound: D-Glucarate; D-Glucaric acid; L-Gularic acid; D-Saccharic acid; D-Glucosaccharic acid; Glucaric acid; Glucarate

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN0-5285|reaction.ecocyc.RXN0-5285]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-204|reaction.ecocyc.TRANS-RXN0-204]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GLUCARDEHYDRA-RXN|reaction.ecocyc.GLUCARDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-204|reaction.ecocyc.TRANS-RXN0-204]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KDGALDOL-RXN|reaction.ecocyc.KDGALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.Q46916|protein.Q46916]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00818`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
