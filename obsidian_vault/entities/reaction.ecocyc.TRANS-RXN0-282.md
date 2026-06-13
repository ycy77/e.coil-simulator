---
entity_id: "reaction.ecocyc.TRANS-RXN0-282"
entity_type: "reaction"
name: "TRANS-RXN0-282"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-282"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-282

`reaction.ecocyc.TRANS-RXN0-282`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-282`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

3-PHENYLPROPIONATE -> 3-PHENYLPROPIONATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 3-PHENYLPROPIONATE -> 3-PHENYLPROPIONATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hcaT (protein.Q47142). Substrates: Phenylpropanoate (molecule.C05629). Products: Phenylpropanoate (molecule.C05629).

## Annotation

3-PHENYLPROPIONATE -> 3-PHENYLPROPIONATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.Q47142|protein.Q47142]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C05629|molecule.C05629]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05629|molecule.C05629]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-282`

## Notes

3-PHENYLPROPIONATE -> 3-PHENYLPROPIONATE; direction=LEFT-TO-RIGHT
