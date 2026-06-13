---
entity_id: "reaction.ecocyc.ENOYL-COA-DELTA-ISOM-RXN"
entity_type: "reaction"
name: "ENOYL-COA-DELTA-ISOM-RXN"
source_database: "EcoCyc"
source_id: "ENOYL-COA-DELTA-ISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ENOYL-COA-DELTA-ISOM-RXN

`reaction.ecocyc.ENOYL-COA-DELTA-ISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ENOYL-COA-DELTA-ISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A reaction in β-oxidation of fatty acids, required to feed unsaturated fatty acids into the main pathway. EcoCyc reaction equation: CIS-DELTA3-ENOYL-COA -> TRANS-D2-ENOYL-COA; direction=REVERSIBLE. A reaction in β-oxidation of fatty acids, required to feed unsaturated fatty acids into the main pathway.

## Biological Role

Catalyzed by fadB (protein.P21177), fadJ (protein.P77399). Substrates: a (3Z)-3-enoyl-CoA (molecule.ecocyc.CIS-DELTA3-ENOYL-COA). Products: a (2E)-2-enoyl-CoA (molecule.ecocyc.TRANS-D2-ENOYL-COA).

## Enriched Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Annotation

A reaction in β-oxidation of fatty acids, required to feed unsaturated fatty acids into the main pathway.

## Pathways

- `ecocyc.FAO-PWY` fatty acid β-oxidation I (generic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.TRANS-D2-ENOYL-COA|molecule.ecocyc.TRANS-D2-ENOYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CIS-DELTA3-ENOYL-COA|molecule.ecocyc.CIS-DELTA3-ENOYL-COA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ENOYL-COA-DELTA-ISOM-RXN`

## Notes

CIS-DELTA3-ENOYL-COA -> TRANS-D2-ENOYL-COA; direction=REVERSIBLE
