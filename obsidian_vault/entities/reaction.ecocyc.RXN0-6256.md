---
entity_id: "reaction.ecocyc.RXN0-6256"
entity_type: "reaction"
name: "RXN0-6256"
source_database: "EcoCyc"
source_id: "RXN0-6256"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6256

`reaction.ecocyc.RXN0-6256`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6256`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1885 + GLUTATHIONE -> 2-MERCAPTOETHANOL + OXIDIZED-GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1885 + GLUTATHIONE -> 2-MERCAPTOETHANOL + OXIDIZED-GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by disulfide bond oxidoreductase YfcG (complex.ecocyc.CPLX0-7806), disulfide reductase / organic hydroperoxide reductase (complex.ecocyc.CPLX0-7917). Substrates: Glutathione (molecule.C00051), 2-hydroxyethyldisulfide (molecule.ecocyc.CPD0-1885). Products: Glutathione disulfide (molecule.C00127), 2-sulfanylethan-1-ol (molecule.ecocyc.2-MERCAPTOETHANOL).

## Annotation

CPD0-1885 + GLUTATHIONE -> 2-MERCAPTOETHANOL + OXIDIZED-GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7806|complex.ecocyc.CPLX0-7806]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7917|complex.ecocyc.CPLX0-7917]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1885|molecule.ecocyc.CPD0-1885]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6256`

## Notes

CPD0-1885 + GLUTATHIONE -> 2-MERCAPTOETHANOL + OXIDIZED-GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT
