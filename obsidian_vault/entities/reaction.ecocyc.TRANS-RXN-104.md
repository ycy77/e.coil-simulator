---
entity_id: "reaction.ecocyc.TRANS-RXN-104"
entity_type: "reaction"
name: "lactate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-104"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# lactate:proton symport

`reaction.ecocyc.TRANS-RXN-104`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-104`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + L-LACTATE -> PROTON + L-LACTATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + L-LACTATE -> PROTON + L-LACTATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by lldP (protein.P33231), glcA (protein.Q46839). Substrates: H+ (molecule.C00080), (S)-Lactate (molecule.C00186). Products: H+ (molecule.C00080), (S)-Lactate (molecule.C00186).

## Annotation

PROTON + L-LACTATE -> PROTON + L-LACTATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P33231|protein.P33231]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46839|protein.Q46839]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00186|molecule.C00186]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00186|molecule.C00186]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-104`

## Notes

PROTON + L-LACTATE -> PROTON + L-LACTATE; direction=REVERSIBLE
