---
entity_id: "reaction.ecocyc.SEDOBISALDOL-RXN"
entity_type: "reaction"
name: "SEDOBISALDOL-RXN"
source_database: "EcoCyc"
source_id: "SEDOBISALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SEDOBISALDOL-RXN

`reaction.ecocyc.SEDOBISALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SEDOBISALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-SEDOHEPTULOSE-1-7-P2 -> DIHYDROXY-ACETONE-PHOSPHATE + ERYTHROSE-4P; direction=REVERSIBLE EcoCyc reaction equation: D-SEDOHEPTULOSE-1-7-P2 -> DIHYDROXY-ACETONE-PHOSPHATE + ERYTHROSE-4P; direction=REVERSIBLE.

## Biological Role

Catalyzed by fructose-bisphosphate aldolase class II (complex.ecocyc.FRUCBISALD-CLASSII). Substrates: Sedoheptulose 1,7-bisphosphate (molecule.C00447). Products: Glycerone phosphate (molecule.C00111), D-Erythrose 4-phosphate (molecule.C00279).

## Enriched Pathways

- `ecocyc.PWY0-1517` sedoheptulose bisphosphate bypass (EcoCyc)

## Annotation

D-SEDOHEPTULOSE-1-7-P2 -> DIHYDROXY-ACETONE-PHOSPHATE + ERYTHROSE-4P; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1517` sedoheptulose bisphosphate bypass (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.FRUCBISALD-CLASSII|complex.ecocyc.FRUCBISALD-CLASSII]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00279|molecule.C00279]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00447|molecule.C00447]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SEDOBISALDOL-RXN`

## Notes

D-SEDOHEPTULOSE-1-7-P2 -> DIHYDROXY-ACETONE-PHOSPHATE + ERYTHROSE-4P; direction=REVERSIBLE
