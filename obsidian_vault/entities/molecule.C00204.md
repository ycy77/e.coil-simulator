---
entity_id: "molecule.C00204"
entity_type: "small_molecule"
name: "2-Dehydro-3-deoxy-D-gluconate"
source_database: "KEGG"
source_id: "C00204"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Dehydro-3-deoxy-D-gluconate"
  - "2-Keto-3-deoxy-D-gluconate"
  - "2-Dehydro-3-deoxy-D-gluconic acid"
---

# 2-Dehydro-3-deoxy-D-gluconate

`molecule.C00204`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00204`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Dehydro-3-deoxy-D-gluconate; 2-Keto-3-deoxy-D-gluconate; 2-Dehydro-3-deoxy-D-gluconic acid

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: 2-Dehydro-3-deoxy-D-gluconate; 2-Keto-3-deoxy-D-gluconate; 2-Dehydro-3-deoxy-D-gluconic acid

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (10)

- `is_product_of` --> [[reaction.R01540|reaction.R01540]] `KEGG` `database` - C00817 <=> C00204 + C00001
- `is_product_of` --> [[reaction.ecocyc.ALTRODEHYDRAT-RXN|reaction.ecocyc.ALTRODEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MANNONDEHYDRAT-RXN|reaction.ecocyc.MANNONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-113|reaction.ecocyc.TRANS-RXN-113]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01541|reaction.R01541]] `KEGG` `database` - C00002 + C00204 <=> C00008 + C04442
- `is_substrate_of` --> [[reaction.R01542|reaction.R01542]] `KEGG` `database` - C00204 + C00003 <=> C04349 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.1.1.1.127-RXN|reaction.ecocyc.1.1.1.127-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DEOXYGLUCONOKIN-RXN|reaction.ecocyc.DEOXYGLUCONOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DHDOGALDOL-RXN|reaction.ecocyc.DHDOGALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-113|reaction.ecocyc.TRANS-RXN-113]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P0A712|protein.P0A712]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00204`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
