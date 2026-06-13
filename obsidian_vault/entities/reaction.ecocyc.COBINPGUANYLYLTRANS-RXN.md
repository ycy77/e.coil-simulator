---
entity_id: "reaction.ecocyc.COBINPGUANYLYLTRANS-RXN"
entity_type: "reaction"
name: "COBINPGUANYLYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "COBINPGUANYLYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# COBINPGUANYLYLTRANS-RXN

`reaction.ecocyc.COBINPGUANYLYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:COBINPGUANYLYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of cobalamin biosynthesis. EcoCyc reaction equation: PROTON + ADENOSYLCOBINAMIDE-P + GTP -> ADENOSYLCOBINAMIDE-GDP + PPI; direction=LEFT-TO-RIGHT. This reaction is part of cobalamin biosynthesis.

## Biological Role

Catalyzed by cobinamide-P guanylyltransferase / cobinamide kinase (complex.ecocyc.COBU-CPLX). Substrates: GTP (molecule.C00044), H+ (molecule.C00080), Adenosyl cobinamide phosphate (molecule.C06509). Products: Diphosphate (molecule.C00013), Adenosine-GDP-cobinamide (molecule.C06510).

## Enriched Pathways

- `ecocyc.COBALSYN-PWY` superpathway of adenosylcobalamin salvage from cobinamide I (EcoCyc)
- `ecocyc.PWY-7971` adenosylcobinamide-GDP salvage from cobinamide I (EcoCyc)

## Annotation

This reaction is part of cobalamin biosynthesis.

## Pathways

- `ecocyc.COBALSYN-PWY` superpathway of adenosylcobalamin salvage from cobinamide I (EcoCyc)
- `ecocyc.PWY-7971` adenosylcobinamide-GDP salvage from cobinamide I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.COBU-CPLX|complex.ecocyc.COBU-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06510|molecule.C06510]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06509|molecule.C06509]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:COBINPGUANYLYLTRANS-RXN`

## Notes

PROTON + ADENOSYLCOBINAMIDE-P + GTP -> ADENOSYLCOBINAMIDE-GDP + PPI; direction=LEFT-TO-RIGHT
