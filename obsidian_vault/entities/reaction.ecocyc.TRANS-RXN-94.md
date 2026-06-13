---
entity_id: "reaction.ecocyc.TRANS-RXN-94"
entity_type: "reaction"
name: "melibiose:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-94"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# melibiose:proton symport

`reaction.ecocyc.TRANS-RXN-94`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-94`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + MELIBIOSE -> PROTON + MELIBIOSE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + MELIBIOSE -> PROTON + MELIBIOSE; direction=REVERSIBLE.

## Biological Role

Catalyzed by lacY (protein.P02920), melB (protein.P02921). Substrates: H+ (molecule.C00080), Melibiose (molecule.C05402). Products: H+ (molecule.C00080), Melibiose (molecule.C05402).

## Annotation

PROTON + MELIBIOSE -> PROTON + MELIBIOSE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P02920|protein.P02920]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P02921|protein.P02921]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05402|molecule.C05402]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05402|molecule.C05402]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-94`

## Notes

PROTON + MELIBIOSE -> PROTON + MELIBIOSE; direction=REVERSIBLE
