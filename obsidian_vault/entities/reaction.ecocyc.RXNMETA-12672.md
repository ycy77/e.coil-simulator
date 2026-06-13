---
entity_id: "reaction.ecocyc.RXNMETA-12672"
entity_type: "reaction"
name: "RXNMETA-12672"
source_database: "EcoCyc"
source_id: "RXNMETA-12672"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXNMETA-12672

`reaction.ecocyc.RXNMETA-12672`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXNMETA-12672`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPDMETA-13650 + NADP + WATER -> CPD0-2364 + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPDMETA-13650 + NADP + WATER -> CPD0-2364 + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by oxepin-CoA hydrolase [multifunctional] (complex.ecocyc.CPLX0-8538). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), 3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde (molecule.C19946). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 3-Oxo-5,6-dehydrosuberyl-CoA (molecule.C19945).

## Enriched Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Annotation

CPDMETA-13650 + NADP + WATER -> CPD0-2364 + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8538|complex.ecocyc.CPLX0-8538]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C19945|molecule.C19945]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C19946|molecule.C19946]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXNMETA-12672`

## Notes

CPDMETA-13650 + NADP + WATER -> CPD0-2364 + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
