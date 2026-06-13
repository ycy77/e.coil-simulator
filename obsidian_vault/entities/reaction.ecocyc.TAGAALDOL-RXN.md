---
entity_id: "reaction.ecocyc.TAGAALDOL-RXN"
entity_type: "reaction"
name: "TAGAALDOL-RXN"
source_database: "EcoCyc"
source_id: "TAGAALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TAGAALDOL-RXN

`reaction.ecocyc.TAGAALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TAGAALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the galactitol and N-acetylgalactosamine catabolism pathways. EcoCyc reaction equation: TAGATOSE-1-6-DIPHOSPHATE -> DIHYDROXY-ACETONE-PHOSPHATE + GAP; direction=LEFT-TO-RIGHT. This reaction is part of the galactitol and N-acetylgalactosamine catabolism pathways.

## Biological Role

Catalyzed by tagatose-1,6-bisphosphate aldolase 1 (complex.ecocyc.CPLX0-240), gatY (protein.P0C8J6). Substrates: D-Tagatose 1,6-bisphosphate (molecule.C03785). Products: Glycerone phosphate (molecule.C00111), D-Glyceraldehyde 3-phosphate (molecule.C00118).

## Enriched Pathways

- `ecocyc.GALACTITOLCAT-PWY` galactitol degradation (EcoCyc)

## Annotation

This reaction is part of the galactitol and N-acetylgalactosamine catabolism pathways.

## Pathways

- `ecocyc.GALACTITOLCAT-PWY` galactitol degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[protein.P0C8J8|protein.P0C8J8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P0C8K0|protein.P0C8K0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-240|complex.ecocyc.CPLX0-240]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0C8J6|protein.P0C8J6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03785|molecule.C03785]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TAGAALDOL-RXN`

## Notes

TAGATOSE-1-6-DIPHOSPHATE -> DIHYDROXY-ACETONE-PHOSPHATE + GAP; direction=LEFT-TO-RIGHT
