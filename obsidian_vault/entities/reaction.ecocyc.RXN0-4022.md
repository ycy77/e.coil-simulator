---
entity_id: "reaction.ecocyc.RXN0-4022"
entity_type: "reaction"
name: "RXN0-4022"
source_database: "EcoCyc"
source_id: "RXN0-4022"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4022

`reaction.ecocyc.RXN0-4022`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4022`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

7-AMINOMETHYL-7-DEAZAGUANINE + NADP -> 7-CYANO-7-DEAZAGUANINE + NADPH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: 7-AMINOMETHYL-7-DEAZAGUANINE + NADP -> 7-CYANO-7-DEAZAGUANINE + NADPH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 7-cyano-7-deazaguanine reductase (complex.ecocyc.CPLX0-3501). Substrates: NADP+ (molecule.C00006), 7-Aminomethyl-7-carbaguanine (molecule.C16675). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 7-Cyano-7-carbaguanine (molecule.C15996).

## Enriched Pathways

- `ecocyc.PWY-6700` queuosine biosynthesis I (de novo) (EcoCyc)

## Annotation

7-AMINOMETHYL-7-DEAZAGUANINE + NADP -> 7-CYANO-7-DEAZAGUANINE + NADPH + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-6700` queuosine biosynthesis I (de novo) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3501|complex.ecocyc.CPLX0-3501]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C15996|molecule.C15996]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16675|molecule.C16675]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4022`

## Notes

7-AMINOMETHYL-7-DEAZAGUANINE + NADP -> 7-CYANO-7-DEAZAGUANINE + NADPH + PROTON; direction=RIGHT-TO-LEFT
