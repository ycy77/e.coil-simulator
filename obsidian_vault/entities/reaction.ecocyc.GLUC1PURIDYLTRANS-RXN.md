---
entity_id: "reaction.ecocyc.GLUC1PURIDYLTRANS-RXN"
entity_type: "reaction"
name: "GLUC1PURIDYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "GLUC1PURIDYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUC1PURIDYLTRANS-RXN

`reaction.ecocyc.GLUC1PURIDYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUC1PURIDYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction of intermediary metabolism is also involved in the biosynthesis of polysaccharide moieties in the cell wall. EcoCyc reaction equation: PROTON + GLC-1-P + UTP -> CPD-12575 + PPI; direction=REVERSIBLE. This reaction of intermediary metabolism is also involved in the biosynthesis of polysaccharide moieties in the cell wall.

## Biological Role

Catalyzed by UTP—glucose-1-phosphate uridylyltransferase (complex.ecocyc.CPLX0-8205). Substrates: UTP (molecule.C00075), H+ (molecule.C00080), α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P). Products: Diphosphate (molecule.C00013), UDP-glucose (molecule.C00029).

## Enriched Pathways

- `ecocyc.PWY-7343` UDP-α-D-glucose biosynthesis (EcoCyc)

## Annotation

This reaction of intermediary metabolism is also involved in the biosynthesis of polysaccharide moieties in the cell wall.

## Pathways

- `ecocyc.PWY-7343` UDP-α-D-glucose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8205|complex.ecocyc.CPLX0-8205]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLUC1PURIDYLTRANS-RXN`

## Notes

PROTON + GLC-1-P + UTP -> CPD-12575 + PPI; direction=REVERSIBLE
