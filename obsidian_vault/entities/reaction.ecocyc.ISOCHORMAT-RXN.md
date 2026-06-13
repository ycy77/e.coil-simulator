---
entity_id: "reaction.ecocyc.ISOCHORMAT-RXN"
entity_type: "reaction"
name: "ISOCHORMAT-RXN"
source_database: "EcoCyc"
source_id: "ISOCHORMAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ISOCHORMAT-RXN

`reaction.ecocyc.ISOCHORMAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ISOCHORMAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the enterobactin biosynthetic pathway. EcoCyc reaction equation: WATER + ISOCHORISMATE -> PYRUVATE + DIHYDRO-DIOH-BENZOATE; direction=LEFT-TO-RIGHT. This is the second reaction in the enterobactin biosynthetic pathway.

## Biological Role

Catalyzed by holo-EntB dimer (complex.ecocyc.ENTB-CPLX). Substrates: H2O (molecule.C00001), Isochorismate (molecule.C00885). Products: Pyruvate (molecule.C00022), (2S,3S)-2,3-Dihydro-2,3-dihydroxybenzoate (molecule.C04171).

## Enriched Pathways

- `ecocyc.PWY-5901` 2,3-dihydroxybenzoate biosynthesis (EcoCyc)

## Annotation

This is the second reaction in the enterobactin biosynthetic pathway.

## Pathways

- `ecocyc.PWY-5901` 2,3-dihydroxybenzoate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ENTB-CPLX|complex.ecocyc.ENTB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04171|molecule.C04171]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00885|molecule.C00885]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ISOCHORMAT-RXN`

## Notes

WATER + ISOCHORISMATE -> PYRUVATE + DIHYDRO-DIOH-BENZOATE; direction=LEFT-TO-RIGHT
