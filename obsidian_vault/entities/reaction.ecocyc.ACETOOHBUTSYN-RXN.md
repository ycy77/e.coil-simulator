---
entity_id: "reaction.ecocyc.ACETOOHBUTSYN-RXN"
entity_type: "reaction"
name: "2-aceto-2-hydroxy-butyrate synthase"
source_database: "EcoCyc"
source_id: "ACETOOHBUTSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-aceto-2-hydroxy-butyrate synthase

`reaction.ecocyc.ACETOOHBUTSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETOOHBUTSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first of a set of shared homologous reactions in the valine, isoleucine and leucine biosynthetic pathways. EcoCyc reaction equation: PROTON + PYRUVATE + 2-OXOBUTANOATE -> 2-ACETO-2-HYDROXY-BUTYRATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT. The first of a set of shared homologous reactions in the valine, isoleucine and leucine biosynthetic pathways.

## Biological Role

Catalyzed by acetohydroxybutanoate synthase / acetolactate synthase (complex.ecocyc.ACETOLACTSYNI-CPLX), acetohydroxybutanoate synthase / acetolactate synthase (complex.ecocyc.ACETOLACTSYNII-CPLX), acetolactate synthase / acetohydroxybutanoate synthase (complex.ecocyc.ACETOLACTSYNIII-CPLX). Substrates: Pyruvate (molecule.C00022), H+ (molecule.C00080), 2-Oxobutanoate (molecule.C00109). Products: CO2 (molecule.C00011), (S)-2-Aceto-2-hydroxybutanoate (molecule.C06006).

## Enriched Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)

## Annotation

The first of a set of shared homologous reactions in the valine, isoleucine and leucine biosynthetic pathways.

## Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.ACETOLACTSYNI-CPLX|complex.ecocyc.ACETOLACTSYNI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ACETOLACTSYNII-CPLX|complex.ecocyc.ACETOLACTSYNII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ACETOLACTSYNIII-CPLX|complex.ecocyc.ACETOLACTSYNIII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06006|molecule.C06006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACETOOHBUTSYN-RXN`

## Notes

PROTON + PYRUVATE + 2-OXOBUTANOATE -> 2-ACETO-2-HYDROXY-BUTYRATE + CARBON-DIOXIDE; direction=PHYSIOL-LEFT-TO-RIGHT
