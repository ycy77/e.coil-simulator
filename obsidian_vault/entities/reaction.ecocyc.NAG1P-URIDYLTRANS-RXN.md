---
entity_id: "reaction.ecocyc.NAG1P-URIDYLTRANS-RXN"
entity_type: "reaction"
name: "NAG1P-URIDYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "NAG1P-URIDYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NAG1P-URIDYLTRANS-RXN

`reaction.ecocyc.NAG1P-URIDYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NAG1P-URIDYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction generates UDP-N-acetylglucosamine, precursor of peptidoglycan, lipopolysaccharide and enterobacterial common antigen. EcoCyc reaction equation: PROTON + N-ACETYL-D-GLUCOSAMINE-1-P + UTP -> UDP-N-ACETYL-D-GLUCOSAMINE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction generates UDP-N-acetylglucosamine, precursor of peptidoglycan, lipopolysaccharide and enterobacterial common antigen.

## Biological Role

Catalyzed by fused N-acetylglucosamine-1-phosphate uridyltransferase and glucosamine-1-phosphate acetyltransferase (complex.ecocyc.NAG1P-URIDYLTRANS-CPLX). Substrates: UTP (molecule.C00075), H+ (molecule.C00080), N-acetyl-α-D-glucosamine 1-phosphate (molecule.ecocyc.N-ACETYL-D-GLUCOSAMINE-1-P). Products: Diphosphate (molecule.C00013), UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043).

## Enriched Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)
- `ecocyc.UDPNAGSYN-PWY` UDP-N-acetyl-D-glucosamine biosynthesis I (EcoCyc)

## Annotation

This reaction generates UDP-N-acetylglucosamine, precursor of peptidoglycan, lipopolysaccharide and enterobacterial common antigen.

## Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)
- `ecocyc.UDPNAGSYN-PWY` UDP-N-acetyl-D-glucosamine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.NAG1P-URIDYLTRANS-CPLX|complex.ecocyc.NAG1P-URIDYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00043|molecule.C00043]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N-ACETYL-D-GLUCOSAMINE-1-P|molecule.ecocyc.N-ACETYL-D-GLUCOSAMINE-1-P]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NAG1P-URIDYLTRANS-RXN`

## Notes

PROTON + N-ACETYL-D-GLUCOSAMINE-1-P + UTP -> UDP-N-ACETYL-D-GLUCOSAMINE + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
