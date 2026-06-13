---
entity_id: "reaction.ecocyc.PGLUCONDEHYDRAT-RXN"
entity_type: "reaction"
name: "PGLUCONDEHYDRAT-RXN"
source_database: "EcoCyc"
source_id: "PGLUCONDEHYDRAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PGLUCONDEHYDRAT-RXN

`reaction.ecocyc.PGLUCONDEHYDRAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PGLUCONDEHYDRAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a key reaction in the Entner-Doudoroff pathway. EcoCyc reaction equation: CPD-2961 -> 2-KETO-3-DEOXY-6-P-GLUCONATE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT. This is a key reaction in the Entner-Doudoroff pathway.

## Biological Role

Catalyzed by edd (protein.P0ADF6). Substrates: 6-Phospho-D-gluconate (molecule.C00345). Products: H2O (molecule.C00001), 2-Dehydro-3-deoxy-6-phospho-D-gluconate (molecule.C04442).

## Enriched Pathways

- `ecocyc.ENTNER-DOUDOROFF-PWY` Entner-Doudoroff shunt (EcoCyc)

## Annotation

This is a key reaction in the Entner-Doudoroff pathway.

## Pathways

- `ecocyc.ENTNER-DOUDOROFF-PWY` Entner-Doudoroff shunt (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P0ADF6|protein.P0ADF6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04442|molecule.C04442]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00345|molecule.C00345]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5401|molecule.ecocyc.CPD-5401]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PGLUCONDEHYDRAT-RXN`

## Notes

CPD-2961 -> 2-KETO-3-DEOXY-6-P-GLUCONATE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
