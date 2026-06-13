---
entity_id: "reaction.ecocyc.TRANS-RXN0-623"
entity_type: "reaction"
name: "TRANS-RXN0-623"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-623"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-623

`reaction.ecocyc.TRANS-RXN0-623`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-623`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction models vectorial import of exogenous LCFA by membrane-associated acyl-CoA synthetases, as described in and . Fatty acids must partition into the membrane and flip prior to extraction by acyl-CoA synthetases, resulting in a requirement for an energized membrane . EcoCyc reaction equation: CPD66-39 + ATP + CO-A + PROTON -> Saturated-Fatty-Acyl-CoA + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction models vectorial import of exogenous LCFA by membrane-associated acyl-CoA synthetases, as described in and . Fatty acids must partition into the membrane and flip prior to extraction by acyl-CoA synthetases, resulting in a requirement for an energized membrane .

## Biological Role

Catalyzed by long-chain-fatty-acid—CoA ligase (complex.ecocyc.ACYLCOASYN-CPLX), fadK (protein.P38135). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), H+ (molecule.C00080), a 2,3,4-saturated fatty acid (molecule.ecocyc.CPD66-39). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), a 2,3,4-saturated fatty acyl CoA (molecule.ecocyc.Saturated-Fatty-Acyl-CoA).

## Annotation

This reaction models vectorial import of exogenous LCFA by membrane-associated acyl-CoA synthetases, as described in and . Fatty acids must partition into the membrane and flip prior to extraction by acyl-CoA synthetases, resulting in a requirement for an energized membrane .

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.ACYLCOASYN-CPLX|complex.ecocyc.ACYLCOASYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P38135|protein.P38135]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Saturated-Fatty-Acyl-CoA|molecule.ecocyc.Saturated-Fatty-Acyl-CoA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD66-39|molecule.ecocyc.CPD66-39]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1385|molecule.ecocyc.CPD0-1385]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HSCN|molecule.ecocyc.HSCN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-623`

## Notes

CPD66-39 + ATP + CO-A + PROTON -> Saturated-Fatty-Acyl-CoA + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
