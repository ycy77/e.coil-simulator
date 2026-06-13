---
entity_id: "reaction.ecocyc.RXN0-7445"
entity_type: "reaction"
name: "RXN0-7445"
source_database: "EcoCyc"
source_id: "RXN0-7445"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7445

`reaction.ecocyc.RXN0-7445`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7445`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The chromosomal loci DARS1 and DARS2 and membrane-associated acidic phospholipids have been described to convert DnaA-ADP to the apo-form. EcoCyc reaction equation: MONOMER0-4565 + WATER -> PD03831 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. The chromosomal loci DARS1 and DARS2 and membrane-associated acidic phospholipids have been described to convert DnaA-ADP to the apo-form.

## Biological Role

Substrates: H2O (molecule.C00001). Products: ADP (molecule.C00008).

## Annotation

The chromosomal loci DARS1 and DARS2 and membrane-associated acidic phospholipids have been described to convert DnaA-ADP to the apo-form.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7445`

## Notes

MONOMER0-4565 + WATER -> PD03831 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
