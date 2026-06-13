---
entity_id: "reaction.ecocyc.PYRROLINECARBDEHYDROG-RXN"
entity_type: "reaction"
name: "1-pyrroline-5-carboxylate dehydrogenase"
source_database: "EcoCyc"
source_id: "PYRROLINECARBDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1-pyrroline-5-carboxylate dehydrogenase

`reaction.ecocyc.PYRROLINECARBDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRROLINECARBDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction takes part in proline utilization and in the interconversions of glutamate and glutamine. EcoCyc reaction equation: L-DELTA1-PYRROLINE_5-CARBOXYLATE + NAD + WATER -> PROTON + GLT + NADH; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction takes part in proline utilization and in the interconversions of glutamate and glutamine.

## Biological Role

Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), (S)-1-Pyrroline-5-carboxylate (molecule.C03912). Products: NADH (molecule.C00004), L-Glutamate (molecule.C00025), H+ (molecule.C00080).

## Annotation

This reaction takes part in proline utilization and in the interconversions of glutamate and glutamine.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03912|molecule.C03912]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PYRROLINECARBDEHYDROG-RXN`

## Notes

L-DELTA1-PYRROLINE_5-CARBOXYLATE + NAD + WATER -> PROTON + GLT + NADH; direction=PHYSIOL-LEFT-TO-RIGHT
