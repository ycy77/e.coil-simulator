---
entity_id: "reaction.ecocyc.COBINAMIDEKIN-RXN"
entity_type: "reaction"
name: "COBINAMIDEKIN-RXN"
source_database: "EcoCyc"
source_id: "COBINAMIDEKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# COBINAMIDEKIN-RXN

`reaction.ecocyc.COBINAMIDEKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:COBINAMIDEKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of cobalamin biosynthesis. EcoCyc reaction equation: ADENOSYLCOBINAMIDE + ATP -> PROTON + ADENOSYLCOBINAMIDE-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of cobalamin biosynthesis.

## Biological Role

Catalyzed by cobinamide-P guanylyltransferase / cobinamide kinase (complex.ecocyc.COBU-CPLX). Substrates: ATP (molecule.C00002), Adenosyl cobinamide (molecule.C06508). Products: ADP (molecule.C00008), H+ (molecule.C00080), Adenosyl cobinamide phosphate (molecule.C06509).

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
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06509|molecule.C06509]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06508|molecule.C06508]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:COBINAMIDEKIN-RXN`

## Notes

ADENOSYLCOBINAMIDE + ATP -> PROTON + ADENOSYLCOBINAMIDE-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
