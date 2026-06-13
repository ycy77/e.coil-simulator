---
entity_id: "reaction.ecocyc.DEOXYGLUCONOKIN-RXN"
entity_type: "reaction"
name: "DEOXYGLUCONOKIN-RXN"
source_database: "EcoCyc"
source_id: "DEOXYGLUCONOKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DEOXYGLUCONOKIN-RXN

`reaction.ecocyc.DEOXYGLUCONOKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEOXYGLUCONOKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A single connecting reaction between 2-dehydro-3-deoxygluconate production and the Entner-Doudoroff pathway. EcoCyc reaction equation: 2-DEHYDRO-3-DEOXY-D-GLUCONATE + ATP -> PROTON + 2-KETO-3-DEOXY-6-P-GLUCONATE + ADP; direction=LEFT-TO-RIGHT. A single connecting reaction between 2-dehydro-3-deoxygluconate production and the Entner-Doudoroff pathway.

## Biological Role

Catalyzed by kdgK (protein.P37647). Substrates: ATP (molecule.C00002), 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204). Products: ADP (molecule.C00008), H+ (molecule.C00080), 2-Dehydro-3-deoxy-6-phospho-D-gluconate (molecule.C04442).

## Enriched Pathways

- `ecocyc.GALACTUROCAT-PWY` D-galacturonate degradation I (EcoCyc)
- `ecocyc.PWY-7242` D-fructuronate degradation (EcoCyc)
- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Annotation

A single connecting reaction between 2-dehydro-3-deoxygluconate production and the Entner-Doudoroff pathway.

## Pathways

- `ecocyc.GALACTUROCAT-PWY` D-galacturonate degradation I (EcoCyc)
- `ecocyc.PWY-7242` D-fructuronate degradation (EcoCyc)
- `ecocyc.PWY-7562` 3,6-anhydro-α-L-galactopyranose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37647|protein.P37647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04442|molecule.C04442]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00204|molecule.C00204]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DEOXYGLUCONOKIN-RXN`

## Notes

2-DEHYDRO-3-DEOXY-D-GLUCONATE + ATP -> PROTON + 2-KETO-3-DEOXY-6-P-GLUCONATE + ADP; direction=LEFT-TO-RIGHT
