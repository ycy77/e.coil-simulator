---
entity_id: "reaction.ecocyc.TRANS-RXN-262"
entity_type: "reaction"
name: "asparagine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-262"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# asparagine:proton symport

`reaction.ecocyc.TRANS-RXN-262`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-262`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + ASN -> PROTON + ASN; direction=REVERSIBLE EcoCyc reaction equation: PROTON + ASN -> PROTON + ASN; direction=REVERSIBLE.

## Biological Role

Catalyzed by ansP (protein.P77610). Substrates: H+ (molecule.C00080), L-Asparagine (molecule.C00152). Products: H+ (molecule.C00080), L-Asparagine (molecule.C00152).

## Annotation

PROTON + ASN -> PROTON + ASN; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77610|protein.P77610]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-262`

## Notes

PROTON + ASN -> PROTON + ASN; direction=REVERSIBLE
