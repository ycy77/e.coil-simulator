---
entity_id: "reaction.ecocyc.2.3.1.118-RXN"
entity_type: "reaction"
name: "2.3.1.118-RXN"
source_database: "EcoCyc"
source_id: "2.3.1.118-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "ARYLAMINE N-ACETYLTRANSFERASE"
  - "ARYLHYDROXAMATE N,O-ACETYLTRANSFERASE"
---

# 2.3.1.118-RXN

`reaction.ecocyc.2.3.1.118-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.3.1.118-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-Hydroxy-Arylamines + ACETYL-COA -> N-Acetoxy-Arylamines + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: N-Hydroxy-Arylamines + ACETYL-COA -> N-Acetoxy-Arylamines + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by arylamine N-acetyltransferase (complex.ecocyc.CPLX0-236). Substrates: Acetyl-CoA (molecule.C00024), an N-hydroxy-arylamine (molecule.ecocyc.N-Hydroxy-Arylamines). Products: CoA (molecule.C00010), an N-acetoxyarylamine (molecule.ecocyc.N-Acetoxy-Arylamines).

## Annotation

N-Hydroxy-Arylamines + ACETYL-COA -> N-Acetoxy-Arylamines + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-236|complex.ecocyc.CPLX0-236]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-Acetoxy-Arylamines|molecule.ecocyc.N-Acetoxy-Arylamines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N-Hydroxy-Arylamines|molecule.ecocyc.N-Hydroxy-Arylamines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.3.1.118-RXN`

## Notes

N-Hydroxy-Arylamines + ACETYL-COA -> N-Acetoxy-Arylamines + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
