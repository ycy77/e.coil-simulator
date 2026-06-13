---
entity_id: "reaction.ecocyc.RNA-3-PHOSPHATE-CYCLASE-RXN"
entity_type: "reaction"
name: "RNA-3-PHOSPHATE-CYCLASE-RXN"
source_database: "EcoCyc"
source_id: "RNA-3-PHOSPHATE-CYCLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "RNA CYCLASE"
---

# RNA-3-PHOSPHATE-CYCLASE-RXN

`reaction.ecocyc.RNA-3-PHOSPHATE-CYCLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RNA-3-PHOSPHATE-CYCLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADENOSINE 5'-(γ-THIO)TRIPHOSPHATE CAN ACT INSTEAD OF ATP. EcoCyc reaction equation: 3-Prime-Phosphate-Terminated-RNAs + ATP -> Cyclic-Phosphate-Terminated-RNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. ADENOSINE 5'-(γ-THIO)TRIPHOSPHATE CAN ACT INSTEAD OF ATP.

## Biological Role

Catalyzed by rtcA (protein.P46849). Substrates: ATP (molecule.C00002). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

ADENOSINE 5'-(γ-THIO)TRIPHOSPHATE CAN ACT INSTEAD OF ATP.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P46849|protein.P46849]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RNA-3-PHOSPHATE-CYCLASE-RXN`

## Notes

3-Prime-Phosphate-Terminated-RNAs + ATP -> Cyclic-Phosphate-Terminated-RNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
