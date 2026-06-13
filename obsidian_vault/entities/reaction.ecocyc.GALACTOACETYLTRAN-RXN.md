---
entity_id: "reaction.ecocyc.GALACTOACETYLTRAN-RXN"
entity_type: "reaction"
name: "GALACTOACETYLTRAN-RXN"
source_database: "EcoCyc"
source_id: "GALACTOACETYLTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GALACTOACETYLTRAN-RXN

`reaction.ecocyc.GALACTOACETYLTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GALACTOACETYLTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of galactose, galactoside and glucose catabolism. EcoCyc reaction equation: Beta-D-Galactosides + ACETYL-COA -> 6-Acetyl-Beta-D-Galactosides + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT. Part of galactose, galactoside and glucose catabolism.

## Biological Role

Catalyzed by galactoside O-acetyltransferase (complex.ecocyc.GALACTOACETYLTRAN-CPLX). Substrates: Acetyl-CoA (molecule.C00024), a β-D-galactoside (molecule.ecocyc.Beta-D-Galactosides). Products: CoA (molecule.C00010), a 6-acetyl-β-D-galactoside (molecule.ecocyc.6-Acetyl-Beta-D-Galactosides).

## Annotation

Part of galactose, galactoside and glucose catabolism.

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.GALACTOACETYLTRAN-CPLX|complex.ecocyc.GALACTOACETYLTRAN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.6-Acetyl-Beta-D-Galactosides|molecule.ecocyc.6-Acetyl-Beta-D-Galactosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Beta-D-Galactosides|molecule.ecocyc.Beta-D-Galactosides]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1607|molecule.ecocyc.CPD0-1607]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1608|molecule.ecocyc.CPD0-1608]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1609|molecule.ecocyc.CPD0-1609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GALACTOACETYLTRAN-RXN`

## Notes

Beta-D-Galactosides + ACETYL-COA -> 6-Acetyl-Beta-D-Galactosides + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
