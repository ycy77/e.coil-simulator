---
entity_id: "reaction.ecocyc.RXN0-6576"
entity_type: "reaction"
name: "RXN0-6576"
source_database: "EcoCyc"
source_id: "RXN0-6576"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6576

`reaction.ecocyc.RXN0-6576`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6576`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + CPD-4544 -> CPD0-2381 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + CPD-4544 -> CPD0-2381 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tellurite methyltransferase (complex.ecocyc.CPLX0-7913). Substrates: S-Adenosyl-L-methionine (molecule.C00019), tellurite (molecule.ecocyc.CPD-4544). Products: S-Adenosyl-L-homocysteine (molecule.C00021), methanetelluronate (molecule.ecocyc.CPD0-2381).

## Annotation

S-ADENOSYLMETHIONINE + CPD-4544 -> CPD0-2381 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7913|complex.ecocyc.CPLX0-7913]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2381|molecule.ecocyc.CPD0-2381]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-4544|molecule.ecocyc.CPD-4544]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6576`

## Notes

S-ADENOSYLMETHIONINE + CPD-4544 -> CPD0-2381 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
