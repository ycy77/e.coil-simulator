---
entity_id: "molecule.C00294"
entity_type: "small_molecule"
name: "Inosine"
source_database: "KEGG"
source_id: "C00294"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Inosine"
---

# Inosine

`molecule.C00294`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00294`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Inosine

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Inosine

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.ecocyc.ADENODEAMIN-RXN|reaction.ecocyc.ADENODEAMIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-7607|reaction.ecocyc.RXN-7607]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-18|reaction.ecocyc.RXN0-18]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-108G|reaction.ecocyc.TRANS-RXN-108G]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.INOPHOSPHOR-RXN|reaction.ecocyc.INOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.INOSINE-NUCLEOSIDASE-RXN|reaction.ecocyc.INOSINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.INOSINEKIN-RXN|reaction.ecocyc.INOSINEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-18|reaction.ecocyc.RXN0-18]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-108G|reaction.ecocyc.TRANS-RXN-108G]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[protein.P0ADL1|protein.P0ADL1]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00294`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
