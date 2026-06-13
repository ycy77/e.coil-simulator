---
entity_id: "reaction.ecocyc.RXN0-1461"
entity_type: "reaction"
name: "RXN0-1461"
source_database: "EcoCyc"
source_id: "RXN0-1461"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1461

`reaction.ecocyc.RXN0-1461`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1461`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in porphyrin biosynthesis. The reaction stoichiometry has been experimentally determined using aerobic coproporphyrinogen oxidase from the yeast Saccharomyces cerevisiae . The Enzyme Commission presents the following reaction for EC 1.3.3.3: coproporphyrinogen-III + O2 = protoporphyrinogen-IX + 2 CO2 The reaction listed by the Enzyme Commission differs from the experimentally verified equation. EcoCyc reaction equation: COPROPORPHYRINOGEN_III + OXYGEN-MOLECULE + PROTON -> PROTOPORPHYRINOGEN + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT. A reaction in porphyrin biosynthesis. The reaction stoichiometry has been experimentally determined using aerobic coproporphyrinogen oxidase from the yeast Saccharomyces cerevisiae . The Enzyme Commission presents the following reaction for EC 1.3.3.3: coproporphyrinogen-III + O2 = protoporphyrinogen-IX + 2 CO2 The reaction listed by the Enzyme Commission differs from the experimentally verified equation.

## Biological Role

Catalyzed by coproporphyrinogen III oxidase (complex.ecocyc.CPLX0-7808). Substrates: Oxygen (molecule.C00007), H+ (molecule.C00080), Coproporphyrinogen III (molecule.C03263). Products: H2O (molecule.C00001), CO2 (molecule.C00011), Protoporphyrinogen IX (molecule.C01079).

## Enriched Pathways

- `ecocyc.HEME-BIOSYNTHESIS-II-1` heme b biosynthesis V (aerobic) (EcoCyc)

## Annotation

A reaction in porphyrin biosynthesis. The reaction stoichiometry has been experimentally determined using aerobic coproporphyrinogen oxidase from the yeast Saccharomyces cerevisiae . The Enzyme Commission presents the following reaction for EC 1.3.3.3: coproporphyrinogen-III + O2 = protoporphyrinogen-IX + 2 CO2 The reaction listed by the Enzyme Commission differs from the experimentally verified equation.

## Pathways

- `ecocyc.HEME-BIOSYNTHESIS-II-1` heme b biosynthesis V (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7808|complex.ecocyc.CPLX0-7808]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01079|molecule.C01079]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03263|molecule.C03263]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C02191|molecule.C02191]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-1461`

## Notes

COPROPORPHYRINOGEN_III + OXYGEN-MOLECULE + PROTON -> PROTOPORPHYRINOGEN + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
