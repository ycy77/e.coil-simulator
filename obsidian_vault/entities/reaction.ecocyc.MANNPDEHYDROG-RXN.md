---
entity_id: "reaction.ecocyc.MANNPDEHYDROG-RXN"
entity_type: "reaction"
name: "MANNPDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "MANNPDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MANNPDEHYDROG-RXN

`reaction.ecocyc.MANNPDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MANNPDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction takes part in mannitol degradation. EcoCyc reaction equation: MANNITOL-1P + NAD -> PROTON + FRUCTOSE-6P + NADH; direction=REVERSIBLE. This reaction takes part in mannitol degradation.

## Biological Role

Catalyzed by mtlD (protein.P09424). Substrates: NAD+ (molecule.C00003), D-Mannitol 1-phosphate (molecule.C00644). Products: NADH (molecule.C00004), H+ (molecule.C00080), β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P).

## Enriched Pathways

- `ecocyc.MANNIDEG-PWY` mannitol degradation I (EcoCyc)

## Annotation

This reaction takes part in mannitol degradation.

## Pathways

- `ecocyc.MANNIDEG-PWY` mannitol degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P09424|protein.P09424]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00644|molecule.C00644]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MANNPDEHYDROG-RXN`

## Notes

MANNITOL-1P + NAD -> PROTON + FRUCTOSE-6P + NADH; direction=REVERSIBLE
