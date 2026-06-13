---
entity_id: "reaction.ecocyc.RXN0-3261"
entity_type: "reaction"
name: "RXN0-3261"
source_database: "EcoCyc"
source_id: "RXN0-3261"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3261

`reaction.ecocyc.RXN0-3261`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3261`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction is the stepwise removal of the two amino-terminal arginines from alkaline phosphatase isozyme 1, creating isozymes 2 and 3 in the process. EcoCyc reaction equation: Alkaline-Phosphatases + WATER -> ARG + Alkaloine-Phosphatase-With-Cleaved-Arg; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the stepwise removal of the two amino-terminal arginines from alkaline phosphatase isozyme 1, creating isozymes 2 and 3 in the process.

## Biological Role

Catalyzed by iap (protein.P10423). Substrates: H2O (molecule.C00001). Products: L-Arginine (molecule.C00062).

## Annotation

This reaction is the stepwise removal of the two amino-terminal arginines from alkaline phosphatase isozyme 1, creating isozymes 2 and 3 in the process.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P10423|protein.P10423]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3261`

## Notes

Alkaline-Phosphatases + WATER -> ARG + Alkaloine-Phosphatase-With-Cleaved-Arg; direction=PHYSIOL-LEFT-TO-RIGHT
