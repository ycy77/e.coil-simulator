---
entity_id: "reaction.ecocyc.ACETOLACTSYN-RXN"
entity_type: "reaction"
name: "ACETOLACTSYN-RXN"
source_database: "EcoCyc"
source_id: "ACETOLACTSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETOLACTSYN-RXN

`reaction.ecocyc.ACETOLACTSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETOLACTSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first of a set of shared homologous reactions in the valine, isoleucine and leucine biosynthetic pathways. EcoCyc reaction equation: PROTON + PYRUVATE -> 2-ACETO-LACTATE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT. The first of a set of shared homologous reactions in the valine, isoleucine and leucine biosynthetic pathways.

## Biological Role

Catalyzed by acetohydroxybutanoate synthase / acetolactate synthase (complex.ecocyc.ACETOLACTSYNI-CPLX), acetohydroxybutanoate synthase / acetolactate synthase (complex.ecocyc.ACETOLACTSYNII-CPLX), acetolactate synthase / acetohydroxybutanoate synthase (complex.ecocyc.ACETOLACTSYNIII-CPLX). Substrates: Pyruvate (molecule.C00022), H+ (molecule.C00080). Products: CO2 (molecule.C00011), (S)-2-Acetolactate (molecule.C06010).

## Enriched Pathways

- `ecocyc.VALSYN-PWY` L-valine biosynthesis (EcoCyc)

## Annotation

The first of a set of shared homologous reactions in the valine, isoleucine and leucine biosynthetic pathways.

## Pathways

- `ecocyc.VALSYN-PWY` L-valine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.ACETOLACTSYNI-CPLX|complex.ecocyc.ACETOLACTSYNI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ACETOLACTSYNII-CPLX|complex.ecocyc.ACETOLACTSYNII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ACETOLACTSYNIII-CPLX|complex.ecocyc.ACETOLACTSYNIII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06010|molecule.C06010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1692|molecule.ecocyc.CPD0-1692]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACETOLACTSYN-RXN`

## Notes

PROTON + PYRUVATE -> 2-ACETO-LACTATE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
