---
entity_id: "molecule.C01159"
entity_type: "small_molecule"
name: "2,3-Bisphospho-D-glycerate"
source_database: "KEGG"
source_id: "C01159"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2,3-Bisphospho-D-glycerate"
  - "2,3-Diphospho-D-glycerate"
  - "D-Greenwald ester"
  - "DPG"
---

# 2,3-Bisphospho-D-glycerate

`molecule.C01159`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01159`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2,3-Bisphospho-D-glycerate; 2,3-Diphospho-D-glycerate; D-Greenwald ester; DPG EcoCyc common name: 2,3-diphospho-D-glycerate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s). Binds 2,3-bisphosphoglycerate-dependent phosphoglycerate mutase (complex.ecocyc.PHOSGLYCMUTASE).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)

## Annotation

KEGG compound: 2,3-Bisphospho-D-glycerate; 2,3-Diphospho-D-glycerate; D-Greenwald ester; DPG

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)

## Outgoing Edges (6)

- `binds` --> [[complex.ecocyc.PHOSGLYCMUTASE|complex.ecocyc.PHOSGLYCMUTASE]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.RXN-15510|reaction.ecocyc.RXN-15510]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15512|reaction.ecocyc.RXN-15512]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15509|reaction.ecocyc.RXN-15509]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15511|reaction.ecocyc.RXN-15511]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01159`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
