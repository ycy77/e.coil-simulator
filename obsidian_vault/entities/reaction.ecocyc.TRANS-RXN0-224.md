---
entity_id: "reaction.ecocyc.TRANS-RXN0-224"
entity_type: "reaction"
name: "TRANS-RXN0-224"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-224"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-224

`reaction.ecocyc.TRANS-RXN0-224`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-224`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

WATER + Macrolide-Antibiotics + ATP -> Macrolide-Antibiotics + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + Macrolide-Antibiotics + ATP -> Macrolide-Antibiotics + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ABC-type tripartite efflux pump (complex.ecocyc.TRANS-200-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), a macrolide antibiotic (molecule.ecocyc.Macrolide-Antibiotics). Products: ADP (molecule.C00008), H+ (molecule.C00080), a macrolide antibiotic (molecule.ecocyc.Macrolide-Antibiotics), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + Macrolide-Antibiotics + ATP -> Macrolide-Antibiotics + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.TRANS-200-CPLX|complex.ecocyc.TRANS-200-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Macrolide-Antibiotics|molecule.ecocyc.Macrolide-Antibiotics]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Macrolide-Antibiotics|molecule.ecocyc.Macrolide-Antibiotics]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-224`

## Notes

WATER + Macrolide-Antibiotics + ATP -> Macrolide-Antibiotics + Pi + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
