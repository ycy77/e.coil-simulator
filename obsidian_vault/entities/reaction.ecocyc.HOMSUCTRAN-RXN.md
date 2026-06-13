---
entity_id: "reaction.ecocyc.HOMSUCTRAN-RXN"
entity_type: "reaction"
name: "HOMSUCTRAN-RXN"
source_database: "EcoCyc"
source_id: "HOMSUCTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HOMSUCTRAN-RXN

`reaction.ecocyc.HOMSUCTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HOMSUCTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first enzyme in the methionine biosynthetic pathway. EcoCyc reaction equation: HOMO-SER + SUC-COA -> O-SUCCINYL-L-HOMOSERINE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first enzyme in the methionine biosynthetic pathway.

## Biological Role

Catalyzed by homoserine O-succinyltransferase (complex.ecocyc.HOMSUCTRAN-CPLX). Substrates: Succinyl-CoA (molecule.C00091), L-Homoserine (molecule.C00263). Products: CoA (molecule.C00010), O-Succinyl-L-homoserine (molecule.C01118).

## Enriched Pathways

- `ecocyc.HOMOSER-METSYN-PWY` L-methionine biosynthesis I (EcoCyc)

## Annotation

This is the first enzyme in the methionine biosynthetic pathway.

## Pathways

- `ecocyc.HOMOSER-METSYN-PWY` L-methionine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.HOMSUCTRAN-CPLX|complex.ecocyc.HOMSUCTRAN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01118|molecule.C01118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00091|molecule.C00091]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.ALPHA-METHYLMETHIONINE|molecule.ecocyc.ALPHA-METHYLMETHIONINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLPYROCARBONATE|molecule.ecocyc.DIETHYLPYROCARBONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:HOMSUCTRAN-RXN`

## Notes

HOMO-SER + SUC-COA -> O-SUCCINYL-L-HOMOSERINE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
