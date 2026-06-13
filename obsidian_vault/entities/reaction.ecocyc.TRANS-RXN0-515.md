---
entity_id: "reaction.ecocyc.TRANS-RXN0-515"
entity_type: "reaction"
name: "lactate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-515"
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

`reaction.ecocyc.TRANS-RXN0-515`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-515`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

D-LACTATE + PROTON -> D-LACTATE + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: D-LACTATE + PROTON -> D-LACTATE + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lldP (protein.P33231), glcA (protein.Q46839). Substrates: H+ (molecule.C00080), (R)-Lactate (molecule.C00256). Products: H+ (molecule.C00080), (R)-Lactate (molecule.C00256).

## Annotation

D-LACTATE + PROTON -> D-LACTATE + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P33231|protein.P33231]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46839|protein.Q46839]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-515`

## Notes

D-LACTATE + PROTON -> D-LACTATE + PROTON; direction=LEFT-TO-RIGHT
