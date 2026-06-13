---
entity_id: "reaction.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-RXN"
entity_type: "reaction"
name: "7-ALPHA-HYDROXYSTEROID-DEH-RXN"
source_database: "EcoCyc"
source_id: "7-ALPHA-HYDROXYSTEROID-DEH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 7-ALPHA-HYDROXYSTEROID-DEH-RXN

`reaction.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:7-ALPHA-HYDROXYSTEROID-DEH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + CHOLATE -> PROTON + NADH + CHOLANATE2; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NAD + CHOLATE -> PROTON + NADH + CHOLANATE2; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 7-α-hydroxysteroid dehydrogenase (complex.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-CPLX). Substrates: NAD+ (molecule.C00003), Cholic acid (molecule.C00695). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3α,12α-dihydroxy-7-oxo-5β-cholan-24-oate (molecule.ecocyc.CHOLANATE2).

## Annotation

NAD + CHOLATE -> PROTON + NADH + CHOLANATE2; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `catalyzes` <-- [[complex.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-CPLX|complex.ecocyc.7-ALPHA-HYDROXYSTEROID-DEH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CHOLANATE2|molecule.ecocyc.CHOLANATE2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00695|molecule.C00695]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1693|molecule.ecocyc.CPD0-1693]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1694|molecule.ecocyc.CPD0-1694]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1695|molecule.ecocyc.CPD0-1695]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1696|molecule.ecocyc.CPD0-1696]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLPYROCARBONATE|molecule.ecocyc.DIETHYLPYROCARBONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-BROMOSUCCINIMIDE|molecule.ecocyc.N-BROMOSUCCINIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:7-ALPHA-HYDROXYSTEROID-DEH-RXN`

## Notes

NAD + CHOLATE -> PROTON + NADH + CHOLANATE2; direction=PHYSIOL-LEFT-TO-RIGHT
