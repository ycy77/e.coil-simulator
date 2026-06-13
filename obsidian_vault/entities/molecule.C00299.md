---
entity_id: "molecule.C00299"
entity_type: "small_molecule"
name: "Uridine"
source_database: "KEGG"
source_id: "C00299"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Uridine"
---

# Uridine

`molecule.C00299`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00299`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Uridine

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 7 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Uridine

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (13)

- `is_product_of` --> [[reaction.R01877|reaction.R01877]] `KEGG` `database` - C01368 + C00001 <=> C00299 + C00009
- `is_product_of` --> [[reaction.R01878|reaction.R01878]] `KEGG` `database` - C00475 + C00001 <=> C00299 + C00014
- `is_product_of` --> [[reaction.ecocyc.CYTIDEAM2-RXN|reaction.ecocyc.CYTIDEAM2-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14025|reaction.ecocyc.RXN-14025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14115|reaction.ecocyc.RXN-14115]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14510|reaction.ecocyc.RXN-14510]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-108I|reaction.ecocyc.TRANS-RXN-108I]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-108I|reaction.ecocyc.TRANS-RXN-108I]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN|reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.URIDINEKIN-RXN|reaction.ecocyc.URIDINEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.URKI-RXN|reaction.ecocyc.URKI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.URPHOS-RXN|reaction.ecocyc.URPHOS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACID-PHOSPHATASE-RXN|reaction.ecocyc.ACID-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00299`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
