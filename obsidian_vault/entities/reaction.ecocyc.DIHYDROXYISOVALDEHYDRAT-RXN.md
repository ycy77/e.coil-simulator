---
entity_id: "reaction.ecocyc.DIHYDROXYISOVALDEHYDRAT-RXN"
entity_type: "reaction"
name: "DIHYDROXYISOVALDEHYDRAT-RXN"
source_database: "EcoCyc"
source_id: "DIHYDROXYISOVALDEHYDRAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIHYDROXYISOVALDEHYDRAT-RXN

`reaction.ecocyc.DIHYDROXYISOVALDEHYDRAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIHYDROXYISOVALDEHYDRAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The third shared step in valine and leucine biosynthetic pathways. EcoCyc reaction equation: CPD-13357 -> 2-KETO-ISOVALERATE + WATER; direction=LEFT-TO-RIGHT. The third shared step in valine and leucine biosynthetic pathways.

## Biological Role

Catalyzed by dihydroxy-acid dehydratase (complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX). Substrates: (R)-2,3-Dihydroxy-3-methylbutanoate (molecule.C04272). Products: H2O (molecule.C00001), 3-Methyl-2-oxobutanoic acid (molecule.C00141).

## Enriched Pathways

- `ecocyc.VALSYN-PWY` L-valine biosynthesis (EcoCyc)

## Annotation

The third shared step in valine and leucine biosynthetic pathways.

## Pathways

- `ecocyc.VALSYN-PWY` L-valine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX|complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00141|molecule.C00141]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04272|molecule.C04272]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.NaF|molecule.ecocyc.NaF]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DIHYDROXYISOVALDEHYDRAT-RXN`

## Notes

CPD-13357 -> 2-KETO-ISOVALERATE + WATER; direction=LEFT-TO-RIGHT
