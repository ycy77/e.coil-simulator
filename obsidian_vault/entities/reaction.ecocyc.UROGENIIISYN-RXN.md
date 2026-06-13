---
entity_id: "reaction.ecocyc.UROGENIIISYN-RXN"
entity_type: "reaction"
name: "UROGENIIISYN-RXN"
source_database: "EcoCyc"
source_id: "UROGENIIISYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "UROPORPHYRINOGEN-III COSYNTHETASE"
  - "UROPORPHYRINOGEN-III COSYNTHASE"
  - "HYDROXYMETHYLBILANE HYDROLYASE (CYCLIZING)"
---

# UROGENIIISYN-RXN

`reaction.ecocyc.UROGENIIISYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UROGENIIISYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in porphyrin biosynthesis. In the presence of EC 4.3.1.8, forms uroporphyrinogen-III from porphobilinogen. EcoCyc reaction equation: HYDROXYMETHYLBILANE -> WATER + UROPORPHYRINOGEN-III; direction=LEFT-TO-RIGHT. A reaction in porphyrin biosynthesis. In the presence of EC 4.3.1.8, forms uroporphyrinogen-III from porphobilinogen.

## Biological Role

Catalyzed by hemD (protein.P09126). Substrates: Hydroxymethylbilane (molecule.C01024). Products: H2O (molecule.C00001), Uroporphyrinogen III (molecule.C01051).

## Enriched Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)

## Annotation

A reaction in porphyrin biosynthesis. In the presence of EC 4.3.1.8, forms uroporphyrinogen-III from porphobilinogen.

## Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P09126|protein.P09126]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01051|molecule.C01051]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01024|molecule.C01024]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UROGENIIISYN-RXN`

## Notes

HYDROXYMETHYLBILANE -> WATER + UROPORPHYRINOGEN-III; direction=LEFT-TO-RIGHT
