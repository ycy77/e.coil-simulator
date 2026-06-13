---
entity_id: "reaction.ecocyc.UDPGLCNACEPIM-RXN"
entity_type: "reaction"
name: "UDPGLCNACEPIM-RXN"
source_database: "EcoCyc"
source_id: "UDPGLCNACEPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPGLCNACEPIM-RXN

`reaction.ecocyc.UDPGLCNACEPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPGLCNACEPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the synthesis of UDP-N-acetyl-mannosaminuronic acid, which is utilized in ECA biosynthesis. EcoCyc reaction equation: UDP-N-ACETYL-D-GLUCOSAMINE -> UDP-MANNAC; direction=REVERSIBLE. This is the first reaction in the synthesis of UDP-N-acetyl-mannosaminuronic acid, which is utilized in ECA biosynthesis.

## Biological Role

Catalyzed by UDP-N-acetylglucosamine 2-epimerase (complex.ecocyc.CPLX0-8008). Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043). Products: UDP-N-acetyl-D-mannosamine (molecule.C01170).

## Enriched Pathways

- `ecocyc.PWY-8462` UDP-N-acetyl-α-D-mannosamine biosynthesis (EcoCyc)
- `ecocyc.PWY0-1611` superpathway of UDP-N-acetyl-α-D-mannosaminouronate biosynthesis (EcoCyc)

## Annotation

This is the first reaction in the synthesis of UDP-N-acetyl-mannosaminuronic acid, which is utilized in ECA biosynthesis.

## Pathways

- `ecocyc.PWY-8462` UDP-N-acetyl-α-D-mannosamine biosynthesis (EcoCyc)
- `ecocyc.PWY0-1611` superpathway of UDP-N-acetyl-α-D-mannosaminouronate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `activates` <-- [[molecule.C00043|molecule.C00043]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8008|complex.ecocyc.CPLX0-8008]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01170|molecule.C01170]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UDPGLCNACEPIM-RXN`

## Notes

UDP-N-ACETYL-D-GLUCOSAMINE -> UDP-MANNAC; direction=REVERSIBLE
