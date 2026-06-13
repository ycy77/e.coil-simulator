---
entity_id: "reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN"
entity_type: "reaction"
name: "CYSTATHIONINE-BETA-LYASE-RXN"
source_database: "EcoCyc"
source_id: "CYSTATHIONINE-BETA-LYASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CYSTATHIONINE-BETA-LYASE-RXN

`reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CYSTATHIONINE-BETA-LYASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third committed step in methionine synthesis. EcoCyc reaction equation: L-CYSTATHIONINE + WATER -> AMMONIUM + PYRUVATE + HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT. This is the third committed step in methionine synthesis.

## Biological Role

Catalyzed by negative regulator of MalT activity/cystathionine β-lyase (complex.ecocyc.CPLX0-8092), cystathionine β-lyase / L-cysteine desulfhydrase / alanine racemase (complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX). Substrates: H2O (molecule.C00001), L-Cystathionine (molecule.C02291). Products: Pyruvate (molecule.C00022), L-Homocysteine (molecule.C00155), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.HOMOSER-METSYN-PWY` L-methionine biosynthesis I (EcoCyc)

## Annotation

This is the third committed step in methionine synthesis.

## Pathways

- `ecocyc.HOMOSER-METSYN-PWY` L-methionine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8092|complex.ecocyc.CPLX0-8092]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX|complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02291|molecule.C02291]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13353|molecule.ecocyc.CPD-13353]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1636|molecule.ecocyc.CPD0-1636]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CYSTATHIONINE-BETA-LYASE-RXN`

## Notes

L-CYSTATHIONINE + WATER -> AMMONIUM + PYRUVATE + HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
