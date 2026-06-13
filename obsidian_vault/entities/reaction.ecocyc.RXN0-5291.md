---
entity_id: "reaction.ecocyc.RXN0-5291"
entity_type: "reaction"
name: "RXN0-5291"
source_database: "EcoCyc"
source_id: "RXN0-5291"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5291

`reaction.ecocyc.RXN0-5291`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5291`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + THIAMINE-PYROPHOSPHATE + ADP -> CPD0-1095 + Pi; direction=REVERSIBLE EcoCyc reaction equation: PROTON + THIAMINE-PYROPHOSPHATE + ADP -> CPD0-1095 + Pi; direction=REVERSIBLE.

## Biological Role

Catalyzed by ThDP adenylyl transferase (protein.ecocyc.MONOMER0-2838). Substrates: ADP (molecule.C00008), Thiamin diphosphate (molecule.C00068), H+ (molecule.C00080). Products: adenosine thiamine triphosphate (molecule.ecocyc.CPD0-1095), phosphate (molecule.ecocyc.Pi).

## Annotation

PROTON + THIAMINE-PYROPHOSPHATE + ADP -> CPD0-1095 + Pi; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.ecocyc.MONOMER0-2838|protein.ecocyc.MONOMER0-2838]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1095|molecule.ecocyc.CPD0-1095]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5291`

## Notes

PROTON + THIAMINE-PYROPHOSPHATE + ADP -> CPD0-1095 + Pi; direction=REVERSIBLE
