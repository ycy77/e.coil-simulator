---
entity_id: "reaction.ecocyc.UDPACYLGLCNACDEACETYL-RXN"
entity_type: "reaction"
name: "UDPACYLGLCNACDEACETYL-RXN"
source_database: "EcoCyc"
source_id: "UDPACYLGLCNACDEACETYL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPACYLGLCNACDEACETYL-RXN

`reaction.ecocyc.UDPACYLGLCNACDEACETYL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPACYLGLCNACDEACETYL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction but the first irreversible step of lipid A biosynthesis. EcoCyc reaction equation: UDP-OHMYR-ACETYLGLUCOSAMINE + WATER -> UDP-OHMYR-GLUCOSAMINE + ACET; direction=LEFT-TO-RIGHT. This is the second reaction but the first irreversible step of lipid A biosynthesis.

## Biological Role

Catalyzed by lpxC (protein.P0A725). Substrates: H2O (molecule.C00001), UDP-3-O-(3-hydroxytetradecanoyl)-N-acetylglucosamine (molecule.C04738). Products: Acetate (molecule.C00033), UDP-3-O-(3-hydroxytetradecanoyl)-D-glucosamine (molecule.C06022).

## Enriched Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Annotation

This is the second reaction but the first irreversible step of lipid A biosynthesis.

## Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A725|protein.P0A725]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06022|molecule.C06022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04738|molecule.C04738]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-4841|molecule.ecocyc.CPD-4841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:UDPACYLGLCNACDEACETYL-RXN`

## Notes

UDP-OHMYR-ACETYLGLUCOSAMINE + WATER -> UDP-OHMYR-GLUCOSAMINE + ACET; direction=LEFT-TO-RIGHT
