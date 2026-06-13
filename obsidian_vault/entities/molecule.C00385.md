---
entity_id: "molecule.C00385"
entity_type: "small_molecule"
name: "Xanthine"
source_database: "KEGG"
source_id: "C00385"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Xanthine"
---

# Xanthine

`molecule.C00385`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00385`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Xanthine Xanthine is a purine nucleobase found in many organisms including humans. It exists as two tautomers: CPD-26753 and CPD-26752. The structure shown here is of the latter.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 9 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: Xanthine

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (13)

- `is_product_of` --> [[reaction.R02142|reaction.R02142]] `KEGG` `database` - C00655 + C00013 <=> C00385 + C00119
- `is_product_of` --> [[reaction.ecocyc.GUANINE-DEAMINASE-RXN|reaction.ecocyc.GUANINE-DEAMINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-5076|reaction.ecocyc.RXN-5076]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-7682|reaction.ecocyc.RXN-7682]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-363|reaction.ecocyc.RXN0-363]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6708|reaction.ecocyc.RXN0-6708]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-561|reaction.ecocyc.TRANS-RXN0-561]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.XANPRIBOSYLTRAN-RXN|reaction.ecocyc.XANPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN|reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-5076|reaction.ecocyc.RXN-5076]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-901|reaction.ecocyc.RXN0-901]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-561|reaction.ecocyc.TRANS-RXN0-561]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.TRANS-RXN-132|reaction.ecocyc.TRANS-RXN-132]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P75892|protein.P75892]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00385`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
