---
entity_id: "reaction.ecocyc.TRANS-RXN-112"
entity_type: "reaction"
name: "L-rhamnose:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-112"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-rhamnose:proton symport

`reaction.ecocyc.TRANS-RXN-112`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-112`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + L-rhamnose -> PROTON + L-rhamnose; direction=REVERSIBLE EcoCyc reaction equation: PROTON + L-rhamnose -> PROTON + L-rhamnose; direction=REVERSIBLE.

## Biological Role

Catalyzed by rhaT (protein.P27125). Substrates: H+ (molecule.C00080), L-Rhamnose (molecule.C00507). Products: H+ (molecule.C00080), L-Rhamnose (molecule.C00507).

## Annotation

PROTON + L-rhamnose -> PROTON + L-rhamnose; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27125|protein.P27125]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00507|molecule.C00507]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00507|molecule.C00507]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-112`

## Notes

PROTON + L-rhamnose -> PROTON + L-rhamnose; direction=REVERSIBLE
