---
entity_id: "reaction.ecocyc.KDPGALDOL-RXN"
entity_type: "reaction"
name: "KDPGALDOL-RXN"
source_database: "EcoCyc"
source_id: "KDPGALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# KDPGALDOL-RXN

`reaction.ecocyc.KDPGALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:KDPGALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the Entner-Doudoroff pathway. It is also a key reaction of hexuronic acid metabolism. EcoCyc reaction equation: 2-KETO-3-DEOXY-6-P-GLUCONATE -> GAP + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second reaction in the Entner-Doudoroff pathway. It is also a key reaction of hexuronic acid metabolism.

## Biological Role

Catalyzed by KHG/KDPG aldolase (complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX). Substrates: 2-Dehydro-3-deoxy-6-phospho-D-gluconate (molecule.C04442). Products: Pyruvate (molecule.C00022), D-Glyceraldehyde 3-phosphate (molecule.C00118).

## Enriched Pathways

- `ecocyc.ENTNER-DOUDOROFF-PWY` Entner-Doudoroff shunt (EcoCyc)
- `ecocyc.GALACTUROCAT-PWY` D-galacturonate degradation I (EcoCyc)
- `ecocyc.PWY-7242` D-fructuronate degradation (EcoCyc)
- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Annotation

This is the second reaction in the Entner-Doudoroff pathway. It is also a key reaction of hexuronic acid metabolism.

## Pathways

- `ecocyc.ENTNER-DOUDOROFF-PWY` Entner-Doudoroff shunt (EcoCyc)
- `ecocyc.GALACTUROCAT-PWY` D-galacturonate degradation I (EcoCyc)
- `ecocyc.PWY-7242` D-fructuronate degradation (EcoCyc)
- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX|complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04442|molecule.C04442]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00345|molecule.C00345]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:KDPGALDOL-RXN`

## Notes

2-KETO-3-DEOXY-6-P-GLUCONATE -> GAP + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT
