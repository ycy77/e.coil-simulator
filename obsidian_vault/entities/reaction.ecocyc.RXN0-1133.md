---
entity_id: "reaction.ecocyc.RXN0-1133"
entity_type: "reaction"
name: "RXN0-1133"
source_database: "EcoCyc"
source_id: "RXN0-1133"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1133

`reaction.ecocyc.RXN0-1133`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1133`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETYL-COA + Pyruvate-dehydrogenase-dihydrolipoate -> CO-A + Pyruvate-dehydrogenase-acetylDHlipoyl; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: ACETYL-COA + Pyruvate-dehydrogenase-dihydrolipoate -> CO-A + Pyruvate-dehydrogenase-acetylDHlipoyl; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by aceF (protein.P06959). Substrates: Acetyl-CoA (molecule.C00024), Enzyme N6-(dihydrolipoyl)lysine (molecule.C15973). Products: CoA (molecule.C00010), [Dihydrolipoyllysine-residue acetyltransferase] S-acetyldihydrolipoyllysine (molecule.C16255).

## Enriched Pathways

- `ecocyc.PYRUVDEHYD-PWY` pyruvate decarboxylation to acetyl CoA I (EcoCyc)

## Annotation

ACETYL-COA + Pyruvate-dehydrogenase-dihydrolipoate -> CO-A + Pyruvate-dehydrogenase-acetylDHlipoyl; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PYRUVDEHYD-PWY` pyruvate decarboxylation to acetyl CoA I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P06959|protein.P06959]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16255|molecule.C16255]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15973|molecule.C15973]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1133`

## Notes

ACETYL-COA + Pyruvate-dehydrogenase-dihydrolipoate -> CO-A + Pyruvate-dehydrogenase-acetylDHlipoyl; direction=PHYSIOL-RIGHT-TO-LEFT
