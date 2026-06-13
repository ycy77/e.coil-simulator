---
entity_id: "reaction.ecocyc.RXN0-2481"
entity_type: "reaction"
name: "RXN0-2481"
source_database: "EcoCyc"
source_id: "RXN0-2481"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2481

`reaction.ecocyc.RXN0-2481`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2481`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Hydrophilic-Solute-Or-Ion-LT-600Da -> Hydrophilic-Solute-Or-Ion-LT-600Da; direction=REVERSIBLE EcoCyc reaction equation: Hydrophilic-Solute-Or-Ion-LT-600Da -> Hydrophilic-Solute-Or-Ion-LT-600Da; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534), ompN (protein.P77747). Substrates: hydrophilic solute or ion < 600 Da (molecule.ecocyc.Hydrophilic-Solute-Or-Ion-LT-600Da). Products: hydrophilic solute or ion < 600 Da (molecule.ecocyc.Hydrophilic-Solute-Or-Ion-LT-600Da).

## Annotation

Hydrophilic-Solute-Or-Ion-LT-600Da -> Hydrophilic-Solute-Or-Ion-LT-600Da; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77747|protein.P77747]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Hydrophilic-Solute-Or-Ion-LT-600Da|molecule.ecocyc.Hydrophilic-Solute-Or-Ion-LT-600Da]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Hydrophilic-Solute-Or-Ion-LT-600Da|molecule.ecocyc.Hydrophilic-Solute-Or-Ion-LT-600Da]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00750|molecule.C00750]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-2481`

## Notes

Hydrophilic-Solute-Or-Ion-LT-600Da -> Hydrophilic-Solute-Or-Ion-LT-600Da; direction=REVERSIBLE
