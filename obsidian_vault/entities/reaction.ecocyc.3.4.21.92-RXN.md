---
entity_id: "reaction.ecocyc.3.4.21.92-RXN"
entity_type: "reaction"
name: "3.4.21.92-RXN"
source_database: "EcoCyc"
source_id: "3.4.21.92-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Endopeptidase Ti"
  - "Protease Ti"
  - "Caseinolytic protease"
---

# 3.4.21.92-RXN

`reaction.ecocyc.3.4.21.92-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.21.92-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolysis of a peptide bond by a serine protease activity. Specificity is chiefly defined by an associated chaperone activity provided by the ATP-dependent chaperones ClpA and ClpX. EcoCyc reaction equation: General-Protein-Substrates + ATP + WATER -> Peptides-holder + Peptide-Holder-Alternative + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a peptide bond by a serine protease activity. Specificity is chiefly defined by an associated chaperone activity provided by the ATP-dependent chaperones ClpA and ClpX.

## Biological Role

Catalyzed by ClpP serine protease (complex.ecocyc.CPLX0-3101), ClpAP (complex.ecocyc.CPLX0-3104), ClpXP (complex.ecocyc.CPLX0-3107), ClpAXP (complex.ecocyc.CPLX0-3108). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

This reaction is the hydrolysis of a peptide bond by a serine protease activity. Specificity is chiefly defined by an associated chaperone activity provided by the ATP-dependent chaperones ClpA and ClpX.

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3101|complex.ecocyc.CPLX0-3101]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3104|complex.ecocyc.CPLX0-3104]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3107|complex.ecocyc.CPLX0-3107]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3108|complex.ecocyc.CPLX0-3108]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE|molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3.4.21.92-RXN`

## Notes

General-Protein-Substrates + ATP + WATER -> Peptides-holder + Peptide-Holder-Alternative + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
