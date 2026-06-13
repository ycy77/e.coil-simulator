---
entity_id: "reaction.ecocyc.RXN0-5390"
entity_type: "reaction"
name: "RXN0-5390"
source_database: "EcoCyc"
source_id: "RXN0-5390"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5390

`reaction.ecocyc.RXN0-5390`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5390`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1158 + WATER -> PROTON + CPD0-1159 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1158 + WATER -> PROTON + CPD0-1159 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acyl-CoA thioesterase II (complex.ecocyc.THIOESTERII-CPLX), fadM (protein.P77712). Substrates: H2O (molecule.C00001), (3E,5Z)-tetradeca-3,5-dienoyl-CoA (molecule.ecocyc.CPD0-1158). Products: CoA (molecule.C00010), H+ (molecule.C00080), (3E,5Z)-tetradeca-3,5-dienoate (molecule.ecocyc.CPD0-1159).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD0-1158 + WATER -> PROTON + CPD0-1159 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.THIOESTERII-CPLX|complex.ecocyc.THIOESTERII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77712|protein.P77712]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1159|molecule.ecocyc.CPD0-1159]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1158|molecule.ecocyc.CPD0-1158]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5390`

## Notes

CPD0-1158 + WATER -> PROTON + CPD0-1159 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
