---
entity_id: "reaction.ecocyc.MYRPALMTRAN-RXN"
entity_type: "reaction"
name: "MYRPALMTRAN-RXN"
source_database: "EcoCyc"
source_id: "MYRPALMTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MYRPALMTRAN-RXN

`reaction.ecocyc.MYRPALMTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MYRPALMTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Myristoyl-ACPs + KDO2-PALMITOLEOYL-LIPID-IVA -> KDO2-LIPID-IVA-COLD + ACP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Myristoyl-ACPs + KDO2-PALMITOLEOYL-LIPID-IVA -> KDO2-LIPID-IVA-COLD + ACP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lpxM (protein.P24205). Substrates: (9Z)-Hexadec-9-enoyl-KDO2-lipid IV(A) (molecule.C20933). Products: (Kdo)2-lipid A, cold adapted (molecule.ecocyc.KDO2-LIPID-IVA-COLD).

## Enriched Pathways

- `ecocyc.KDO-NAGLIPASYN-PWY` superpathway of (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)

## Annotation

Myristoyl-ACPs + KDO2-PALMITOLEOYL-LIPID-IVA -> KDO2-LIPID-IVA-COLD + ACP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.KDO-NAGLIPASYN-PWY` superpathway of (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P24205|protein.P24205]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.KDO2-LIPID-IVA-COLD|molecule.ecocyc.KDO2-LIPID-IVA-COLD]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C20933|molecule.C20933]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MYRPALMTRAN-RXN`

## Notes

Myristoyl-ACPs + KDO2-PALMITOLEOYL-LIPID-IVA -> KDO2-LIPID-IVA-COLD + ACP; direction=LEFT-TO-RIGHT
