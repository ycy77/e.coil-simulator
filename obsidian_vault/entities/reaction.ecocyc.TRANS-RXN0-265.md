---
entity_id: "reaction.ecocyc.TRANS-RXN0-265"
entity_type: "reaction"
name: "amino acid export"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-265"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# amino acid export

`reaction.ecocyc.TRANS-RXN0-265`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-265`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Amino-Acids -> Amino-Acids; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Amino-Acids -> Amino-Acids; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yddG (protein.P46136). Substrates: an amino acid (molecule.ecocyc.Amino-Acids). Products: an amino acid (molecule.ecocyc.Amino-Acids).

## Annotation

Amino-Acids -> Amino-Acids; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P46136|protein.P46136]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids|molecule.ecocyc.Amino-Acids]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Amino-Acids|molecule.ecocyc.Amino-Acids]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-265`

## Notes

Amino-Acids -> Amino-Acids; direction=PHYSIOL-LEFT-TO-RIGHT
