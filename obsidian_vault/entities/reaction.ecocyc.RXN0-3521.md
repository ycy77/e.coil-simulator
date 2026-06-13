---
entity_id: "reaction.ecocyc.RXN0-3521"
entity_type: "reaction"
name: "RXN0-3521"
source_database: "EcoCyc"
source_id: "RXN0-3521"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3521

`reaction.ecocyc.RXN0-3521`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3521`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-L-ARA4-FORMYL-N + CPD-9646 -> CPD0-888 + UDP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: UDP-L-ARA4-FORMYL-N + CPD-9646 -> CPD0-888 + UDP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by arnC (protein.P77757). Substrates: UDP-L-Ara4FN (molecule.C16154), di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556). Products: UDP (molecule.C00015), Undecaprenyl phosphate alpha-L-Ara4FN (molecule.C16156).

## Enriched Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Annotation

UDP-L-ARA4-FORMYL-N + CPD-9646 -> CPD0-888 + UDP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77757|protein.P77757]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16156|molecule.C16156]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C16154|molecule.C16154]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C17556|molecule.C17556]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3521`

## Notes

UDP-L-ARA4-FORMYL-N + CPD-9646 -> CPD0-888 + UDP; direction=LEFT-TO-RIGHT
