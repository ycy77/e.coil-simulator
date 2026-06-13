---
entity_id: "reaction.ecocyc.5.4.2.10-RXN"
entity_type: "reaction"
name: "5.4.2.10-RXN"
source_database: "EcoCyc"
source_id: "5.4.2.10-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 5.4.2.10-RXN

`reaction.ecocyc.5.4.2.10-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:5.4.2.10-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in hexosamine biosynthesis. EcoCyc reaction equation: D-GLUCOSAMINE-6-P -> GLUCOSAMINE-1P; direction=REVERSIBLE. This is the second reaction in hexosamine biosynthesis.

## Biological Role

Catalyzed by phosphoglucosamine mutase (complex.ecocyc.CPLX0-8583). Substrates: D-Glucosamine 6-phosphate (molecule.C00352). Products: alpha-D-Glucosamine 1-phosphate (molecule.C06156).

## Enriched Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)
- `ecocyc.UDPNAGSYN-PWY` UDP-N-acetyl-D-glucosamine biosynthesis I (EcoCyc)

## Annotation

This is the second reaction in hexosamine biosynthesis.

## Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)
- `ecocyc.UDPNAGSYN-PWY` UDP-N-acetyl-D-glucosamine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8583|complex.ecocyc.CPLX0-8583]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C06156|molecule.C06156]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00352|molecule.C00352]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:5.4.2.10-RXN`

## Notes

D-GLUCOSAMINE-6-P -> GLUCOSAMINE-1P; direction=REVERSIBLE
