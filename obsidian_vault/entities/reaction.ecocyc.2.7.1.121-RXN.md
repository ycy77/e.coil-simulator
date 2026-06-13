---
entity_id: "reaction.ecocyc.2.7.1.121-RXN"
entity_type: "reaction"
name: "2.7.1.121-RXN"
source_database: "EcoCyc"
source_id: "2.7.1.121-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.7.1.121-RXN

`reaction.ecocyc.2.7.1.121-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.1.121-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDROXYACETONE + PHOSPHO-ENOL-PYRUVATE -> DIHYDROXY-ACETONE-PHOSPHATE + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DIHYDROXYACETONE + PHOSPHO-ENOL-PYRUVATE -> DIHYDROXY-ACETONE-PHOSPHATE + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dihydroxyacetone kinase (complex.ecocyc.CPLX0-2081). Substrates: Phosphoenolpyruvate (molecule.C00074), Glycerone (molecule.C00184). Products: Pyruvate (molecule.C00022), Glycerone phosphate (molecule.C00111).

## Enriched Pathways

- `ecocyc.GLYCEROLMETAB-PWY` glycerol degradation V (EcoCyc)

## Annotation

DIHYDROXYACETONE + PHOSPHO-ENOL-PYRUVATE -> DIHYDROXY-ACETONE-PHOSPHATE + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.GLYCEROLMETAB-PWY` glycerol degradation V (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2081|complex.ecocyc.CPLX0-2081]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00184|molecule.C00184]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.7.1.121-RXN`

## Notes

DIHYDROXYACETONE + PHOSPHO-ENOL-PYRUVATE -> DIHYDROXY-ACETONE-PHOSPHATE + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT
