---
entity_id: "reaction.ecocyc.RXN-18604"
entity_type: "reaction"
name: "RXN-18604"
source_database: "EcoCyc"
source_id: "RXN-18604"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18604

`reaction.ecocyc.RXN-18604`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18604`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinols + an-oxidized-NrfB-protein -> Menaquinones + a-reduced-NrfB-protein + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Menaquinols + an-oxidized-NrfB-protein -> Menaquinones + a-reduced-NrfB-protein + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by putative menaquinol-cytochrome c reductase NrfCD (complex.ecocyc.CPLX0-8238). Substrates: Menaquinol (molecule.C05819). Products: H+ (molecule.C00080), Menaquinone (molecule.C00828).

## Enriched Pathways

- `ecocyc.PWY0-1585` formate to nitrite electron transfer (EcoCyc)

## Annotation

Menaquinols + an-oxidized-NrfB-protein -> Menaquinones + a-reduced-NrfB-protein + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1585` formate to nitrite electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8238|complex.ecocyc.CPLX0-8238]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18604`

## Notes

Menaquinols + an-oxidized-NrfB-protein -> Menaquinones + a-reduced-NrfB-protein + PROTON; direction=LEFT-TO-RIGHT
