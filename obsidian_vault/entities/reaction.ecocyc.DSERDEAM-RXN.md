---
entity_id: "reaction.ecocyc.DSERDEAM-RXN"
entity_type: "reaction"
name: "DSERDEAM-RXN"
source_database: "EcoCyc"
source_id: "DSERDEAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DSERDEAM-RXN

`reaction.ecocyc.DSERDEAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DSERDEAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction converts D-serine, which is a growth inhibitor, to pyruvate and ammonia. EcoCyc reaction equation: D-SERINE -> PYRUVATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction converts D-serine, which is a growth inhibitor, to pyruvate and ammonia.

## Biological Role

Catalyzed by serine hydroxymethyltransferase (complex.ecocyc.GLYOHMETRANS-CPLX), dsdA (protein.P00926). Substrates: D-Serine (molecule.C00740). Products: Pyruvate (molecule.C00022), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

This reaction converts D-serine, which is a growth inhibitor, to pyruvate and ammonia.

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `activates` <-- [[molecule.C00101|molecule.C00101]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.GLYOHMETRANS-CPLX|complex.ecocyc.GLYOHMETRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P00926|protein.P00926]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00820|molecule.C00820]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.23-Diaminopropanoate|molecule.ecocyc.23-Diaminopropanoate]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.ALLO-THR|molecule.ecocyc.ALLO-THR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1507|molecule.ecocyc.CPD0-1507]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DSERDEAM-RXN`

## Notes

D-SERINE -> PYRUVATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
