---
entity_id: "reaction.ecocyc.2.3.1.157-RXN"
entity_type: "reaction"
name: "2.3.1.157-RXN"
source_database: "EcoCyc"
source_id: "2.3.1.157-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.3.1.157-RXN

`reaction.ecocyc.2.3.1.157-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.3.1.157-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third reaction in hexosamine biosynthesis. EcoCyc reaction equation: GLUCOSAMINE-1P + ACETYL-COA -> PROTON + N-ACETYL-D-GLUCOSAMINE-1-P + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT. This is the third reaction in hexosamine biosynthesis.

## Biological Role

Catalyzed by fused N-acetylglucosamine-1-phosphate uridyltransferase and glucosamine-1-phosphate acetyltransferase (complex.ecocyc.NAG1P-URIDYLTRANS-CPLX). Substrates: Acetyl-CoA (molecule.C00024), alpha-D-Glucosamine 1-phosphate (molecule.C06156). Products: CoA (molecule.C00010), H+ (molecule.C00080), N-acetyl-α-D-glucosamine 1-phosphate (molecule.ecocyc.N-ACETYL-D-GLUCOSAMINE-1-P).

## Enriched Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)
- `ecocyc.UDPNAGSYN-PWY` UDP-N-acetyl-D-glucosamine biosynthesis I (EcoCyc)

## Annotation

This is the third reaction in hexosamine biosynthesis.

## Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)
- `ecocyc.UDPNAGSYN-PWY` UDP-N-acetyl-D-glucosamine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `catalyzes` <-- [[complex.ecocyc.NAG1P-URIDYLTRANS-CPLX|complex.ecocyc.NAG1P-URIDYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-ACETYL-D-GLUCOSAMINE-1-P|molecule.ecocyc.N-ACETYL-D-GLUCOSAMINE-1-P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06156|molecule.C06156]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01050|molecule.C01050]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C02713|molecule.C02713]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C21027|molecule.C21027]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1642|molecule.ecocyc.CPD0-1642]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ACETYL-D-GLUCOSAMINE-1-P|molecule.ecocyc.N-ACETYL-D-GLUCOSAMINE-1-P]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2.3.1.157-RXN`

## Notes

GLUCOSAMINE-1P + ACETYL-COA -> PROTON + N-ACETYL-D-GLUCOSAMINE-1-P + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
