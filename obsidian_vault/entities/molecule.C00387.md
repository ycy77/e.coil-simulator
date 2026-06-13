---
entity_id: "molecule.C00387"
entity_type: "small_molecule"
name: "Guanosine"
source_database: "KEGG"
source_id: "C00387"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Guanosine"
---

# Guanosine

`molecule.C00387`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00387`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Guanosine

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Guanosine

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (12)

- `is_product_of` --> [[reaction.ecocyc.RXN-14124|reaction.ecocyc.RXN-14124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14512|reaction.ecocyc.RXN-14512]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-7609|reaction.ecocyc.RXN-7609]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-22|reaction.ecocyc.RXN0-22]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-474|reaction.ecocyc.TRANS-RXN-474]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02147|reaction.R02147]] `KEGG` `database` - C00387 + C00009 <=> C00242 + C00620
- `is_substrate_of` --> [[reaction.ecocyc.GUANOSINEKIN-RXN|reaction.ecocyc.GUANOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-22|reaction.ecocyc.RXN0-22]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5199|reaction.ecocyc.RXN0-5199]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-474|reaction.ecocyc.TRANS-RXN-474]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACID-PHOSPHATASE-RXN|reaction.ecocyc.ACID-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GUANYL-KIN-RXN|reaction.ecocyc.GUANYL-KIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[protein.P0ADL1|protein.P0ADL1]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00387`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
