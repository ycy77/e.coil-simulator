---
entity_id: "reaction.ecocyc.DIHYDROXYMETVALDEHYDRAT-RXN"
entity_type: "reaction"
name: "2,3-Dihydroxy-3-methylvalerate dehydratase"
source_database: "EcoCyc"
source_id: "DIHYDROXYMETVALDEHYDRAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2,3-Dihydroxy-3-methylvalerate dehydratase

`reaction.ecocyc.DIHYDROXYMETVALDEHYDRAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIHYDROXYMETVALDEHYDRAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth step in the isoleucine biosynthetic pathway, homologous to the second rxn for valine biosynthesis. EcoCyc reaction equation: 1-KETO-2-METHYLVALERATE -> 2-KETO-3-METHYL-VALERATE + WATER; direction=LEFT-TO-RIGHT. This is the fourth step in the isoleucine biosynthetic pathway, homologous to the second rxn for valine biosynthesis.

## Biological Role

Catalyzed by dihydroxy-acid dehydratase (complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX). Substrates: (R)-2,3-Dihydroxy-3-methylpentanoate (molecule.C06007). Products: H2O (molecule.C00001), (S)-3-Methyl-2-oxopentanoic acid (molecule.C00671).

## Enriched Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)

## Annotation

This is the fourth step in the isoleucine biosynthetic pathway, homologous to the second rxn for valine biosynthesis.

## Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX|complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00671|molecule.C00671]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06007|molecule.C06007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.NaF|molecule.ecocyc.NaF]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DIHYDROXYMETVALDEHYDRAT-RXN`

## Notes

1-KETO-2-METHYLVALERATE -> 2-KETO-3-METHYL-VALERATE + WATER; direction=LEFT-TO-RIGHT
