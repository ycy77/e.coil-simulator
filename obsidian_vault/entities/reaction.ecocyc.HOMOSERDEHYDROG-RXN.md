---
entity_id: "reaction.ecocyc.HOMOSERDEHYDROG-RXN"
entity_type: "reaction"
name: "HOMOSERDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "HOMOSERDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HOMOSERDEHYDROG-RXN

`reaction.ecocyc.HOMOSERDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HOMOSERDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD-P-OR-NOP + HOMO-SER -> NADH-P-OR-NOP + L-ASPARTATE-SEMIALDEHYDE + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: NAD-P-OR-NOP + HOMO-SER -> NADH-P-OR-NOP + L-ASPARTATE-SEMIALDEHYDE + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by fused aspartate kinase/homoserine dehydrogenase 1 (complex.ecocyc.ASPKINIHOMOSERDEHYDROGI-CPLX), fused aspartate kinase/homoserine dehydrogenase 2 (complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX). Substrates: L-Homoserine (molecule.C00263), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), L-Aspartate 4-semialdehyde (molecule.C00441), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.HOMOSERSYN-PWY` L-homoserine biosynthesis (EcoCyc)

## Annotation

NAD-P-OR-NOP + HOMO-SER -> NADH-P-OR-NOP + L-ASPARTATE-SEMIALDEHYDE + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.HOMOSERSYN-PWY` L-homoserine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `activates` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ASPKINIHOMOSERDEHYDROGI-CPLX|complex.ecocyc.ASPKINIHOMOSERDEHYDROGI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX|complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00441|molecule.C00441]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1224|molecule.ecocyc.CPD0-1224]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:HOMOSERDEHYDROG-RXN`

## Notes

NAD-P-OR-NOP + HOMO-SER -> NADH-P-OR-NOP + L-ASPARTATE-SEMIALDEHYDE + PROTON; direction=RIGHT-TO-LEFT
