---
entity_id: "reaction.ecocyc.1.3.1.9-RXN"
entity_type: "reaction"
name: "1.3.1.9-RXN"
source_database: "EcoCyc"
source_id: "1.3.1.9-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.3.1.9-RXN

`reaction.ecocyc.1.3.1.9-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.3.1.9-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACYL-ACP + NAD -> TRANS-D2-ENOYL-ACP + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: ACYL-ACP + NAD -> TRANS-D2-ENOYL-ACP + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by enoyl-[acyl-carrier-protein] reductase (complex.ecocyc.CPLX0-8006). Substrates: NAD+ (molecule.C00003). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Annotation

ACYL-ACP + NAD -> TRANS-D2-ENOYL-ACP + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8006|complex.ecocyc.CPLX0-8006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.3.1.9-RXN`

## Notes

ACYL-ACP + NAD -> TRANS-D2-ENOYL-ACP + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
