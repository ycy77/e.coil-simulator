---
entity_id: "reaction.ecocyc.URITRANS-RXN"
entity_type: "reaction"
name: "URITRANS-RXN"
source_database: "EcoCyc"
source_id: "URITRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# URITRANS-RXN

`reaction.ecocyc.URITRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:URITRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the glutamine synthetase cascade. The E.C. number has been assigned by SwissProt. EcoCyc reaction equation: Gln-B + UTP -> URIDYLYL-PROTEIN-PII + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the glutamine synthetase cascade. The E.C. number has been assigned by SwissProt.

## Biological Role

Substrates: UTP (molecule.C00075). Products: Diphosphate (molecule.C00013).

## Annotation

This reaction is part of the glutamine synthetase cascade. The E.C. number has been assigned by SwissProt.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:URITRANS-RXN`

## Notes

Gln-B + UTP -> URIDYLYL-PROTEIN-PII + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
