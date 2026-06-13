---
entity_id: "reaction.ecocyc.TREHALA-RXN"
entity_type: "reaction"
name: "TREHALA-RXN"
source_database: "EcoCyc"
source_id: "TREHALA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TREHALA-RXN

`reaction.ecocyc.TREHALA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TREHALA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC

## Enriched Summary

This reaction hydrolyzes trehalose into two glucose moieties. EcoCyc reaction equation: TREHALOSE + WATER -> GLC + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction hydrolyzes trehalose into two glucose moieties.

## Biological Role

Catalyzed by treA (protein.P13482), treF (protein.P62601). Substrates: H2O (molecule.C00001), alpha,alpha-Trehalose (molecule.C01083). Products: beta-D-Glucose (molecule.C00221), alpha-D-Glucose (molecule.C00267).

## Enriched Pathways

- `ecocyc.PWY0-1182` trehalose degradation II (cytosolic) (EcoCyc)
- `ecocyc.PWY0-1466` trehalose degradation VI (periplasmic) (EcoCyc)

## Annotation

This reaction hydrolyzes trehalose into two glucose moieties.

## Pathways

- `ecocyc.PWY0-1182` trehalose degradation II (cytosolic) (EcoCyc)
- `ecocyc.PWY0-1466` trehalose degradation VI (periplasmic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P13482|protein.P13482]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P62601|protein.P62601]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00221|molecule.C00221]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00267|molecule.C00267]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01083|molecule.C01083]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-2306|molecule.ecocyc.CPD0-2306]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TREHALA-RXN`

## Notes

TREHALOSE + WATER -> GLC + ALPHA-GLUCOSE; direction=PHYSIOL-LEFT-TO-RIGHT
