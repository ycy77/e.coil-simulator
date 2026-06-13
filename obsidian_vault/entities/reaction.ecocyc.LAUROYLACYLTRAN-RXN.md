---
entity_id: "reaction.ecocyc.LAUROYLACYLTRAN-RXN"
entity_type: "reaction"
name: "LAUROYLACYLTRAN-RXN"
source_database: "EcoCyc"
source_id: "LAUROYLACYLTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LAUROYLACYLTRAN-RXN

`reaction.ecocyc.LAUROYLACYLTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LAUROYLACYLTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dodecanoyl-ACPs + KDO2-LIPID-IVA -> KDO2-LAUROYL-LIPID-IVA + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Dodecanoyl-ACPs + KDO2-LIPID-IVA -> KDO2-LAUROYL-LIPID-IVA + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lpxL (protein.P0ACV0). Substrates: KDO2-lipid IVA (molecule.C06025). Products: Lauroyl-KDO2-lipid IV(A) (molecule.C06251).

## Enriched Pathways

- `ecocyc.KDO-LIPASYN-PWY` (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)
- `ecocyc.KDO-NAGLIPASYN-PWY` superpathway of (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)

## Annotation

Dodecanoyl-ACPs + KDO2-LIPID-IVA -> KDO2-LAUROYL-LIPID-IVA + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.KDO-LIPASYN-PWY` (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)
- `ecocyc.KDO-NAGLIPASYN-PWY` superpathway of (Kdo)2-lipid A biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0ACV0|protein.P0ACV0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C06251|molecule.C06251]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06025|molecule.C06025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01832|molecule.C01832]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:LAUROYLACYLTRAN-RXN`

## Notes

Dodecanoyl-ACPs + KDO2-LIPID-IVA -> KDO2-LAUROYL-LIPID-IVA + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
