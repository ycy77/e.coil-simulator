---
entity_id: "reaction.ecocyc.RXN0-2001"
entity_type: "reaction"
name: "RXN0-2001"
source_database: "EcoCyc"
source_id: "RXN0-2001"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2001

`reaction.ecocyc.RXN0-2001`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2001`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

KDO2-LIPID-A + CPD0-1189 -> L-ARA4N-MODIFIED-KDO2-LIPID-A + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: KDO2-LIPID-A + CPD0-1189 -> L-ARA4N-MODIFIED-KDO2-LIPID-A + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by arnT (protein.P76473). Substrates: KDO2-lipid A (molecule.C06026), Undecaprenyl phosphate alpha-L-Ara4N (molecule.C16157). Products: di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556), α-Kdo-(2→4)-α-Kdo-(2→6)-[P4'-α-L-ara4N]-lipid A (E. coli) (molecule.ecocyc.L-ARA4N-MODIFIED-KDO2-LIPID-A).

## Enriched Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Annotation

KDO2-LIPID-A + CPD0-1189 -> L-ARA4N-MODIFIED-KDO2-LIPID-A + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76473|protein.P76473]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C17556|molecule.C17556]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-ARA4N-MODIFIED-KDO2-LIPID-A|molecule.ecocyc.L-ARA4N-MODIFIED-KDO2-LIPID-A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06026|molecule.C06026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16157|molecule.C16157]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2001`

## Notes

KDO2-LIPID-A + CPD0-1189 -> L-ARA4N-MODIFIED-KDO2-LIPID-A + CPD-9646; direction=PHYSIOL-LEFT-TO-RIGHT
