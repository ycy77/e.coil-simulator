---
entity_id: "reaction.ecocyc.GABATRANSAM-RXN"
entity_type: "reaction"
name: "GABATRANSAM-RXN"
source_database: "EcoCyc"
source_id: "GABATRANSAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GABATRANSAM-RXN

`reaction.ecocyc.GABATRANSAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GABATRANSAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the initial reaction in the 4-aminobutyrate (GABA) degradation pathway. EcoCyc reaction equation: 2-KETOGLUTARATE + 4-AMINO-BUTYRATE -> GLT + SUCC-S-ALD; direction=REVERSIBLE. This is the initial reaction in the 4-aminobutyrate (GABA) degradation pathway.

## Biological Role

Catalyzed by 4-aminobutyrate aminotransferase GabT (complex.ecocyc.GABATRANSAM-CPLX), puuE (protein.P50457). Substrates: 2-Oxoglutarate (molecule.C00026), 4-Aminobutanoate (molecule.C00334). Products: L-Glutamate (molecule.C00025), Succinate semialdehyde (molecule.C00232).

## Enriched Pathways

- `ecocyc.PWY-6535` 4-aminobutanoate degradation I (EcoCyc)
- `ecocyc.PWY-6537` 4-aminobutanoate degradation II (EcoCyc)

## Annotation

This is the initial reaction in the 4-aminobutyrate (GABA) degradation pathway.

## Pathways

- `ecocyc.PWY-6535` 4-aminobutanoate degradation I (EcoCyc)
- `ecocyc.PWY-6537` 4-aminobutanoate degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.GABATRANSAM-CPLX|complex.ecocyc.GABATRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P50457|protein.P50457]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00232|molecule.C00232]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00192|molecule.C00192]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CARBOXYMETHOXYLAMINE|molecule.ecocyc.CARBOXYMETHOXYLAMINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1467|molecule.ecocyc.CPD0-1467]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHENYLHYDRAZINE|molecule.ecocyc.PHENYLHYDRAZINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GABATRANSAM-RXN`

## Notes

2-KETOGLUTARATE + 4-AMINO-BUTYRATE -> GLT + SUCC-S-ALD; direction=REVERSIBLE
