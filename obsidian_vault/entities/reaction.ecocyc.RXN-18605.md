---
entity_id: "reaction.ecocyc.RXN-18605"
entity_type: "reaction"
name: "RXN-18605"
source_database: "EcoCyc"
source_id: "RXN-18605"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18605

`reaction.ecocyc.RXN-18605`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18605`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

a-reduced-NrfB-protein + NITRITE + PROTON -> AMMONIUM + WATER + an-oxidized-NrfB-protein; direction=LEFT-TO-RIGHT EcoCyc reaction equation: a-reduced-NrfB-protein + NITRITE + PROTON -> AMMONIUM + WATER + an-oxidized-NrfB-protein; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cytochrome c552 nitrite reductase (complex.ecocyc.CPLX0-12840). Substrates: H+ (molecule.C00080), Nitrite (molecule.C00088). Products: H2O (molecule.C00001), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY0-1585` formate to nitrite electron transfer (EcoCyc)

## Annotation

a-reduced-NrfB-protein + NITRITE + PROTON -> AMMONIUM + WATER + an-oxidized-NrfB-protein; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1585` formate to nitrite electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-12840|complex.ecocyc.CPLX0-12840]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18605`

## Notes

a-reduced-NrfB-protein + NITRITE + PROTON -> AMMONIUM + WATER + an-oxidized-NrfB-protein; direction=LEFT-TO-RIGHT
