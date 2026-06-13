---
entity_id: "reaction.ecocyc.RHAMNULOKIN-RXN"
entity_type: "reaction"
name: "RHAMNULOKIN-RXN"
source_database: "EcoCyc"
source_id: "RHAMNULOKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RHAMNULOKIN-RXN

`reaction.ecocyc.RHAMNULOKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RHAMNULOKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The second step in L-rhamnose catabolism. EcoCyc reaction equation: CPD-16567 + ATP -> PROTON + RHAMNULOSE-1P + ADP; direction=LEFT-TO-RIGHT. The second step in L-rhamnose catabolism.

## Biological Role

Catalyzed by rhaB (protein.P32171). Substrates: ATP (molecule.C00002), L-rhamnulofuranose (molecule.ecocyc.CPD-16567). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-Rhamnulose 1-phosphate (molecule.C01131).

## Enriched Pathways

- `ecocyc.RHAMCAT-PWY` L-rhamnose degradation I (EcoCyc)

## Annotation

The second step in L-rhamnose catabolism.

## Pathways

- `ecocyc.RHAMCAT-PWY` L-rhamnose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P32171|protein.P32171]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01131|molecule.C01131]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-16567|molecule.ecocyc.CPD-16567]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RHAMNULOKIN-RXN`

## Notes

CPD-16567 + ATP -> PROTON + RHAMNULOSE-1P + ADP; direction=LEFT-TO-RIGHT
