---
entity_id: "reaction.ecocyc.TRANS-RXN0-201"
entity_type: "reaction"
name: "citrate:succinate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-201"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# citrate:succinate antiport

`reaction.ecocyc.TRANS-RXN0-201`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-201`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

SUC + CIT -> CIT + SUC; direction=REVERSIBLE EcoCyc reaction equation: SUC + CIT -> CIT + SUC; direction=REVERSIBLE.

## Biological Role

Catalyzed by citT (protein.P0AE74). Substrates: Succinate (molecule.C00042), Citrate (molecule.C00158). Products: Succinate (molecule.C00042), Citrate (molecule.C00158).

## Annotation

SUC + CIT -> CIT + SUC; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AE74|protein.P0AE74]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-201`

## Notes

SUC + CIT -> CIT + SUC; direction=REVERSIBLE
