---
entity_id: "reaction.ecocyc.SORB6PDEHYDROG-RXN"
entity_type: "reaction"
name: "SORB6PDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "SORB6PDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SORB6PDEHYDROG-RXN

`reaction.ecocyc.SORB6PDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SORB6PDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in sorbitol (glucitol) metabolism. EcoCyc reaction equation: D-SORBITOL-6-P + NAD -> CPD-15709 + NADH + PROTON; direction=REVERSIBLE. This is a reaction in sorbitol (glucitol) metabolism.

## Biological Role

Catalyzed by sorbitol-6-phosphate 2-dehydrogenase (complex.ecocyc.SORB6PDEHYDROG-CPLX). Substrates: NAD+ (molecule.C00003), Sorbitol 6-phosphate (molecule.C01096). Products: NADH (molecule.C00004), H+ (molecule.C00080), keto-D-fructose 6-phosphate (molecule.ecocyc.CPD-15709).

## Enriched Pathways

- `ecocyc.SORBDEG-PWY` D-sorbitol degradation II (EcoCyc)

## Annotation

This is a reaction in sorbitol (glucitol) metabolism.

## Pathways

- `ecocyc.SORBDEG-PWY` D-sorbitol degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.SORB6PDEHYDROG-CPLX|complex.ecocyc.SORB6PDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15709|molecule.ecocyc.CPD-15709]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01096|molecule.C01096]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-15157|molecule.ecocyc.CPD-15157]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-15979|molecule.ecocyc.CPD-15979]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-18734|molecule.ecocyc.CPD-18734]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLPYROCARBONATE|molecule.ecocyc.DIETHYLPYROCARBONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SORB6PDEHYDROG-RXN`

## Notes

D-SORBITOL-6-P + NAD -> CPD-15709 + NADH + PROTON; direction=REVERSIBLE
