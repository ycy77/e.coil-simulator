---
entity_id: "molecule.C00295"
entity_type: "small_molecule"
name: "Orotate"
source_database: "KEGG"
source_id: "C00295"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Orotate"
  - "Orotic acid"
  - "Uracil-6-carboxylic acid"
---

# Orotate

`molecule.C00295`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00295`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Orotate; Orotic acid; Uracil-6-carboxylic acid

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: Orotate; Orotic acid; Uracil-6-carboxylic acid

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN|reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.OROPRIBTRANS-RXN|reaction.ecocyc.OROPRIBTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6491|reaction.ecocyc.RXN0-6491]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6554|reaction.ecocyc.RXN0-6554]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-121C|reaction.ecocyc.TRANS-RXN-121C]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6490|reaction.ecocyc.RXN0-6490]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-121C|reaction.ecocyc.TRANS-RXN-121C]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN|reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-6491|reaction.ecocyc.RXN0-6491]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00295`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
