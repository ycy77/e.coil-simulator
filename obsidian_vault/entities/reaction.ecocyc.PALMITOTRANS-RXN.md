---
entity_id: "reaction.ecocyc.PALMITOTRANS-RXN"
entity_type: "reaction"
name: "PALMITOTRANS-RXN"
source_database: "EcoCyc"
source_id: "PALMITOTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PALMITOTRANS-RXN

`reaction.ecocyc.PALMITOTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PALMITOTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Palmitoleoyl-ACPs + KDO2-LIPID-IVA -> KDO2-PALMITOLEOYL-LIPID-IVA + ACP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Palmitoleoyl-ACPs + KDO2-LIPID-IVA -> KDO2-PALMITOLEOYL-LIPID-IVA + ACP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lpxP (protein.P0ACV2). Substrates: KDO2-lipid IVA (molecule.C06025). Products: (9Z)-Hexadec-9-enoyl-KDO2-lipid IV(A) (molecule.C20933).

## Enriched Pathways

- `ecocyc.KDO-NAGLIPASYN-PWY` superpathway of (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)

## Annotation

Palmitoleoyl-ACPs + KDO2-LIPID-IVA -> KDO2-PALMITOLEOYL-LIPID-IVA + ACP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.KDO-NAGLIPASYN-PWY` superpathway of (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0ACV2|protein.P0ACV2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C20933|molecule.C20933]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06025|molecule.C06025]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PALMITOTRANS-RXN`

## Notes

Palmitoleoyl-ACPs + KDO2-LIPID-IVA -> KDO2-PALMITOLEOYL-LIPID-IVA + ACP; direction=LEFT-TO-RIGHT
