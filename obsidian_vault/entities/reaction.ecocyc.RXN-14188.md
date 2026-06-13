---
entity_id: "reaction.ecocyc.RXN-14188"
entity_type: "reaction"
name: "RXN-14188"
source_database: "EcoCyc"
source_id: "RXN-14188"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14188

`reaction.ecocyc.RXN-14188`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14188`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-HYDROXY-CTP + WATER -> CPD-15158 + PPI + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 5-HYDROXY-CTP + WATER -> CPD-15158 + PPI + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nudG (protein.P77788). Substrates: H2O (molecule.C00001), 5-hydroxy-CTP (molecule.ecocyc.5-HYDROXY-CTP). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), 5-hydroxy-CMP (molecule.ecocyc.CPD-15158).

## Enriched Pathways

- `ecocyc.PWY-7206` pyrimidine deoxyribonucleotides dephosphorylation (EcoCyc)

## Annotation

5-HYDROXY-CTP + WATER -> CPD-15158 + PPI + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7206` pyrimidine deoxyribonucleotides dephosphorylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77788|protein.P77788]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15158|molecule.ecocyc.CPD-15158]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-HYDROXY-CTP|molecule.ecocyc.5-HYDROXY-CTP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14188`

## Notes

5-HYDROXY-CTP + WATER -> CPD-15158 + PPI + PROTON; direction=LEFT-TO-RIGHT
