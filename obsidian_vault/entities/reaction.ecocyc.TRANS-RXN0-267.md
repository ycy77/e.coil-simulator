---
entity_id: "reaction.ecocyc.TRANS-RXN0-267"
entity_type: "reaction"
name: "tripeptide:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-267"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# tripeptide:proton symport

`reaction.ecocyc.TRANS-RXN0-267`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-267`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + TRIPEPTIDES -> PROTON + TRIPEPTIDES; direction=REVERSIBLE EcoCyc reaction equation: PROTON + TRIPEPTIDES -> PROTON + TRIPEPTIDES; direction=REVERSIBLE.

## Biological Role

Catalyzed by dtpB (protein.P36837), dtpC (protein.P39276), dtpA (protein.P77304). Substrates: H+ (molecule.C00080), a tripeptide (molecule.ecocyc.TRIPEPTIDES). Products: H+ (molecule.C00080), a tripeptide (molecule.ecocyc.TRIPEPTIDES).

## Annotation

PROTON + TRIPEPTIDES -> PROTON + TRIPEPTIDES; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P36837|protein.P36837]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39276|protein.P39276]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77304|protein.P77304]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TRIPEPTIDES|molecule.ecocyc.TRIPEPTIDES]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.TRIPEPTIDES|molecule.ecocyc.TRIPEPTIDES]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-267`

## Notes

PROTON + TRIPEPTIDES -> PROTON + TRIPEPTIDES; direction=REVERSIBLE
