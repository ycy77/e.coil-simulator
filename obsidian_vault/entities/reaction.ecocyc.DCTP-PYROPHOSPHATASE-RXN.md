---
entity_id: "reaction.ecocyc.DCTP-PYROPHOSPHATASE-RXN"
entity_type: "reaction"
name: "DCTP-PYROPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "DCTP-PYROPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "dCTP diphosphatase"
  - "Deoxycytidine-triphosphatase"
  - "Deoxy-CTPase"
---

# DCTP-PYROPHOSPHATASE-RXN

`reaction.ecocyc.DCTP-PYROPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DCTP-PYROPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DCTP + WATER -> PROTON + DCMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DCTP + WATER -> PROTON + DCMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nudI (protein.P52006). Substrates: H2O (molecule.C00001), dCTP (molecule.C00458). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), dCMP (molecule.C00239).

## Enriched Pathways

- `ecocyc.PWY-7206` pyrimidine deoxyribonucleotides dephosphorylation (EcoCyc)

## Annotation

DCTP + WATER -> PROTON + DCMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7206` pyrimidine deoxyribonucleotides dephosphorylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P52006|protein.P52006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00239|molecule.C00239]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00458|molecule.C00458]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DCTP-PYROPHOSPHATASE-RXN`

## Notes

DCTP + WATER -> PROTON + DCMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
