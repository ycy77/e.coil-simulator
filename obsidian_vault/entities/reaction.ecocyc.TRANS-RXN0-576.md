---
entity_id: "reaction.ecocyc.TRANS-RXN0-576"
entity_type: "reaction"
name: "tellurite:Na+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-576"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# tellurite:Na+ symport

`reaction.ecocyc.TRANS-RXN0-576`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-576`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-4544 + NA+ -> CPD-4544 + NA+; direction=REVERSIBLE EcoCyc reaction equation: CPD-4544 + NA+ -> CPD-4544 + NA+; direction=REVERSIBLE.

## Biological Role

Catalyzed by acetate/glycolate:cation symporter (complex.ecocyc.CPLX0-7955). Substrates: Sodium cation (molecule.C01330), tellurite (molecule.ecocyc.CPD-4544). Products: Sodium cation (molecule.C01330), tellurite (molecule.ecocyc.CPD-4544).

## Annotation

CPD-4544 + NA+ -> CPD-4544 + NA+; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7955|complex.ecocyc.CPLX0-7955]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-4544|molecule.ecocyc.CPD-4544]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-4544|molecule.ecocyc.CPD-4544]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-576`

## Notes

CPD-4544 + NA+ -> CPD-4544 + NA+; direction=REVERSIBLE
