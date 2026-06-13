---
entity_id: "reaction.ecocyc.TRANS-RXN0-270"
entity_type: "reaction"
name: "L-leucine:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-270"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-leucine:proton antiport

`reaction.ecocyc.TRANS-RXN0-270`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-270`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + LEU -> PROTON + LEU; direction=REVERSIBLE EcoCyc reaction equation: PROTON + LEU -> PROTON + LEU; direction=REVERSIBLE.

## Biological Role

Catalyzed by yjeH (protein.P39277), leuE (protein.P76249). Substrates: H+ (molecule.C00080), L-Leucine (molecule.C00123). Products: H+ (molecule.C00080), L-Leucine (molecule.C00123).

## Annotation

PROTON + LEU -> PROTON + LEU; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39277|protein.P39277]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76249|protein.P76249]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-270`

## Notes

PROTON + LEU -> PROTON + LEU; direction=REVERSIBLE
