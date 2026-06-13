---
entity_id: "molecule.C00258"
entity_type: "small_molecule"
name: "D-Glycerate"
source_database: "KEGG"
source_id: "C00258"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glycerate"
  - "Glycerate"
  - "(R)-Glycerate"
  - "Glyceric acid"
---

# D-Glycerate

`molecule.C00258`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00258`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glycerate; Glycerate; (R)-Glycerate; Glyceric acid

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: D-Glycerate; Glycerate; (R)-Glycerate; Glyceric acid

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (14)

- `is_product_of` --> [[reaction.R11959|reaction.R11959]] `KEGG` `database` - C19792 + C00009 <=> C00103 + C00258
- `is_product_of` --> [[reaction.ecocyc.3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN|reaction.ecocyc.3-PHOSPHOGLYCERATE-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PHOSPHOGLYCERATE-PHOSPHATASE-RXN|reaction.ecocyc.PHOSPHOGLYCERATE-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18999|reaction.ecocyc.RXN-18999]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5216|reaction.ecocyc.RXN0-5216]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-523|reaction.ecocyc.TRANS-RXN0-523]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01745|reaction.R01745]] `KEGG` `database` - C00258 + C00003 <=> C01146 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R01747|reaction.R01747]] `KEGG` `database` - C00258 + C00006 <=> C01146 + C00005 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.GKI-RXN|reaction.ecocyc.GKI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLY3KIN-RXN|reaction.ecocyc.GLY3KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-300|reaction.ecocyc.RXN0-300]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5289|reaction.ecocyc.RXN0-5289]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-523|reaction.ecocyc.TRANS-RXN0-523]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TSA-REDUCT-RXN|reaction.ecocyc.TSA-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.Q46916|protein.Q46916]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00258`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
