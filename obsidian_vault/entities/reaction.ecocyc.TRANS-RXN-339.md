---
entity_id: "reaction.ecocyc.TRANS-RXN-339"
entity_type: "reaction"
name: "carbonylcyanide m-chlorophenylhydrazone:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-339"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# carbonylcyanide m-chlorophenylhydrazone:proton antiport

`reaction.ecocyc.TRANS-RXN-339`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-339`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-7970 + PROTON -> CPD-7970 + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-7970 + PROTON -> CPD-7970 + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by emrD (protein.P31442). Substrates: H+ (molecule.C00080), carbonylcyanide m-chlorophenylhydrazone (molecule.ecocyc.CPD-7970). Products: H+ (molecule.C00080), carbonylcyanide m-chlorophenylhydrazone (molecule.ecocyc.CPD-7970).

## Annotation

CPD-7970 + PROTON -> CPD-7970 + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P31442|protein.P31442]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-339`

## Notes

CPD-7970 + PROTON -> CPD-7970 + PROTON; direction=REVERSIBLE
