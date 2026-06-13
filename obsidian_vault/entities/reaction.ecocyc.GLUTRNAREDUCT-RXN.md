---
entity_id: "reaction.ecocyc.GLUTRNAREDUCT-RXN"
entity_type: "reaction"
name: "GLUTRNAREDUCT-RXN"
source_database: "EcoCyc"
source_id: "GLUTRNAREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTRNAREDUCT-RXN

`reaction.ecocyc.GLUTRNAREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTRNAREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in porphyrin biosynthesis, one of two reactions in the synthesis of 5-aminolevulinate by the C5 pathway. EcoCyc reaction equation: GLUTAMATE-1-SEMIALDEHYDE + NADP + GLT-tRNAs -> Charged-GLT-tRNAs + NADPH + PROTON; direction=RIGHT-TO-LEFT. This is the second reaction in porphyrin biosynthesis, one of two reactions in the synthesis of 5-aminolevulinate by the C5 pathway.

## Biological Role

Catalyzed by glutamyl-tRNA reductase (complex.ecocyc.CPLX0-3741). Substrates: NADP+ (molecule.C00006), (S)-4-Amino-5-oxopentanoate (molecule.C03741). Products: NADPH (molecule.C00005), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)

## Annotation

This is the second reaction in porphyrin biosynthesis, one of two reactions in the synthesis of 5-aminolevulinate by the C5 pathway.

## Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3741|complex.ecocyc.CPLX0-3741]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03741|molecule.C03741]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLUTRNAREDUCT-RXN`

## Notes

GLUTAMATE-1-SEMIALDEHYDE + NADP + GLT-tRNAs -> Charged-GLT-tRNAs + NADPH + PROTON; direction=RIGHT-TO-LEFT
