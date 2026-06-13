---
entity_id: "reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN

`reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + NAD + SUCC-S-ALD -> PROTON + NADH + SUC; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + NAD + SUCC-S-ALD -> PROTON + NADH + SUC; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by succinate semialdehyde dehydrogenase (NAD(P)+) Sad (complex.ecocyc.CPLX0-7687), puuC (protein.P23883). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), Succinate semialdehyde (molecule.C00232). Products: NADH (molecule.C00004), Succinate (molecule.C00042), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-6535` 4-aminobutanoate degradation I (EcoCyc)

## Annotation

WATER + NAD + SUCC-S-ALD -> PROTON + NADH + SUC; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6535` 4-aminobutanoate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7687|complex.ecocyc.CPLX0-7687]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P23883|protein.P23883]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00232|molecule.C00232]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN`

## Notes

WATER + NAD + SUCC-S-ALD -> PROTON + NADH + SUC; direction=PHYSIOL-LEFT-TO-RIGHT
