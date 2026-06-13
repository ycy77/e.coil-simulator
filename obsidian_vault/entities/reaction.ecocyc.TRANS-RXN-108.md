---
entity_id: "reaction.ecocyc.TRANS-RXN-108"
entity_type: "reaction"
name: "nucleoside:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-108"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# nucleoside:proton symport

`reaction.ecocyc.TRANS-RXN-108`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-108`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + Nucleosides -> PROTON + Nucleosides; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + Nucleosides -> PROTON + Nucleosides; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), a nucleoside (molecule.ecocyc.Nucleosides). Products: H+ (molecule.C00080), a nucleoside (molecule.ecocyc.Nucleosides).

## Annotation

PROTON + Nucleosides -> PROTON + Nucleosides; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nucleosides|molecule.ecocyc.Nucleosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Nucleosides|molecule.ecocyc.Nucleosides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-108`

## Notes

PROTON + Nucleosides -> PROTON + Nucleosides; direction=LEFT-TO-RIGHT
