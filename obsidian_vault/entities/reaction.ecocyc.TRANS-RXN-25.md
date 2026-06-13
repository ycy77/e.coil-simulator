---
entity_id: "reaction.ecocyc.TRANS-RXN-25"
entity_type: "reaction"
name: "N-acetylneuraminate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-25"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# N-acetylneuraminate:proton symport

`reaction.ecocyc.TRANS-RXN-25`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-25`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

N-ACETYLNEURAMINATE + PROTON -> N-ACETYLNEURAMINATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: N-ACETYLNEURAMINATE + PROTON -> N-ACETYLNEURAMINATE + PROTON; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), N-Acetylneuraminate (molecule.C00270). Products: H+ (molecule.C00080), N-Acetylneuraminate (molecule.C00270).

## Annotation

N-ACETYLNEURAMINATE + PROTON -> N-ACETYLNEURAMINATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00270|molecule.C00270]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00270|molecule.C00270]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-25`

## Notes

N-ACETYLNEURAMINATE + PROTON -> N-ACETYLNEURAMINATE + PROTON; direction=REVERSIBLE
