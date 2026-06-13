---
entity_id: "reaction.ecocyc.TRANS-RXN-387"
entity_type: "reaction"
name: "TRANS-RXN-387"
source_database: "EcoCyc"
source_id: "TRANS-RXN-387"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-387

`reaction.ecocyc.TRANS-RXN-387`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-387`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Represents (imperfectly) the flipping of lyso-cardiolipins across the inner membrane. EcoCyc reaction equation: a-lyso-cardiolipin -> a-lyso-cardiolipin; direction=PHYSIOL-LEFT-TO-RIGHT. Represents (imperfectly) the flipping of lyso-cardiolipins across the inner membrane.

## Biological Role

Catalyzed by lplT (protein.P39196). Substrates: a lyso-cardiolipin (molecule.ecocyc.a-lyso-cardiolipin). Products: a lyso-cardiolipin (molecule.ecocyc.a-lyso-cardiolipin).

## Annotation

Represents (imperfectly) the flipping of lyso-cardiolipins across the inner membrane.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P39196|protein.P39196]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.a-lyso-cardiolipin|molecule.ecocyc.a-lyso-cardiolipin]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.a-lyso-cardiolipin|molecule.ecocyc.a-lyso-cardiolipin]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-387`

## Notes

a-lyso-cardiolipin -> a-lyso-cardiolipin; direction=PHYSIOL-LEFT-TO-RIGHT
