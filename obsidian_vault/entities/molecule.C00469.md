---
entity_id: "molecule.C00469"
entity_type: "small_molecule"
name: "Ethanol"
source_database: "KEGG"
source_id: "C00469"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Ethanol"
  - "Ethyl alcohol"
  - "Methylcarbinol"
---

# Ethanol

`molecule.C00469`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00469`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Ethanol; Ethyl alcohol; Methylcarbinol

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)

## Annotation

KEGG compound: Ethanol; Ethyl alcohol; Methylcarbinol

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)

## Outgoing Edges (6)

- `activates` --> [[reaction.ecocyc.ACID-PHOSPHATASE-RXN|reaction.ecocyc.ACID-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-546|reaction.ecocyc.TRANS-RXN0-546]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00746|reaction.R00746]] `KEGG` `database` - C00469 + C00006 <=> C00084 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R00754|reaction.R00754]] `KEGG` `database` - C00469 + C00003 <=> C00084 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-546|reaction.ecocyc.TRANS-RXN0-546]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00469`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
