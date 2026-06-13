---
entity_id: "reaction.ecocyc.RXN-14116"
entity_type: "reaction"
name: "RXN-14116"
source_database: "EcoCyc"
source_id: "RXN-14116"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14116

`reaction.ecocyc.RXN-14116`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14116`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-GLUTAMATE_GAMMA-SEMIALDEHYDE + WATER + NAD -> GLT + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-GLUTAMATE_GAMMA-SEMIALDEHYDE + WATER + NAD -> GLT + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fused DNA-binding transcriptional repressor / proline dehydrogenase / 1-pyrroline-5-carboxylate dehydrogenase PutA (complex.ecocyc.PUTA-CPLX). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), L-Glutamate 5-semialdehyde (molecule.C01165). Products: NADH (molecule.C00004), L-Glutamate (molecule.C00025), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PROUT-PWY-I` proline degradation (EcoCyc)

## Annotation

L-GLUTAMATE_GAMMA-SEMIALDEHYDE + WATER + NAD -> GLT + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PROUT-PWY-I` proline degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.PUTA-CPLX|complex.ecocyc.PUTA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01165|molecule.C01165]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14116`

## Notes

L-GLUTAMATE_GAMMA-SEMIALDEHYDE + WATER + NAD -> GLT + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
