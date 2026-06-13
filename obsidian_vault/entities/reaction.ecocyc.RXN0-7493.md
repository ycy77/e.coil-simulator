---
entity_id: "reaction.ecocyc.RXN0-7493"
entity_type: "reaction"
name: "RXN0-7493"
source_database: "EcoCyc"
source_id: "RXN0-7493"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7493

`reaction.ecocyc.RXN0-7493`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7493`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Represents the five-electron, six-proton reduction of nitric oxide to ammonium. Catalysis of this reaction by E. coli periplasmic cytochrome c nitrite reductase may contribute to cellular NO detoxification (see ). EcoCyc reaction equation: NITRIC-OXIDE + a-reduced-NrfB-protein + PROTON -> AMMONIUM + an-oxidized-NrfB-protein + WATER; direction=LEFT-TO-RIGHT. Represents the five-electron, six-proton reduction of nitric oxide to ammonium. Catalysis of this reaction by E. coli periplasmic cytochrome c nitrite reductase may contribute to cellular NO detoxification (see ).

## Biological Role

Catalyzed by cytochrome c552 nitrite reductase (complex.ecocyc.CPLX0-12840). Substrates: H+ (molecule.C00080), Nitric oxide (molecule.C00533). Products: H2O (molecule.C00001), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

Represents the five-electron, six-proton reduction of nitric oxide to ammonium. Catalysis of this reaction by E. coli periplasmic cytochrome c nitrite reductase may contribute to cellular NO detoxification (see ).

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-12840|complex.ecocyc.CPLX0-12840]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00533|molecule.C00533]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7493`

## Notes

NITRIC-OXIDE + a-reduced-NrfB-protein + PROTON -> AMMONIUM + an-oxidized-NrfB-protein + WATER; direction=LEFT-TO-RIGHT
