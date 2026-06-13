---
entity_id: "reaction.ecocyc.TRANS-RXN0-616"
entity_type: "reaction"
name: "D-cystine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-616"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-cystine:proton symport

`reaction.ecocyc.TRANS-RXN0-616`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-616`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD0-1564 + PROTON -> CPD0-1564 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD0-1564 + PROTON -> CPD0-1564 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by tcyP (protein.P77529). Substrates: H+ (molecule.C00080), D-cystine (molecule.ecocyc.CPD0-1564). Products: H+ (molecule.C00080), D-cystine (molecule.ecocyc.CPD0-1564).

## Annotation

CPD0-1564 + PROTON -> CPD0-1564 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77529|protein.P77529]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1564|molecule.ecocyc.CPD0-1564]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1564|molecule.ecocyc.CPD0-1564]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-616`

## Notes

CPD0-1564 + PROTON -> CPD0-1564 + PROTON; direction=REVERSIBLE
