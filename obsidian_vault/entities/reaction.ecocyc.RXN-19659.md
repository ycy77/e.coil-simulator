---
entity_id: "reaction.ecocyc.RXN-19659"
entity_type: "reaction"
name: "RXN-19659"
source_database: "EcoCyc"
source_id: "RXN-19659"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19659

`reaction.ecocyc.RXN-19659`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19659`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CARBAMATE + WATER + PROTON -> AMMONIUM + HCO3; direction=REVERSIBLE EcoCyc reaction equation: CARBAMATE + WATER + PROTON -> AMMONIUM + HCO3; direction=REVERSIBLE.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Carbamate (molecule.C01563). Products: HCO3- (molecule.C00288), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY0-41` allantoin degradation IV (anaerobic) (EcoCyc)

## Annotation

CARBAMATE + WATER + PROTON -> AMMONIUM + HCO3; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-41` allantoin degradation IV (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01563|molecule.C01563]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19659`

## Notes

CARBAMATE + WATER + PROTON -> AMMONIUM + HCO3; direction=REVERSIBLE
