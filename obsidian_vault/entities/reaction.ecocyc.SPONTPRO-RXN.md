---
entity_id: "reaction.ecocyc.SPONTPRO-RXN"
entity_type: "reaction"
name: "SPONTPRO-RXN"
source_database: "EcoCyc"
source_id: "SPONTPRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SPONTPRO-RXN

`reaction.ecocyc.SPONTPRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SPONTPRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + WATER + L-DELTA1-PYRROLINE_5-CARBOXYLATE -> L-GLUTAMATE_GAMMA-SEMIALDEHYDE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + WATER + L-DELTA1-PYRROLINE_5-CARBOXYLATE -> L-GLUTAMATE_GAMMA-SEMIALDEHYDE; direction=REVERSIBLE.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), (S)-1-Pyrroline-5-carboxylate (molecule.C03912). Products: L-Glutamate 5-semialdehyde (molecule.C01165).

## Enriched Pathways

- `ecocyc.PROSYN-PWY` L-proline biosynthesis I (from L-glutamate) (EcoCyc)
- `ecocyc.PROUT-PWY-I` proline degradation (EcoCyc)

## Annotation

PROTON + WATER + L-DELTA1-PYRROLINE_5-CARBOXYLATE -> L-GLUTAMATE_GAMMA-SEMIALDEHYDE; direction=REVERSIBLE

## Pathways

- `ecocyc.PROSYN-PWY` L-proline biosynthesis I (from L-glutamate) (EcoCyc)
- `ecocyc.PROUT-PWY-I` proline degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C01165|molecule.C01165]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03912|molecule.C03912]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SPONTPRO-RXN`

## Notes

PROTON + WATER + L-DELTA1-PYRROLINE_5-CARBOXYLATE -> L-GLUTAMATE_GAMMA-SEMIALDEHYDE; direction=REVERSIBLE
