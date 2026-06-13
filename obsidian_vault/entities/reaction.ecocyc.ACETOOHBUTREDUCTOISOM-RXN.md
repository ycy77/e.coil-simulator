---
entity_id: "reaction.ecocyc.ACETOOHBUTREDUCTOISOM-RXN"
entity_type: "reaction"
name: "ACETOOHBUTREDUCTOISOM-RXN"
source_database: "EcoCyc"
source_id: "ACETOOHBUTREDUCTOISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "&alpha"
  - "-keto-&beta"
  - "-hydroxylacil reductoisomerase"
  - "Acetohydroxy acid isomeroreductase"
  - "Dihydroxyisovalerate dehydrogenase (isomerizing)"
---

# ACETOOHBUTREDUCTOISOM-RXN

`reaction.ecocyc.ACETOOHBUTREDUCTOISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETOOHBUTREDUCTOISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third reaction in the isoleucine biosynthetic pathway, homologous to the second rxn for valine biosynthesis. EcoCyc reaction equation: 1-KETO-2-METHYLVALERATE + NADP -> PROTON + 2-ACETO-2-HYDROXY-BUTYRATE + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT. This is the third reaction in the isoleucine biosynthetic pathway, homologous to the second rxn for valine biosynthesis.

## Biological Role

Catalyzed by ketol-acid reductoisomerase (NADP+) (complex.ecocyc.CPLX0-7643). Substrates: NADP+ (molecule.C00006), (R)-2,3-Dihydroxy-3-methylpentanoate (molecule.C06007). Products: NADPH (molecule.C00005), H+ (molecule.C00080), (S)-2-Aceto-2-hydroxybutanoate (molecule.C06006).

## Enriched Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)

## Annotation

This is the third reaction in the isoleucine biosynthetic pathway, homologous to the second rxn for valine biosynthesis.

## Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7643|complex.ecocyc.CPLX0-7643]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06006|molecule.C06006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06007|molecule.C06007]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACETOOHBUTREDUCTOISOM-RXN`

## Notes

1-KETO-2-METHYLVALERATE + NADP -> PROTON + 2-ACETO-2-HYDROXY-BUTYRATE + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT
