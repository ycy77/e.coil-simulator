---
entity_id: "reaction.ecocyc.RXN0-1132"
entity_type: "reaction"
name: "RXN0-1132"
source_database: "EcoCyc"
source_id: "RXN0-1132"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1132

`reaction.ecocyc.RXN0-1132`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1132`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pyruvate-dehydrogenase-dihydrolipoate + NAD -> Pyruvate-dehydrogenase-lipoate + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Pyruvate-dehydrogenase-dihydrolipoate + NAD -> Pyruvate-dehydrogenase-lipoate + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lipoamide dehydrogenase (complex.ecocyc.E3-CPLX). Substrates: NAD+ (molecule.C00003), Enzyme N6-(dihydrolipoyl)lysine (molecule.C15973). Products: NADH (molecule.C00004), H+ (molecule.C00080), Enzyme N6-(lipoyl)lysine (molecule.C15972).

## Enriched Pathways

- `ecocyc.PYRUVDEHYD-PWY` pyruvate decarboxylation to acetyl CoA I (EcoCyc)

## Annotation

Pyruvate-dehydrogenase-dihydrolipoate + NAD -> Pyruvate-dehydrogenase-lipoate + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PYRUVDEHYD-PWY` pyruvate decarboxylation to acetyl CoA I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15972|molecule.C15972]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15973|molecule.C15973]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-1132`

## Notes

Pyruvate-dehydrogenase-dihydrolipoate + NAD -> Pyruvate-dehydrogenase-lipoate + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
