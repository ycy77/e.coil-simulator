---
entity_id: "reaction.ecocyc.UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN"
entity_type: "reaction"
name: "UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN

`reaction.ecocyc.UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third committed step in lipid A biosynthesis. EcoCyc reaction equation: R-3-hydroxymyristoyl-ACPs + UDP-OHMYR-GLUCOSAMINE -> OH-MYRISTOYL + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This is the third committed step in lipid A biosynthesis.

## Biological Role

Catalyzed by UDP-3-O-(3-hydroxymyristoyl)glucosamine N-acyltransferase (complex.ecocyc.CPLX0-8016). Substrates: UDP-3-O-(3-hydroxytetradecanoyl)-D-glucosamine (molecule.C06022). Products: H+ (molecule.C00080), UDP-2,3-bis(3-hydroxytetradecanoyl)glucosamine (molecule.C04652).

## Enriched Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Annotation

This is the third committed step in lipid A biosynthesis.

## Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8016|complex.ecocyc.CPLX0-8016]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04652|molecule.C04652]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06022|molecule.C06022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN`

## Notes

R-3-hydroxymyristoyl-ACPs + UDP-OHMYR-GLUCOSAMINE -> OH-MYRISTOYL + ACP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
