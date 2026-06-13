---
entity_id: "reaction.ecocyc.RXN0-7248"
entity_type: "reaction"
name: "RXN0-7248"
source_database: "EcoCyc"
source_id: "RXN0-7248"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7248

`reaction.ecocyc.RXN0-7248`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7248`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This reaction models vectorial import of exogenous LCFA by membrane-associated acyl-CoA synthetases, as described in and . Fatty acids must partition into the membrane and flip prior to extraction by acyl-CoA synthetases, resulting in a requirement for an energized membrane . This instance reaction is used to avoid instantiation errors caused by ambiguity between cis-vaccenate and oleate masses. EcoCyc reaction equation: CPD-9245 + ATP + CO-A + PROTON -> CPD-10269 + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction models vectorial import of exogenous LCFA by membrane-associated acyl-CoA synthetases, as described in and . Fatty acids must partition into the membrane and flip prior to extraction by acyl-CoA synthetases, resulting in a requirement for an energized membrane . This instance reaction is used to avoid instantiation errors caused by ambiguity between cis-vaccenate and oleate masses.

## Biological Role

Catalyzed by long-chain-fatty-acid—CoA ligase (complex.ecocyc.ACYLCOASYN-CPLX), fadK (protein.P38135). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), H+ (molecule.C00080), (9Z)-Hexadecenoic acid (molecule.C08362). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), Palmitoleoyl-CoA (molecule.C21072).

## Annotation

This reaction models vectorial import of exogenous LCFA by membrane-associated acyl-CoA synthetases, as described in and . Fatty acids must partition into the membrane and flip prior to extraction by acyl-CoA synthetases, resulting in a requirement for an energized membrane . This instance reaction is used to avoid instantiation errors caused by ambiguity between cis-vaccenate and oleate masses.

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.ACYLCOASYN-CPLX|complex.ecocyc.ACYLCOASYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P38135|protein.P38135]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C21072|molecule.C21072]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C08362|molecule.C08362]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1385|molecule.ecocyc.CPD0-1385]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HSCN|molecule.ecocyc.HSCN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7248`

## Notes

CPD-9245 + ATP + CO-A + PROTON -> CPD-10269 + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
