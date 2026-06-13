---
entity_id: "reaction.ecocyc.RXN0-5256"
entity_type: "reaction"
name: "hydrogen:menaquinone oxidoreductase"
source_database: "EcoCyc"
source_id: "RXN0-5256"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# hydrogen:menaquinone oxidoreductase

`reaction.ecocyc.RXN0-5256`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5256`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinones + PROTON + HYDROGEN-MOLECULE -> Menaquinols + PROTON; direction=REVERSIBLE EcoCyc reaction equation: Menaquinones + PROTON + HYDROGEN-MOLECULE -> Menaquinols + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by hydrogenase 1, oxygen tolerant hydrogenase (complex.ecocyc.CPLX0-8167). Substrates: H+ (molecule.C00080), Hydrogen (molecule.C00282), Menaquinone (molecule.C00828). Products: H+ (molecule.C00080), Menaquinol (molecule.C05819).

## Annotation

Menaquinones + PROTON + HYDROGEN-MOLECULE -> Menaquinols + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8167|complex.ecocyc.CPLX0-8167]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00282|molecule.C00282]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00237|molecule.C00237]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2841|molecule.ecocyc.CPD-2841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-BROMOSUCCINIMIDE|molecule.ecocyc.N-BROMOSUCCINIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5256`

## Notes

Menaquinones + PROTON + HYDROGEN-MOLECULE -> Menaquinols + PROTON; direction=REVERSIBLE
