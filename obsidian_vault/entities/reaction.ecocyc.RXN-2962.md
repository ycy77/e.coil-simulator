---
entity_id: "reaction.ecocyc.RXN-2962"
entity_type: "reaction"
name: "RXN-2962"
source_database: "EcoCyc"
source_id: "RXN-2962"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-2962

`reaction.ecocyc.RXN-2962`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-2962`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD-P-OR-NOP + S-HYDROXYMETHYLGLUTATHIONE -> NADH-P-OR-NOP + CPD-548 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NAD-P-OR-NOP + S-HYDROXYMETHYLGLUTATHIONE -> NADH-P-OR-NOP + CPD-548 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by S-(hydroxymethyl)glutathione dehydrogenase (complex.ecocyc.ADHC-CPLX). Substrates: S-(Hydroxymethyl)glutathione (molecule.C14180), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), S-Formylglutathione (molecule.C01031), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.PWY-1801` formaldehyde oxidation II (glutathione-dependent) (EcoCyc)

## Annotation

NAD-P-OR-NOP + S-HYDROXYMETHYLGLUTATHIONE -> NADH-P-OR-NOP + CPD-548 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-1801` formaldehyde oxidation II (glutathione-dependent) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ADHC-CPLX|complex.ecocyc.ADHC-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01031|molecule.C01031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C14180|molecule.C14180]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-2962`

## Notes

NAD-P-OR-NOP + S-HYDROXYMETHYLGLUTATHIONE -> NADH-P-OR-NOP + CPD-548 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
