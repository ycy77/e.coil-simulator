---
entity_id: "reaction.ecocyc.ORNCARBAMTRANSFER-RXN"
entity_type: "reaction"
name: "ORNCARBAMTRANSFER-RXN"
source_database: "EcoCyc"
source_id: "ORNCARBAMTRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ORNCARBAMTRANSFER-RXN

`reaction.ecocyc.ORNCARBAMTRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ORNCARBAMTRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the sixth step in arginine biosynthesis. It is also part of the urea cycle. EcoCyc reaction equation: L-ORNITHINE + CARBAMOYL-P -> PROTON + L-CITRULLINE + Pi; direction=REVERSIBLE. This is the sixth step in arginine biosynthesis. It is also part of the urea cycle.

## Biological Role

Catalyzed by ornithine carbamoyltransferase (complex.ecocyc.ORNCARBAMTRANSFERF-CPLX), ornithine carbamoyltransferase (complex.ecocyc.ORNCARBAMTRANSFERI-CPLX). Substrates: L-Ornithine (molecule.C00077), Carbamoyl phosphate (molecule.C00169). Products: H+ (molecule.C00080), L-Citrulline (molecule.C00327), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.ARGSYN-PWY` L-arginine biosynthesis I (via L-ornithine) (EcoCyc)

## Annotation

This is the sixth step in arginine biosynthesis. It is also part of the urea cycle.

## Pathways

- `ecocyc.ARGSYN-PWY` L-arginine biosynthesis I (via L-ornithine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.ORNCARBAMTRANSFERF-CPLX|complex.ecocyc.ORNCARBAMTRANSFERF-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ORNCARBAMTRANSFERI-CPLX|complex.ecocyc.ORNCARBAMTRANSFERI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00327|molecule.C00327]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.L-2-AMINOPENTANOIC-ACID|molecule.ecocyc.L-2-AMINOPENTANOIC-ACID]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-DELTA-PHOSPHONOACETYL-L-ORNITHINE|molecule.ecocyc.N-DELTA-PHOSPHONOACETYL-L-ORNITHINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Sulfhydryl-Reagents|molecule.ecocyc.Sulfhydryl-Reagents]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ORNCARBAMTRANSFER-RXN`

## Notes

L-ORNITHINE + CARBAMOYL-P -> PROTON + L-CITRULLINE + Pi; direction=REVERSIBLE
