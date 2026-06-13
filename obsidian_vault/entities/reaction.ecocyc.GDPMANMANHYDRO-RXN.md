---
entity_id: "reaction.ecocyc.GDPMANMANHYDRO-RXN"
entity_type: "reaction"
name: "GDPMANMANHYDRO-RXN"
source_database: "EcoCyc"
source_id: "GDPMANMANHYDRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GDPMANMANHYDRO-RXN

`reaction.ecocyc.GDPMANMANHYDRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GDPMANMANHYDRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of GDP-mannose utilization. EcoCyc reaction equation: GDP-MANNOSE + WATER -> MANNOSE + PROTON + GDP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of GDP-mannose utilization.

## Biological Role

Catalyzed by GDP-mannose mannosyl hydrolase (complex.ecocyc.CPLX0-7712). Substrates: H2O (molecule.C00001), GDP-mannose (molecule.C00096). Products: GDP (molecule.C00035), H+ (molecule.C00080), D-Mannose (molecule.C00159).

## Annotation

This reaction is part of GDP-mannose utilization.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7712|complex.ecocyc.CPLX0-7712]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00159|molecule.C00159]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00096|molecule.C00096]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GDPMANMANHYDRO-RXN`

## Notes

GDP-MANNOSE + WATER -> MANNOSE + PROTON + GDP; direction=PHYSIOL-LEFT-TO-RIGHT
