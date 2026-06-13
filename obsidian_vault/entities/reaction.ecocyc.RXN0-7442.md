---
entity_id: "reaction.ecocyc.RXN0-7442"
entity_type: "reaction"
name: "RXN0-7442"
source_database: "EcoCyc"
source_id: "RXN0-7442"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7442

`reaction.ecocyc.RXN0-7442`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7442`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-SELENOCYSTEINE + Selenium-Carrier-Protein-L-Cysteine -> L-ALPHA-ALANINE + Selenium-Carrier-Protein-S-selanyl-L-Cysteine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-SELENOCYSTEINE + Selenium-Carrier-Protein-L-Cysteine -> L-ALPHA-ALANINE + Selenium-Carrier-Protein-S-selanyl-L-Cysteine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-cysteine desulfurase SufS (complex.ecocyc.CPLX0-246). Substrates: L-Selenocysteine (molecule.C05688), a [selenium-carrier protein]-L-cysteine (molecule.ecocyc.Selenium-Carrier-Protein-L-Cysteine). Products: L-Alanine (molecule.C00041), a [selenium-carrier protein]-S-selenopersulfide (molecule.ecocyc.Selenium-Carrier-Protein-S-selanyl-L-Cysteine).

## Annotation

L-SELENOCYSTEINE + Selenium-Carrier-Protein-L-Cysteine -> L-ALPHA-ALANINE + Selenium-Carrier-Protein-S-selanyl-L-Cysteine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-246|complex.ecocyc.CPLX0-246]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Selenium-Carrier-Protein-S-selanyl-L-Cysteine|molecule.ecocyc.Selenium-Carrier-Protein-S-selanyl-L-Cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05688|molecule.C05688]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Selenium-Carrier-Protein-L-Cysteine|molecule.ecocyc.Selenium-Carrier-Protein-L-Cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7442`

## Notes

L-SELENOCYSTEINE + Selenium-Carrier-Protein-L-Cysteine -> L-ALPHA-ALANINE + Selenium-Carrier-Protein-S-selanyl-L-Cysteine; direction=PHYSIOL-LEFT-TO-RIGHT
