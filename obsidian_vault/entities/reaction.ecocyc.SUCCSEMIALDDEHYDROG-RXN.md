---
entity_id: "reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN"
entity_type: "reaction"
name: "SUCCSEMIALDDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "SUCCSEMIALDDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SUCCSEMIALDDEHYDROG-RXN

`reaction.ecocyc.SUCCSEMIALDDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUCCSEMIALDDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the 4-aminobutyrate (GABA) degradation pathway. EcoCyc reaction equation: SUCC-S-ALD + NADP + WATER -> SUC + NADPH + PROTON; direction=LEFT-TO-RIGHT. This reaction is part of the 4-aminobutyrate (GABA) degradation pathway.

## Biological Role

Catalyzed by succinate-semialdehyde dehydrogenase (NADP+) GabD (complex.ecocyc.CPLX0-7688). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), Succinate semialdehyde (molecule.C00232). Products: NADPH (molecule.C00005), Succinate (molecule.C00042), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-6537` 4-aminobutanoate degradation II (EcoCyc)

## Annotation

This reaction is part of the 4-aminobutyrate (GABA) degradation pathway.

## Pathways

- `ecocyc.PWY-6537` 4-aminobutanoate degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7688|complex.ecocyc.CPLX0-7688]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00232|molecule.C00232]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C07209|molecule.C07209]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SUCCSEMIALDDEHYDROG-RXN`

## Notes

SUCC-S-ALD + NADP + WATER -> SUC + NADPH + PROTON; direction=LEFT-TO-RIGHT
