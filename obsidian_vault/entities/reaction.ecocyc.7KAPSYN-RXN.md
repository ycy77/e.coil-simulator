---
entity_id: "reaction.ecocyc.7KAPSYN-RXN"
entity_type: "reaction"
name: "7KAPSYN-RXN"
source_database: "EcoCyc"
source_id: "7KAPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "7-KETO-8-AMINO-PELAGONIC ACID SYNTHETASE"
  - "7-KAP SYNTHETASE"
---

# 7KAPSYN-RXN

`reaction.ecocyc.7KAPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:7KAPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + L-ALPHA-ALANINE + CPD-558 -> CARBON-DIOXIDE + CO-A + 8-AMINO-7-OXONONANOATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + L-ALPHA-ALANINE + CPD-558 -> CARBON-DIOXIDE + CO-A + 8-AMINO-7-OXONONANOATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 8-amino-7-oxononanoate synthase (complex.ecocyc.7KAPSYN-CPLX). Substrates: L-Alanine (molecule.C00041), H+ (molecule.C00080), Pimeloyl-CoA (molecule.C01063). Products: CoA (molecule.C00010), CO2 (molecule.C00011), 8-Amino-7-oxononanoate (molecule.C01092).

## Annotation

PROTON + L-ALPHA-ALANINE + CPD-558 -> CARBON-DIOXIDE + CO-A + 8-AMINO-7-OXONONANOATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.7KAPSYN-CPLX|complex.ecocyc.7KAPSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01092|molecule.C01092]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01063|molecule.C01063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1636|molecule.ecocyc.CPD0-1636]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:7KAPSYN-RXN`

## Notes

PROTON + L-ALPHA-ALANINE + CPD-558 -> CARBON-DIOXIDE + CO-A + 8-AMINO-7-OXONONANOATE; direction=PHYSIOL-LEFT-TO-RIGHT
