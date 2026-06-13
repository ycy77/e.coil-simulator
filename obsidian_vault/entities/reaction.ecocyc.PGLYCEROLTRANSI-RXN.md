---
entity_id: "reaction.ecocyc.PGLYCEROLTRANSI-RXN"
entity_type: "reaction"
name: "PGLYCEROLTRANSI-RXN"
source_database: "EcoCyc"
source_id: "PGLYCEROLTRANSI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PGLYCEROLTRANSI-RXN

`reaction.ecocyc.PGLYCEROLTRANSI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PGLYCEROLTRANSI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction is part of membrane-derived oligosaccharide (MDO) synthesis. Phosphatidyl residues are transferred from phosphatidylglycerol to membrane-derived oligosaccharides or to certain β-glucoside acceptors. EcoCyc reaction equation: MDO-D-Glucoses + L-1-PHOSPHATIDYL-GLYCEROL -> CPD-16400 + DIACYLGLYCEROL + PROTON; direction=REVERSIBLE. This reaction is part of membrane-derived oligosaccharide (MDO) synthesis. Phosphatidyl residues are transferred from phosphatidylglycerol to membrane-derived oligosaccharides or to certain β-glucoside acceptors.

## Biological Role

Catalyzed by mdoB (protein.P39401). Substrates: Phosphatidylglycerol (molecule.C00344), an osmoregulated periplasmic glucan (molecule.ecocyc.MDO-D-Glucoses). Products: H+ (molecule.C00080), 1,2-Diacyl-sn-glycerol (molecule.C00641), an osmoregulated periplasmic glucan with phosphoglycerol substituent (molecule.ecocyc.CPD-16400).

## Annotation

This reaction is part of membrane-derived oligosaccharide (MDO) synthesis. Phosphatidyl residues are transferred from phosphatidylglycerol to membrane-derived oligosaccharides or to certain β-glucoside acceptors.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39401|protein.P39401]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00641|molecule.C00641]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-16400|molecule.ecocyc.CPD-16400]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00344|molecule.C00344]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MDO-D-Glucoses|molecule.ecocyc.MDO-D-Glucoses]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PGLYCEROLTRANSI-RXN`

## Notes

MDO-D-Glucoses + L-1-PHOSPHATIDYL-GLYCEROL -> CPD-16400 + DIACYLGLYCEROL + PROTON; direction=REVERSIBLE
