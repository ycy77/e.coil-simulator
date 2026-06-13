---
entity_id: "reaction.ecocyc.TRANS-RXN-21"
entity_type: "reaction"
name: "galactose:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-21"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# galactose:proton symport

`reaction.ecocyc.TRANS-RXN-21`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-21`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + D-galactopyranose -> PROTON + D-galactopyranose; direction=REVERSIBLE EcoCyc reaction equation: PROTON + D-galactopyranose -> PROTON + D-galactopyranose; direction=REVERSIBLE.

## Biological Role

Catalyzed by galP (protein.P0AEP1). Substrates: H+ (molecule.C00080), D-Galactose (molecule.C00124). Products: H+ (molecule.C00080), D-Galactose (molecule.C00124).

## Annotation

PROTON + D-galactopyranose -> PROTON + D-galactopyranose; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEP1|protein.P0AEP1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-21`

## Notes

PROTON + D-galactopyranose -> PROTON + D-galactopyranose; direction=REVERSIBLE
