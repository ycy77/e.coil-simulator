---
entity_id: "reaction.ecocyc.3.4.15.5-RXN"
entity_type: "reaction"
name: "3.4.15.5-RXN"
source_database: "EcoCyc"
source_id: "3.4.15.5-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Dipeptidyl carboxypeptidase"
---

# 3.4.15.5-RXN

`reaction.ecocyc.3.4.15.5-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.15.5-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction is the hydrolysis of a peptide bond in an amino-blocked small peptide. EcoCyc reaction equation: Peptidyl-Dipeptidase-Dcp-Substrates + WATER -> Peptides-holder + DIPEPTIDES; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a peptide bond in an amino-blocked small peptide.

## Biological Role

Catalyzed by dcp (protein.P24171). Substrates: H2O (molecule.C00001). Products: a dipeptide (molecule.ecocyc.DIPEPTIDES).

## Annotation

This reaction is the hydrolysis of a peptide bond in an amino-blocked small peptide.

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `activates` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P24171|protein.P24171]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.DIPEPTIDES|molecule.ecocyc.DIPEPTIDES]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2067|molecule.ecocyc.CPD0-2067]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.4.15.5-RXN`

## Notes

Peptidyl-Dipeptidase-Dcp-Substrates + WATER -> Peptides-holder + DIPEPTIDES; direction=PHYSIOL-LEFT-TO-RIGHT
