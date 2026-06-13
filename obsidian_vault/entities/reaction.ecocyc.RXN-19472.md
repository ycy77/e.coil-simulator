---
entity_id: "reaction.ecocyc.RXN-19472"
entity_type: "reaction"
name: "RXN-19472"
source_database: "EcoCyc"
source_id: "RXN-19472"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19472

`reaction.ecocyc.RXN-19472`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19472`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SER + Non-ribosomal-peptide-synthetases + ATP -> L-seryl-NRPS + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SER + Non-ribosomal-peptide-synthetases + ATP -> L-seryl-NRPS + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Serine (molecule.C00065). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

SER + Non-ribosomal-peptide-synthetases + ATP -> L-seryl-NRPS + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19472`

## Notes

SER + Non-ribosomal-peptide-synthetases + ATP -> L-seryl-NRPS + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
