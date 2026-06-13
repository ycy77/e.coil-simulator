---
entity_id: "reaction.ecocyc.RXN0-3942"
entity_type: "reaction"
name: "RXN0-3942"
source_database: "EcoCyc"
source_id: "RXN0-3942"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3942

`reaction.ecocyc.RXN0-3942`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3942`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-9000 + WATER -> 4-AMINO-BUTYRATE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-9000 + WATER -> 4-AMINO-BUTYRATE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by γ-glutamyl-γ-aminobutyrate hydrolase (complex.ecocyc.CPLX0-3943). Substrates: H2O (molecule.C00001), 4-(L-gamma-Glutamylamino)butanoate (molecule.C15767). Products: L-Glutamate (molecule.C00025), 4-Aminobutanoate (molecule.C00334).

## Enriched Pathways

- `ecocyc.PWY0-1221` putrescine degradation II (EcoCyc)

## Annotation

CPD-9000 + WATER -> 4-AMINO-BUTYRATE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1221` putrescine degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3943|complex.ecocyc.CPLX0-3943]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15767|molecule.C15767]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3942`

## Notes

CPD-9000 + WATER -> 4-AMINO-BUTYRATE + GLT; direction=PHYSIOL-LEFT-TO-RIGHT
