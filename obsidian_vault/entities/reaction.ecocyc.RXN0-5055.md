---
entity_id: "reaction.ecocyc.RXN0-5055"
entity_type: "reaction"
name: "RXN0-5055"
source_database: "EcoCyc"
source_id: "RXN0-5055"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5055

`reaction.ecocyc.RXN0-5055`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5055`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETYL-COA + carboxybiotin-L-lysine-in-BCCP-dimers -> MALONYL-COA + biotin-L-lysine-in-BCCP-dimers; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ACETYL-COA + carboxybiotin-L-lysine-in-BCCP-dimers -> MALONYL-COA + biotin-L-lysine-in-BCCP-dimers; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acetyl-CoA carboxyltransferase (complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX). Substrates: Acetyl-CoA (molecule.C00024), a [carboxyl-carrier protein dimer]-N6-carboxybiotinyl-L-lysine (molecule.ecocyc.carboxybiotin-L-lysine-in-BCCP-dimers). Products: Malonyl-CoA (molecule.C00083), a [biotin carboxyl-carrier-protein dimer]-N6-biotinyl-L-lysine (molecule.ecocyc.biotin-L-lysine-in-BCCP-dimers).

## Enriched Pathways

- `ecocyc.PWY-4381` fatty acid biosynthesis initiation (type II) (EcoCyc)
- `ecocyc.PWY0-1264` malonyl-CoA biosynthesis via biotin-carboxyl carrier protein (EcoCyc)

## Annotation

ACETYL-COA + carboxybiotin-L-lysine-in-BCCP-dimers -> MALONYL-COA + biotin-L-lysine-in-BCCP-dimers; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-4381` fatty acid biosynthesis initiation (type II) (EcoCyc)
- `ecocyc.PWY0-1264` malonyl-CoA biosynthesis via biotin-carboxyl carrier protein (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX|complex.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00083|molecule.C00083]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.biotin-L-lysine-in-BCCP-dimers|molecule.ecocyc.biotin-L-lysine-in-BCCP-dimers]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.carboxybiotin-L-lysine-in-BCCP-dimers|molecule.ecocyc.carboxybiotin-L-lysine-in-BCCP-dimers]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01909|molecule.C01909]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1598|molecule.ecocyc.CPD0-1598]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5055`

## Notes

ACETYL-COA + carboxybiotin-L-lysine-in-BCCP-dimers -> MALONYL-COA + biotin-L-lysine-in-BCCP-dimers; direction=PHYSIOL-LEFT-TO-RIGHT
