---
entity_id: "reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN

`reaction.ecocyc.ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

An early reaction in the synthesis of lysine, methionine and threonine. EcoCyc reaction equation: NADP + Pi + L-ASPARTATE-SEMIALDEHYDE -> PROTON + NADPH + L-BETA-ASPARTYL-P; direction=REVERSIBLE. An early reaction in the synthesis of lysine, methionine and threonine.

## Biological Role

Catalyzed by aspartate-semialdehyde dehydrogenase (complex.ecocyc.ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX). Substrates: NADP+ (molecule.C00006), L-Aspartate 4-semialdehyde (molecule.C00441), phosphate (molecule.ecocyc.Pi). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 4-Phospho-L-aspartate (molecule.C03082).

## Enriched Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)
- `ecocyc.HOMOSERSYN-PWY` L-homoserine biosynthesis (EcoCyc)

## Annotation

An early reaction in the synthesis of lysine, methionine and threonine.

## Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)
- `ecocyc.HOMOSERSYN-PWY` L-homoserine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (19)

- `catalyzes` <-- [[complex.ecocyc.ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX|complex.ecocyc.ASP-SEMIALDEHYDE-DEHYDROGENASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03082|molecule.C03082]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00441|molecule.C00441]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00491|molecule.C00491]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BORATE|molecule.ecocyc.BORATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1224|molecule.ecocyc.CPD0-1224]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETATE|molecule.ecocyc.IODOACETATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.TRIS|molecule.ecocyc.TRIS]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN`

## Notes

NADP + Pi + L-ASPARTATE-SEMIALDEHYDE -> PROTON + NADPH + L-BETA-ASPARTYL-P; direction=REVERSIBLE
