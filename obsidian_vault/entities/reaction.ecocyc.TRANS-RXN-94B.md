---
entity_id: "reaction.ecocyc.TRANS-RXN-94B"
entity_type: "reaction"
name: "melibiose:Li+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-94B"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# melibiose:Li+ symport

`reaction.ecocyc.TRANS-RXN-94B`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-94B`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

LI+ + MELIBIOSE -> LI+ + MELIBIOSE; direction=REVERSIBLE EcoCyc reaction equation: LI+ + MELIBIOSE -> LI+ + MELIBIOSE; direction=REVERSIBLE.

## Biological Role

Catalyzed by melB (protein.P02921). Substrates: Melibiose (molecule.C05402), Li+ (molecule.ecocyc.LI_). Products: Melibiose (molecule.C05402), Li+ (molecule.ecocyc.LI_).

## Annotation

LI+ + MELIBIOSE -> LI+ + MELIBIOSE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P02921|protein.P02921]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C05402|molecule.C05402]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05402|molecule.C05402]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-94B`

## Notes

LI+ + MELIBIOSE -> LI+ + MELIBIOSE; direction=REVERSIBLE
