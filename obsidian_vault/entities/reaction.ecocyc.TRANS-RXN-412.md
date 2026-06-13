---
entity_id: "reaction.ecocyc.TRANS-RXN-412"
entity_type: "reaction"
name: "TRANS-RXN-412"
source_database: "EcoCyc"
source_id: "TRANS-RXN-412"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-412

`reaction.ecocyc.TRANS-RXN-412`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-412`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

7-CYANO-7-DEAZAGUANINE -> 7-CYANO-7-DEAZAGUANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 7-CYANO-7-DEAZAGUANINE -> 7-CYANO-7-DEAZAGUANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yhhQ (protein.P37619). Substrates: 7-Cyano-7-carbaguanine (molecule.C15996). Products: 7-Cyano-7-carbaguanine (molecule.C15996).

## Annotation

7-CYANO-7-DEAZAGUANINE -> 7-CYANO-7-DEAZAGUANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37619|protein.P37619]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C15996|molecule.C15996]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C15996|molecule.C15996]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-412`

## Notes

7-CYANO-7-DEAZAGUANINE -> 7-CYANO-7-DEAZAGUANINE; direction=PHYSIOL-LEFT-TO-RIGHT
