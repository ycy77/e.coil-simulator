---
entity_id: "reaction.ecocyc.UGD-RXN"
entity_type: "reaction"
name: "UGD-RXN"
source_database: "EcoCyc"
source_id: "UGD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UGD-RXN

`reaction.ecocyc.UGD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UGD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction UDP-D-glucuronate is synthesized. It is one of four nucleotide sugars necessary for production of the colanic acid repeat unit. EcoCyc reaction equation: CPD-12575 + WATER + NAD -> PROTON + NADH + UDP-GLUCURONATE; direction=LEFT-TO-RIGHT. In this reaction UDP-D-glucuronate is synthesized. It is one of four nucleotide sugars necessary for production of the colanic acid repeat unit.

## Biological Role

Catalyzed by UDP-glucose 6-dehydrogenase (complex.ecocyc.CPLX0-8098). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), UDP-glucose (molecule.C00029). Products: NADH (molecule.C00004), H+ (molecule.C00080), UDP-glucuronate (molecule.C00167).

## Enriched Pathways

- `ecocyc.PWY-7346` UDP-α-D-glucuronate biosynthesis (from UDP-glucose) (EcoCyc)

## Annotation

In this reaction UDP-D-glucuronate is synthesized. It is one of four nucleotide sugars necessary for production of the colanic acid repeat unit.

## Pathways

- `ecocyc.PWY-7346` UDP-α-D-glucuronate biosynthesis (from UDP-glucose) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8098|complex.ecocyc.CPLX0-8098]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00167|molecule.C00167]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UGD-RXN`

## Notes

CPD-12575 + WATER + NAD -> PROTON + NADH + UDP-GLUCURONATE; direction=LEFT-TO-RIGHT
