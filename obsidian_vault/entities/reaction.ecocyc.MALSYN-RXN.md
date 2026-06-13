---
entity_id: "reaction.ecocyc.MALSYN-RXN"
entity_type: "reaction"
name: "MALSYN-RXN"
source_database: "EcoCyc"
source_id: "MALSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "glyoxylate-acetate condensation"
---

# MALSYN-RXN

`reaction.ecocyc.MALSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MALSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETYL-COA + WATER + GLYOX -> PROTON + MAL + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ACETYL-COA + WATER + GLYOX -> PROTON + MAL + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aceB (protein.P08997), glcB (protein.P37330). Substrates: H2O (molecule.C00001), Acetyl-CoA (molecule.C00024), Glyoxylate (molecule.C00048). Products: CoA (molecule.C00010), H+ (molecule.C00080), (S)-Malate (molecule.C00149).

## Enriched Pathways

- `ecocyc.GLYOXDEG-PWY` glycolate and glyoxylate degradation II (EcoCyc)
- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)
- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Annotation

ACETYL-COA + WATER + GLYOX -> PROTON + MAL + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.GLYOXDEG-PWY` glycolate and glyoxylate degradation II (EcoCyc)
- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)
- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P08997|protein.P08997]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37330|protein.P37330]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00209|molecule.C00209]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MALSYN-RXN`

## Notes

ACETYL-COA + WATER + GLYOX -> PROTON + MAL + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
