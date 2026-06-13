---
entity_id: "reaction.ecocyc.PGLYCEROLTRANSII-RXN"
entity_type: "reaction"
name: "PGLYCEROLTRANSII-RXN"
source_database: "EcoCyc"
source_id: "PGLYCEROLTRANSII-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PGLYCEROLTRANSII-RXN

`reaction.ecocyc.PGLYCEROLTRANSII-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PGLYCEROLTRANSII-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction transfers phosphoglycerol residues between MDO molecules. EcoCyc reaction equation: CPD-16400 + MDO-D-Glucoses -> MDO-D-Glucoses + CPD-16400; direction=REVERSIBLE. This reaction transfers phosphoglycerol residues between MDO molecules.

## Biological Role

Catalyzed by mdoB (protein.P39401). Substrates: an osmoregulated periplasmic glucan with phosphoglycerol substituent (molecule.ecocyc.CPD-16400), an osmoregulated periplasmic glucan (molecule.ecocyc.MDO-D-Glucoses). Products: an osmoregulated periplasmic glucan with phosphoglycerol substituent (molecule.ecocyc.CPD-16400), an osmoregulated periplasmic glucan (molecule.ecocyc.MDO-D-Glucoses).

## Annotation

This reaction transfers phosphoglycerol residues between MDO molecules.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39401|protein.P39401]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-16400|molecule.ecocyc.CPD-16400]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MDO-D-Glucoses|molecule.ecocyc.MDO-D-Glucoses]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-16400|molecule.ecocyc.CPD-16400]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MDO-D-Glucoses|molecule.ecocyc.MDO-D-Glucoses]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-3605|molecule.ecocyc.CPD-3605]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PGLYCEROLTRANSII-RXN`

## Notes

CPD-16400 + MDO-D-Glucoses -> MDO-D-Glucoses + CPD-16400; direction=REVERSIBLE
