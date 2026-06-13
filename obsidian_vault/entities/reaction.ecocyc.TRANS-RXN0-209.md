---
entity_id: "reaction.ecocyc.TRANS-RXN0-209"
entity_type: "reaction"
name: "D-gluconate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-209"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-gluconate:proton symport

`reaction.ecocyc.TRANS-RXN0-209`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-209`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + GLUCONATE -> PROTON + GLUCONATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + GLUCONATE -> PROTON + GLUCONATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by gntP (protein.P0AC94), gntU (protein.P0AC96), idnT (protein.P39344), gntT (protein.P39835). Substrates: H+ (molecule.C00080), D-Gluconic acid (molecule.C00257). Products: H+ (molecule.C00080), D-Gluconic acid (molecule.C00257).

## Annotation

PROTON + GLUCONATE -> PROTON + GLUCONATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0AC94|protein.P0AC94]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AC96|protein.P0AC96]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39344|protein.P39344]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39835|protein.P39835]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-209`

## Notes

PROTON + GLUCONATE -> PROTON + GLUCONATE; direction=REVERSIBLE
