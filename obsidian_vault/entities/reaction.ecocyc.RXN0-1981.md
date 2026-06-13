---
entity_id: "reaction.ecocyc.RXN0-1981"
entity_type: "reaction"
name: "acetate:Na+ symport"
source_database: "EcoCyc"
source_id: "RXN0-1981"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# acetate:Na+ symport

`reaction.ecocyc.RXN0-1981`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1981`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ACET + NA+ -> ACET + NA+; direction=REVERSIBLE EcoCyc reaction equation: ACET + NA+ -> ACET + NA+; direction=REVERSIBLE.

## Biological Role

Catalyzed by acetate/glycolate:cation symporter (complex.ecocyc.CPLX0-7955). Substrates: Acetate (molecule.C00033), Sodium cation (molecule.C01330). Products: Acetate (molecule.C00033), Sodium cation (molecule.C01330).

## Annotation

ACET + NA+ -> ACET + NA+; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7955|complex.ecocyc.CPLX0-7955]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1981`

## Notes

ACET + NA+ -> ACET + NA+; direction=REVERSIBLE
