---
entity_id: "molecule.C20933"
entity_type: "small_molecule"
name: "(9Z)-Hexadec-9-enoyl-KDO2-lipid IV(A)"
source_database: "KEGG"
source_id: "C20933"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(9Z)-Hexadec-9-enoyl-KDO2-lipid IV(A)"
  - "Palmitoleoyl-KDO2-lipid IV(A)"
  - "(9Z)-Hexadec-9-enoyl-KDO2-lipid IVA"
---

# (9Z)-Hexadec-9-enoyl-KDO2-lipid IV(A)

`molecule.C20933`

## Static

- Type: `small_molecule`
- Source: `KEGG:C20933`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (9Z)-Hexadec-9-enoyl-KDO2-lipid IV(A); Palmitoleoyl-KDO2-lipid IV(A); (9Z)-Hexadec-9-enoyl-KDO2-lipid IVA EcoCyc common name: Kdo2-(palmitoleoyl)-lipid IVA.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

KEGG compound: (9Z)-Hexadec-9-enoyl-KDO2-lipid IV(A); Palmitoleoyl-KDO2-lipid IV(A); (9Z)-Hexadec-9-enoyl-KDO2-lipid IVA

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R10906|reaction.R10906]] `KEGG` `database` - C16520 + C06025 <=> C20933 + C00229
- `is_product_of` --> [[reaction.ecocyc.PALMITOTRANS-RXN|reaction.ecocyc.PALMITOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.MYRPALMTRAN-RXN|reaction.ecocyc.MYRPALMTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C20933`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
