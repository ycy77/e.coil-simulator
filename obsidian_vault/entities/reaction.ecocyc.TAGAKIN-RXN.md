---
entity_id: "reaction.ecocyc.TAGAKIN-RXN"
entity_type: "reaction"
name: "TAGAKIN-RXN"
source_database: "EcoCyc"
source_id: "TAGAKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TAGAKIN-RXN

`reaction.ecocyc.TAGAKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TAGAKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the galactitol catabolism pathway. EcoCyc reaction equation: TAGATOSE-6-PHOSPHATE + ATP -> PROTON + TAGATOSE-1-6-DIPHOSPHATE + ADP; direction=LEFT-TO-RIGHT. This reaction is part of the galactitol catabolism pathway.

## Biological Role

Catalyzed by 6-phosphofructokinase 2 (complex.ecocyc.6PFK-2-CPX). Substrates: ATP (molecule.C00002), D-Tagatose 6-phosphate (molecule.C01097). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Tagatose 1,6-bisphosphate (molecule.C03785).

## Enriched Pathways

- `ecocyc.GALACTITOLCAT-PWY` galactitol degradation (EcoCyc)

## Annotation

This reaction is part of the galactitol catabolism pathway.

## Pathways

- `ecocyc.GALACTITOLCAT-PWY` galactitol degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.6PFK-2-CPX|complex.ecocyc.6PFK-2-CPX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03785|molecule.C03785]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01097|molecule.C01097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TAGAKIN-RXN`

## Notes

TAGATOSE-6-PHOSPHATE + ATP -> PROTON + TAGATOSE-1-6-DIPHOSPHATE + ADP; direction=LEFT-TO-RIGHT
