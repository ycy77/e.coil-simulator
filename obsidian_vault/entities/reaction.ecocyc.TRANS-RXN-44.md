---
entity_id: "reaction.ecocyc.TRANS-RXN-44"
entity_type: "reaction"
name: "xenobiotic:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-44"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# xenobiotic:proton antiport

`reaction.ecocyc.TRANS-RXN-44`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-44`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + Xenobiotic -> PROTON + Xenobiotic; direction=REVERSIBLE EcoCyc reaction equation: PROTON + Xenobiotic -> PROTON + Xenobiotic; direction=REVERSIBLE.

## Biological Role

Catalyzed by mdfA (protein.P0AEY8), bcr (protein.P28246), emrD (protein.P31442), mdtM (protein.P39386). Substrates: H+ (molecule.C00080). Products: H+ (molecule.C00080).

## Annotation

PROTON + Xenobiotic -> PROTON + Xenobiotic; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AEY8|protein.P0AEY8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P28246|protein.P28246]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P31442|protein.P31442]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39386|protein.P39386]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-44`

## Notes

PROTON + Xenobiotic -> PROTON + Xenobiotic; direction=REVERSIBLE
