---
entity_id: "reaction.ecocyc.TRANS-RXN-285"
entity_type: "reaction"
name: "L-cystine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-285"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-cystine:proton symport

`reaction.ecocyc.TRANS-RXN-285`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-285`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

L-CYSTINE + PROTON -> L-CYSTINE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: L-CYSTINE + PROTON -> L-CYSTINE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by tcyP (protein.P77529). Substrates: H+ (molecule.C00080), L-Cystine (molecule.C00491). Products: H+ (molecule.C00080), L-Cystine (molecule.C00491).

## Annotation

L-CYSTINE + PROTON -> L-CYSTINE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P77529|protein.P77529]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00491|molecule.C00491]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00491|molecule.C00491]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1562|molecule.ecocyc.CPD0-1562]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1564|molecule.ecocyc.CPD0-1564]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-285`

## Notes

L-CYSTINE + PROTON -> L-CYSTINE + PROTON; direction=REVERSIBLE
