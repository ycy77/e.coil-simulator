---
entity_id: "reaction.ecocyc.TRANS-RXN-335"
entity_type: "reaction"
name: "pyruvate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-335"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# pyruvate:proton symport

`reaction.ecocyc.TRANS-RXN-335`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-335`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PYRUVATE + PROTON -> PYRUVATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: PYRUVATE + PROTON -> PYRUVATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by cstA (protein.P15078), btsT (protein.P39396). Substrates: Pyruvate (molecule.C00022), H+ (molecule.C00080). Products: Pyruvate (molecule.C00022), H+ (molecule.C00080).

## Annotation

PYRUVATE + PROTON -> PYRUVATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P15078|protein.P15078]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39396|protein.P39396]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.3-BROMOPYRUVATE|molecule.ecocyc.3-BROMOPYRUVATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-8179|molecule.ecocyc.CPD-8179]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-335`

## Notes

PYRUVATE + PROTON -> PYRUVATE + PROTON; direction=REVERSIBLE
