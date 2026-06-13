---
entity_id: "reaction.ecocyc.RXN0-1134"
entity_type: "reaction"
name: "RXN0-1134"
source_database: "EcoCyc"
source_id: "RXN0-1134"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1134

`reaction.ecocyc.RXN0-1134`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1134`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PYRUVATE + Pyruvate-dehydrogenase-lipoate + PROTON -> Pyruvate-dehydrogenase-acetylDHlipoyl + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PYRUVATE + Pyruvate-dehydrogenase-lipoate + PROTON -> Pyruvate-dehydrogenase-acetylDHlipoyl + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyruvate dehydrogenase (complex.ecocyc.E1P-CPLX). Substrates: Pyruvate (molecule.C00022), H+ (molecule.C00080), Enzyme N6-(lipoyl)lysine (molecule.C15972). Products: CO2 (molecule.C00011), [Dihydrolipoyllysine-residue acetyltransferase] S-acetyldihydrolipoyllysine (molecule.C16255).

## Enriched Pathways

- `ecocyc.PYRUVDEHYD-PWY` pyruvate decarboxylation to acetyl CoA I (EcoCyc)

## Annotation

PYRUVATE + Pyruvate-dehydrogenase-lipoate + PROTON -> Pyruvate-dehydrogenase-acetylDHlipoyl + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PYRUVDEHYD-PWY` pyruvate decarboxylation to acetyl CoA I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.E1P-CPLX|complex.ecocyc.E1P-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16255|molecule.C16255]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15972|molecule.C15972]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1134`

## Notes

PYRUVATE + Pyruvate-dehydrogenase-lipoate + PROTON -> Pyruvate-dehydrogenase-acetylDHlipoyl + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
