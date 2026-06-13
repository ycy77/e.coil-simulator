---
entity_id: "reaction.ecocyc.DARABKIN-RXN"
entity_type: "reaction"
name: "DARABKIN-RXN"
source_database: "EcoCyc"
source_id: "DARABKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DARABKIN-RXN

`reaction.ecocyc.DARABKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DARABKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the metabolism of D-arabinose in E. coli K-12 through utilization of the L-fucose catabolism pathway enzymes. EcoCyc reaction equation: D-RIBULOSE + ATP -> PROTON + D-RIBULOSE-1-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second reaction in the metabolism of D-arabinose in E. coli K-12 through utilization of the L-fucose catabolism pathway enzymes.

## Biological Role

Catalyzed by fucK (protein.P11553). Substrates: ATP (molecule.C00002), D-Ribulose (molecule.C00309). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Ribulose 1-phosphate (molecule.C22337).

## Enriched Pathways

- `ecocyc.DARABCATK12-PWY` D-arabinose degradation II (EcoCyc)

## Annotation

This is the second reaction in the metabolism of D-arabinose in E. coli K-12 through utilization of the L-fucose catabolism pathway enzymes.

## Pathways

- `ecocyc.DARABCATK12-PWY` D-arabinose degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P11553|protein.P11553]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C22337|molecule.C22337]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00309|molecule.C00309]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DARABKIN-RXN`

## Notes

D-RIBULOSE + ATP -> PROTON + D-RIBULOSE-1-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
