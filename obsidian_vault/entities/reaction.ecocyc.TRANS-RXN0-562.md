---
entity_id: "reaction.ecocyc.TRANS-RXN0-562"
entity_type: "reaction"
name: "TRANS-RXN0-562"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-562"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-562

`reaction.ecocyc.TRANS-RXN0-562`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-562`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

HYPOXANTHINE + PROTON -> HYPOXANTHINE + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: HYPOXANTHINE + PROTON -> HYPOXANTHINE + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by ghxP (protein.P0AF52), ghxQ (protein.Q46817). Substrates: H+ (molecule.C00080), Hypoxanthine (molecule.C00262). Products: H+ (molecule.C00080), Hypoxanthine (molecule.C00262).

## Annotation

HYPOXANTHINE + PROTON -> HYPOXANTHINE + PROTON; direction=RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P0AF52|protein.P0AF52]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46817|protein.Q46817]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00242|molecule.C00242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-15916|molecule.ecocyc.CPD-15916]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5721|molecule.ecocyc.CPD-5721]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1143|molecule.ecocyc.CPD0-1143]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1932|molecule.ecocyc.CPD0-1932]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-562`

## Notes

HYPOXANTHINE + PROTON -> HYPOXANTHINE + PROTON; direction=RIGHT-TO-LEFT
