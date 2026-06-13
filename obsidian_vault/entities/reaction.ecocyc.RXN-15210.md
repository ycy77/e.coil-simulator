---
entity_id: "reaction.ecocyc.RXN-15210"
entity_type: "reaction"
name: "RXN-15210"
source_database: "EcoCyc"
source_id: "RXN-15210"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15210

`reaction.ecocyc.RXN-15210`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15210`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-16398 + L-1-PHOSPHATIDYL-ETHANOLAMINE -> CPD-16401 + DIACYLGLYCEROL; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-16398 + L-1-PHOSPHATIDYL-ETHANOLAMINE -> CPD-16401 + DIACYLGLYCEROL; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by opgE (protein.P75785). Substrates: Phosphatidylethanolamine (molecule.C00350), an E. coli osmoregulated periplasmic glucan (OPG) (molecule.ecocyc.CPD-16398). Products: 1,2-Diacyl-sn-glycerol (molecule.C00641), an E. coli osmoregulated periplasmic glucan with phosphotidylethanolamine substituent (molecule.ecocyc.CPD-16401).

## Annotation

CPD-16398 + L-1-PHOSPHATIDYL-ETHANOLAMINE -> CPD-16401 + DIACYLGLYCEROL; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75785|protein.P75785]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00641|molecule.C00641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-16401|molecule.ecocyc.CPD-16401]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-16398|molecule.ecocyc.CPD-16398]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15210`

## Notes

CPD-16398 + L-1-PHOSPHATIDYL-ETHANOLAMINE -> CPD-16401 + DIACYLGLYCEROL; direction=LEFT-TO-RIGHT
