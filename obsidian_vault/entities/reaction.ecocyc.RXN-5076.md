---
entity_id: "reaction.ecocyc.RXN-5076"
entity_type: "reaction"
name: "xanthine:proton symport"
source_database: "EcoCyc"
source_id: "RXN-5076"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# xanthine:proton symport

`reaction.ecocyc.RXN-5076`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-5076`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

XANTHINE + PROTON -> XANTHINE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: XANTHINE + PROTON -> XANTHINE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by xanP (protein.P0AGM9), xanQ (protein.P67444), rutG (protein.P75892), uacT (protein.Q46821). Substrates: H+ (molecule.C00080), Xanthine (molecule.C00385). Products: H+ (molecule.C00080), Xanthine (molecule.C00385).

## Annotation

XANTHINE + PROTON -> XANTHINE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0AGM9|protein.P0AGM9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P67444|protein.P67444]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75892|protein.P75892]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46821|protein.Q46821]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-5076`

## Notes

XANTHINE + PROTON -> XANTHINE + PROTON; direction=REVERSIBLE
