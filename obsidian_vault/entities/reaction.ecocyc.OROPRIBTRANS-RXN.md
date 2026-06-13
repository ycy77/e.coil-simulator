---
entity_id: "reaction.ecocyc.OROPRIBTRANS-RXN"
entity_type: "reaction"
name: "OROPRIBTRANS-RXN"
source_database: "EcoCyc"
source_id: "OROPRIBTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# OROPRIBTRANS-RXN

`reaction.ecocyc.OROPRIBTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OROPRIBTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth step in pyrimidine biosynthesis. EcoCyc reaction equation: OROTIDINE-5-PHOSPHATE + PPI -> PRPP + OROTATE; direction=REVERSIBLE. This is the fifth step in pyrimidine biosynthesis.

## Biological Role

Catalyzed by orotate phosphoribosyltransferase (complex.ecocyc.OROPRIBTRANS-CPLX). Substrates: Diphosphate (molecule.C00013), Orotidine 5'-phosphate (molecule.C01103). Products: 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), Orotate (molecule.C00295).

## Enriched Pathways

- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Annotation

This is the fifth step in pyrimidine biosynthesis.

## Pathways

- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.OROPRIBTRANS-CPLX|complex.ecocyc.OROPRIBTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00295|molecule.C00295]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01103|molecule.C01103]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:OROPRIBTRANS-RXN`

## Notes

OROTIDINE-5-PHOSPHATE + PPI -> PRPP + OROTATE; direction=REVERSIBLE
