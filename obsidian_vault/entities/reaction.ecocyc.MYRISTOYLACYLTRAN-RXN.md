---
entity_id: "reaction.ecocyc.MYRISTOYLACYLTRAN-RXN"
entity_type: "reaction"
name: "MYRISTOYLACYLTRAN-RXN"
source_database: "EcoCyc"
source_id: "MYRISTOYLACYLTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MYRISTOYLACYLTRAN-RXN

`reaction.ecocyc.MYRISTOYLACYLTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MYRISTOYLACYLTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Myristoyl-ACPs + KDO2-LAUROYL-LIPID-IVA -> KDO2-LIPID-A + ACP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Myristoyl-ACPs + KDO2-LAUROYL-LIPID-IVA -> KDO2-LIPID-A + ACP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lpxM (protein.P24205). Substrates: Lauroyl-KDO2-lipid IV(A) (molecule.C06251). Products: KDO2-lipid A (molecule.C06026).

## Enriched Pathways

- `ecocyc.KDO-LIPASYN-PWY` (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)
- `ecocyc.KDO-NAGLIPASYN-PWY` superpathway of (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)

## Annotation

Myristoyl-ACPs + KDO2-LAUROYL-LIPID-IVA -> KDO2-LIPID-A + ACP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.KDO-LIPASYN-PWY` (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)
- `ecocyc.KDO-NAGLIPASYN-PWY` superpathway of (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P24205|protein.P24205]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C06026|molecule.C06026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06251|molecule.C06251]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MYRISTOYLACYLTRAN-RXN`

## Notes

Myristoyl-ACPs + KDO2-LAUROYL-LIPID-IVA -> KDO2-LIPID-A + ACP; direction=LEFT-TO-RIGHT
