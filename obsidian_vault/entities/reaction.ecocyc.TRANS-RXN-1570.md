---
entity_id: "reaction.ecocyc.TRANS-RXN-1570"
entity_type: "reaction"
name: "TRANS-RXN-1570"
source_database: "EcoCyc"
source_id: "TRANS-RXN-1570"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-1570

`reaction.ecocyc.TRANS-RXN-1570`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-1570`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-2583 + PROTON -> CPD0-2583 + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2583 + PROTON -> CPD0-2583 + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ampG (protein.P0AE16). Substrates: H+ (molecule.C00080), GlcNAc-1,6-anhMurNAc-L-Ala-γ-D-Glu-meso-DAP-D-Ala-D-Ala (molecule.ecocyc.CPD0-2583). Products: H+ (molecule.C00080), GlcNAc-1,6-anhMurNAc-L-Ala-γ-D-Glu-meso-DAP-D-Ala-D-Ala (molecule.ecocyc.CPD0-2583).

## Annotation

CPD0-2583 + PROTON -> CPD0-2583 + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AE16|protein.P0AE16]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2583|molecule.ecocyc.CPD0-2583]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2583|molecule.ecocyc.CPD0-2583]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-1570`

## Notes

CPD0-2583 + PROTON -> CPD0-2583 + PROTON; direction=LEFT-TO-RIGHT
