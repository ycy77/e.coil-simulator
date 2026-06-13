---
entity_id: "reaction.ecocyc.ALPHAGALACTOSID-RXN"
entity_type: "reaction"
name: "ALPHAGALACTOSID-RXN"
source_database: "EcoCyc"
source_id: "ALPHAGALACTOSID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALPHAGALACTOSID-RXN

`reaction.ecocyc.ALPHAGALACTOSID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALPHAGALACTOSID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of galactose, galactoside and glucose catabolism. EcoCyc reaction equation: WATER + MELIBIOSE -> D-galactopyranose + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT. Part of galactose, galactoside and glucose catabolism.

## Biological Role

Catalyzed by α-galactosidase (complex.ecocyc.ALPHAGALACTOSID-CPLX). Substrates: H2O (molecule.C00001), Melibiose (molecule.C05402). Products: D-Glucose (molecule.C00031), D-Galactose (molecule.C00124).

## Enriched Pathways

- `ecocyc.PWY0-1301` melibiose degradation (EcoCyc)

## Annotation

Part of galactose, galactoside and glucose catabolism.

## Pathways

- `ecocyc.PWY0-1301` melibiose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `activates` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.Thiols|molecule.ecocyc.Thiols]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ALPHAGALACTOSID-CPLX|complex.ecocyc.ALPHAGALACTOSID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05402|molecule.C05402]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.15-DIDEOXY-15-IMINO-D-GALACTITOL|molecule.ecocyc.15-DIDEOXY-15-IMINO-D-GALACTITOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.5-AMINO-5-DEOXY-D-GALACTOPYRANOSIDE|molecule.ecocyc.5-AMINO-5-DEOXY-D-GALACTOPYRANOSIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-1490|molecule.ecocyc.CPD-1490]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ALPHAGALACTOSID-RXN`

## Notes

WATER + MELIBIOSE -> D-galactopyranose + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT
