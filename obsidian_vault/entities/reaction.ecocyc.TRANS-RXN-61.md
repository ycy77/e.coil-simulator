---
entity_id: "reaction.ecocyc.TRANS-RXN-61"
entity_type: "reaction"
name: "3-(3-hydroxyphenyl)propanoate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-61"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-(3-hydroxyphenyl)propanoate:proton symport

`reaction.ecocyc.TRANS-RXN-61`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-61`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + 3-HYDROXYPHENYL-PROPIONATE -> PROTON + 3-HYDROXYPHENYL-PROPIONATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + 3-HYDROXYPHENYL-PROPIONATE -> PROTON + 3-HYDROXYPHENYL-PROPIONATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by mhpT (protein.P77589). Substrates: H+ (molecule.C00080), 3-(3-Hydroxyphenyl)propanoic acid (molecule.C11457). Products: H+ (molecule.C00080), 3-(3-Hydroxyphenyl)propanoic acid (molecule.C11457).

## Annotation

PROTON + 3-HYDROXYPHENYL-PROPIONATE -> PROTON + 3-HYDROXYPHENYL-PROPIONATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77589|protein.P77589]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11457|molecule.C11457]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11457|molecule.C11457]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-61`

## Notes

PROTON + 3-HYDROXYPHENYL-PROPIONATE -> PROTON + 3-HYDROXYPHENYL-PROPIONATE; direction=REVERSIBLE
