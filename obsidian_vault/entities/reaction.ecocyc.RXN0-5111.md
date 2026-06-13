---
entity_id: "reaction.ecocyc.RXN0-5111"
entity_type: "reaction"
name: "glycolate:Na+ symport"
source_database: "EcoCyc"
source_id: "RXN0-5111"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glycolate:Na+ symport

`reaction.ecocyc.RXN0-5111`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5111`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GLYCOLLATE + NA+ -> GLYCOLLATE + NA+; direction=REVERSIBLE EcoCyc reaction equation: GLYCOLLATE + NA+ -> GLYCOLLATE + NA+; direction=REVERSIBLE.

## Biological Role

Catalyzed by acetate/glycolate:cation symporter (complex.ecocyc.CPLX0-7955). Substrates: Glycolate (molecule.C00160), Sodium cation (molecule.C01330). Products: Glycolate (molecule.C00160), Sodium cation (molecule.C01330).

## Annotation

GLYCOLLATE + NA+ -> GLYCOLLATE + NA+; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7955|complex.ecocyc.CPLX0-7955]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5111`

## Notes

GLYCOLLATE + NA+ -> GLYCOLLATE + NA+; direction=REVERSIBLE
