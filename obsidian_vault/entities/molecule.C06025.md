---
entity_id: "molecule.C06025"
entity_type: "small_molecule"
name: "KDO2-lipid IVA"
source_database: "KEGG"
source_id: "C06025"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "KDO2-lipid IVA"
  - "Di[3-deoxy-D-manno-octulosonyl]-lipid IV(A)"
  - "KDO2-lipid IV(A)"
  - "alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[lipid IVA]"
---

# KDO2-lipid IVA

`molecule.C06025`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06025`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: KDO2-lipid IVA; Di[3-deoxy-D-manno-octulosonyl]-lipid IV(A); KDO2-lipid IV(A); alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[lipid IVA] EcoCyc common name: α-Kdo-(2->4)-α-Kdo-(2->6)-lipid IVA (E. coli).

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

KEGG compound: KDO2-lipid IVA; Di[3-deoxy-D-manno-octulosonyl]-lipid IV(A); KDO2-lipid IV(A); alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[lipid IVA]

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (10)

- `is_product_of` --> [[reaction.ecocyc.KDOTRANS2-RXN|reaction.ecocyc.KDOTRANS2-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R09774|reaction.R09774]] `KEGG` `database` - C16157 + C06025 <=> C19883 + C17556
- `is_substrate_of` --> [[reaction.R10906|reaction.R10906]] `KEGG` `database` - C16520 + C06025 <=> C20933 + C00229
- `is_substrate_of` --> [[reaction.ecocyc.LAUROYLACYLTRAN-RXN|reaction.ecocyc.LAUROYLACYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PALMITOTRANS-RXN|reaction.ecocyc.PALMITOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11326|reaction.ecocyc.RXN-11326]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4581|reaction.ecocyc.RXN0-4581]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5057|reaction.ecocyc.RXN0-5057]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KDOTRANS-RXN|reaction.ecocyc.KDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KDOTRANS2-RXN|reaction.ecocyc.KDOTRANS2-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06025`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
