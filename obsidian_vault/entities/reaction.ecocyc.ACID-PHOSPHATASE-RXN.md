---
entity_id: "reaction.ecocyc.ACID-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "ACID-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "ACID-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "GLYCEROPHOSPHATASE"
  - "PHOSPHOMONOESTERASE"
  - "ACID PHOSPHOMONOESTERASE"
---

# ACID-PHOSPHATASE-RXN

`reaction.ecocyc.ACID-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACID-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

WIDE SPECIFICITY. ALSO CATALYSES TRANSPHOSPHORYLATIONS. EcoCyc reaction equation: WATER + Orthophosphoric-Monoesters -> Alcohols + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. WIDE SPECIFICITY. ALSO CATALYSES TRANSPHOSPHORYLATIONS.

## Biological Role

Catalyzed by acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX). Substrates: H2O (molecule.C00001), Orthophosphoric monoester (molecule.C01153). Products: an alcohol (molecule.ecocyc.Alcohols), phosphate (molecule.ecocyc.Pi).

## Annotation

WIDE SPECIFICITY. ALSO CATALYSES TRANSPHOSPHORYLATIONS.

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[molecule.C00469|molecule.C00469]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Alcohols|molecule.ecocyc.Alcohols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01153|molecule.C01153]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00299|molecule.C00299]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Nucleosides|molecule.ecocyc.Nucleosides]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACID-PHOSPHATASE-RXN`

## Notes

WATER + Orthophosphoric-Monoesters -> Alcohols + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
