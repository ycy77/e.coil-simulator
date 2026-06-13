---
entity_id: "molecule.C00243"
entity_type: "small_molecule"
name: "Lactose"
source_database: "KEGG"
source_id: "C00243"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Lactose"
  - "1-beta-D-Galactopyranosyl-4-D-glucopyranose"
  - "beta-D-Gal-(1->4)-D-Glc"
  - "Milk sugar"
---

# Lactose

`molecule.C00243`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00243`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Lactose; 1-beta-D-Galactopyranosyl-4-D-glucopyranose; beta-D-Gal-(1->4)-D-Glc; Milk sugar

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Lactose; 1-beta-D-Galactopyranosyl-4-D-glucopyranose; beta-D-Gal-(1->4)-D-Glc; Milk sugar

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-24|reaction.ecocyc.TRANS-RXN-24]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-82|reaction.ecocyc.TRANS-RXN-82]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.BETAGALACTOSID-RXN|reaction.ecocyc.BETAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5363|reaction.ecocyc.RXN0-5363]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-24|reaction.ecocyc.TRANS-RXN-24]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-82|reaction.ecocyc.TRANS-RXN-82]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[protein.P02920|protein.P02920]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P33026|protein.P33026]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00243`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
