---
entity_id: "reaction.ecocyc.PRAISOM-RXN"
entity_type: "reaction"
name: "PRAISOM-RXN"
source_database: "EcoCyc"
source_id: "PRAISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "N-(5'-PHOSPHORIBOSYL)ANTHRANILATE ISOMERASE"
---

# PRAISOM-RXN

`reaction.ecocyc.PRAISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PRAISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third step in the tryptophan synthesis pathway EcoCyc reaction equation: N-5-PHOSPHORIBOSYL-ANTHRANILATE -> CARBOXYPHENYLAMINO-DEOXYRIBULOSE-P; direction=LEFT-TO-RIGHT. This is the third step in the tryptophan synthesis pathway

## Biological Role

Catalyzed by trpC (protein.P00909). Substrates: N-(5-Phospho-D-ribosyl)anthranilate (molecule.C04302). Products: 1-(2-Carboxyphenylamino)-1-deoxy-D-ribulose 5-phosphate (molecule.C01302).

## Enriched Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Annotation

This is the third step in the tryptophan synthesis pathway

## Pathways

- `ecocyc.TRPSYN-PWY` L-tryptophan biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P00909|protein.P00909]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01302|molecule.C01302]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04302|molecule.C04302]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PRAISOM-RXN`

## Notes

N-5-PHOSPHORIBOSYL-ANTHRANILATE -> CARBOXYPHENYLAMINO-DEOXYRIBULOSE-P; direction=LEFT-TO-RIGHT
