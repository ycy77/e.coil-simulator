---
entity_id: "reaction.ecocyc.RXN-21072"
entity_type: "reaction"
name: "RXN-21072"
source_database: "EcoCyc"
source_id: "RXN-21072"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21072

`reaction.ecocyc.RXN-21072`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21072`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ala-tRNA-Pro + WATER -> PRO-tRNAs + L-ALPHA-ALANINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Ala-tRNA-Pro + WATER -> PRO-tRNAs + L-ALPHA-ALANINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by proline—tRNA ligase (complex.ecocyc.PROS-CPLX). Substrates: H2O (molecule.C00001). Products: L-Alanine (molecule.C00041), H+ (molecule.C00080).

## Annotation

Ala-tRNA-Pro + WATER -> PRO-tRNAs + L-ALPHA-ALANINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.PROS-CPLX|complex.ecocyc.PROS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21072`

## Notes

Ala-tRNA-Pro + WATER -> PRO-tRNAs + L-ALPHA-ALANINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
