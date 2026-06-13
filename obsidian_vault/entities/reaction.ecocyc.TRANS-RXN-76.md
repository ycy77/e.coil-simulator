---
entity_id: "reaction.ecocyc.TRANS-RXN-76"
entity_type: "reaction"
name: "tryptophan:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-76"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# tryptophan:proton symport

`reaction.ecocyc.TRANS-RXN-76`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-76`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + TRP -> PROTON + TRP; direction=REVERSIBLE EcoCyc reaction equation: PROTON + TRP -> PROTON + TRP; direction=REVERSIBLE.

## Biological Role

Catalyzed by mtr (protein.P0AAD2), aroP (protein.P15993), tnaB (protein.P23173). Substrates: L-Tryptophan (molecule.C00078), H+ (molecule.C00080). Products: L-Tryptophan (molecule.C00078), H+ (molecule.C00080).

## Annotation

PROTON + TRP -> PROTON + TRP; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AAD2|protein.P0AAD2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P15993|protein.P15993]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P23173|protein.P23173]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-76`

## Notes

PROTON + TRP -> PROTON + TRP; direction=REVERSIBLE
