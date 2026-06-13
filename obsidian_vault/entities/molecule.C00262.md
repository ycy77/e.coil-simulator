---
entity_id: "molecule.C00262"
entity_type: "small_molecule"
name: "Hypoxanthine"
source_database: "KEGG"
source_id: "C00262"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Hypoxanthine"
  - "Purine-6-ol"
---

# Hypoxanthine

`molecule.C00262`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00262`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Hypoxanthine; Purine-6-ol

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: Hypoxanthine; Purine-6-ol

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (15)

- `is_component_of` --> [[complex.ecocyc.CPLX-123|complex.ecocyc.CPLX-123]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.ADENINE-DEAMINASE-RXN|reaction.ecocyc.ADENINE-DEAMINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DEOXYINOPHOSPHOR-RXN|reaction.ecocyc.DEOXYINOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN|reaction.ecocyc.HYPOXANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.INOPHOSPHOR-RXN|reaction.ecocyc.INOPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.INOSINATE-NUCLEOSIDASE-RXN|reaction.ecocyc.INOSINATE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.INOSINE-NUCLEOSIDASE-RXN|reaction.ecocyc.INOSINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-562|reaction.ecocyc.TRANS-RXN0-562]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-579|reaction.ecocyc.TRANS-RXN0-579]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-7682|reaction.ecocyc.RXN-7682]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-284|reaction.ecocyc.RXN0-284]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-562|reaction.ecocyc.TRANS-RXN0-562]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-579|reaction.ecocyc.TRANS-RXN0-579]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-447|reaction.ecocyc.TRANS-RXN0-447]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-577|reaction.ecocyc.TRANS-RXN0-577]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.Q46817|protein.Q46817]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00262`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
