---
entity_id: "reaction.ecocyc.TRANS-RXN-42"
entity_type: "reaction"
name: "potassium:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-42"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# potassium:proton antiport

`reaction.ecocyc.TRANS-RXN-42`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-42`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + K+ -> PROTON + K+; direction=REVERSIBLE EcoCyc reaction equation: PROTON + K+ -> PROTON + K+; direction=REVERSIBLE.

## Biological Role

Catalyzed by K+ : H+ antiporter KefC (complex.ecocyc.CPLX0-7819), mdfA (protein.P0AEY8), chaA (protein.P31801), kefB (protein.P45522). Substrates: H+ (molecule.C00080), Potassium cation (molecule.C00238). Products: H+ (molecule.C00080), Potassium cation (molecule.C00238).

## Annotation

PROTON + K+ -> PROTON + K+; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[protein.P0A754|protein.P0A754]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7819|complex.ecocyc.CPLX0-7819]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AEY8|protein.P0AEY8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P31801|protein.P31801]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P45522|protein.P45522]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-42`

## Notes

PROTON + K+ -> PROTON + K+; direction=REVERSIBLE
