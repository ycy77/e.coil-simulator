---
entity_id: "reaction.ecocyc.RXNMETA-12671"
entity_type: "reaction"
name: "RXNMETA-12671"
source_database: "EcoCyc"
source_id: "RXNMETA-12671"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXNMETA-12671

`reaction.ecocyc.RXNMETA-12671`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXNMETA-12671`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2363 + WATER -> CPDMETA-13650; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2363 + WATER -> CPDMETA-13650; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by oxepin-CoA hydrolase [multifunctional] (complex.ecocyc.CPLX0-8538). Substrates: H2O (molecule.C00001), 2-Oxepin-2(3H)-ylideneacetyl-CoA (molecule.C19975). Products: 3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde (molecule.C19946).

## Enriched Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Annotation

CPD0-2363 + WATER -> CPDMETA-13650; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8538|complex.ecocyc.CPLX0-8538]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C19946|molecule.C19946]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C19975|molecule.C19975]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-2558|molecule.ecocyc.CPD0-2558]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXNMETA-12671`

## Notes

CPD0-2363 + WATER -> CPDMETA-13650; direction=PHYSIOL-LEFT-TO-RIGHT
