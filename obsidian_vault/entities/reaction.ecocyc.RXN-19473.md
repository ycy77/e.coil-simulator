---
entity_id: "reaction.ecocyc.RXN-19473"
entity_type: "reaction"
name: "RXN-19473"
source_database: "EcoCyc"
source_id: "RXN-19473"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19473

`reaction.ecocyc.RXN-19473`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19473`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Non-ribosomal-peptide-synthetases + SERYL-AMP -> L-seryl-NRPS + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Non-ribosomal-peptide-synthetases + SERYL-AMP -> L-seryl-NRPS + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-seryl)adenylate (molecule.ecocyc.SERYL-AMP). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

Non-ribosomal-peptide-synthetases + SERYL-AMP -> L-seryl-NRPS + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.SERYL-AMP|molecule.ecocyc.SERYL-AMP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19473`

## Notes

Non-ribosomal-peptide-synthetases + SERYL-AMP -> L-seryl-NRPS + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
