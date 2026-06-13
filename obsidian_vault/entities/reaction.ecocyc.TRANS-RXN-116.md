---
entity_id: "reaction.ecocyc.TRANS-RXN-116"
entity_type: "reaction"
name: "cytosine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-116"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# cytosine:proton symport

`reaction.ecocyc.TRANS-RXN-116`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-116`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CYTOSINE -> PROTON + CYTOSINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CYTOSINE -> PROTON + CYTOSINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by codB (protein.P0AA82). Substrates: H+ (molecule.C00080), Cytosine (molecule.C00380). Products: H+ (molecule.C00080), Cytosine (molecule.C00380).

## Annotation

PROTON + CYTOSINE -> PROTON + CYTOSINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AA82|protein.P0AA82]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00380|molecule.C00380]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00380|molecule.C00380]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-116`

## Notes

PROTON + CYTOSINE -> PROTON + CYTOSINE; direction=LEFT-TO-RIGHT
