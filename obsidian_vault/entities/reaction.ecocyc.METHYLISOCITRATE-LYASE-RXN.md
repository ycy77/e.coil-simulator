---
entity_id: "reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN"
entity_type: "reaction"
name: "METHYLISOCITRATE-LYASE-RXN"
source_database: "EcoCyc"
source_id: "METHYLISOCITRATE-LYASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# METHYLISOCITRATE-LYASE-RXN

`reaction.ecocyc.METHYLISOCITRATE-LYASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:METHYLISOCITRATE-LYASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-618 -> SUC + PYRUVATE; direction=REVERSIBLE EcoCyc reaction equation: CPD-618 -> SUC + PYRUVATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by 2-methylisocitrate lyase (complex.ecocyc.CPLX0-1021). Substrates: (2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate (molecule.C04593). Products: Pyruvate (molecule.C00022), Succinate (molecule.C00042).

## Enriched Pathways

- `ecocyc.PWY0-42` 2-methylcitrate cycle I (EcoCyc)

## Annotation

CPD-618 -> SUC + PYRUVATE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-42` 2-methylcitrate cycle I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1021|complex.ecocyc.CPLX0-1021]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04593|molecule.C04593]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.3-BROMOPYRUVATE|molecule.ecocyc.3-BROMOPYRUVATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:METHYLISOCITRATE-LYASE-RXN`

## Notes

CPD-618 -> SUC + PYRUVATE; direction=REVERSIBLE
