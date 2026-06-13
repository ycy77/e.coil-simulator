---
entity_id: "reaction.ecocyc.TRANS-RXN0-227"
entity_type: "reaction"
name: "L-galactonate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-227"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-galactonate:proton symport

`reaction.ecocyc.TRANS-RXN0-227`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-227`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD0-1083 -> CPD0-1083 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: PROTON + CPD0-1083 -> CPD0-1083 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by lgoT (protein.P39398). Substrates: H+ (molecule.C00080), L-Galactonate (molecule.C15930). Products: H+ (molecule.C00080), L-Galactonate (molecule.C15930).

## Annotation

PROTON + CPD0-1083 -> CPD0-1083 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P39398|protein.P39398]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15930|molecule.C15930]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15930|molecule.C15930]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-227`

## Notes

PROTON + CPD0-1083 -> CPD0-1083 + PROTON; direction=REVERSIBLE
