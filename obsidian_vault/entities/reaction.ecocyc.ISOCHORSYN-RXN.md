---
entity_id: "reaction.ecocyc.ISOCHORSYN-RXN"
entity_type: "reaction"
name: "ISOCHORSYN-RXN"
source_database: "EcoCyc"
source_id: "ISOCHORSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ISOCHORSYN-RXN

`reaction.ecocyc.ISOCHORSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ISOCHORSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction chorismate is converted to isochorismate. This is the first committed step in both enterobactin and menaquinone synthesis. EcoCyc reaction equation: CHORISMATE -> ISOCHORISMATE; direction=REVERSIBLE. In this reaction chorismate is converted to isochorismate. This is the first committed step in both enterobactin and menaquinone synthesis.

## Biological Role

Catalyzed by isochorismate synthase MenF (complex.ecocyc.MENF-CPLX), entC (protein.P0AEJ2). Substrates: Chorismate (molecule.C00251). Products: Isochorismate (molecule.C00885).

## Enriched Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)
- `ecocyc.PWY-5901` 2,3-dihydroxybenzoate biosynthesis (EcoCyc)

## Annotation

In this reaction chorismate is converted to isochorismate. This is the first committed step in both enterobactin and menaquinone synthesis.

## Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)
- `ecocyc.PWY-5901` 2,3-dihydroxybenzoate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.MENF-CPLX|complex.ecocyc.MENF-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AEJ2|protein.P0AEJ2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00885|molecule.C00885]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00251|molecule.C00251]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ISOCHORSYN-RXN`

## Notes

CHORISMATE -> ISOCHORISMATE; direction=REVERSIBLE
