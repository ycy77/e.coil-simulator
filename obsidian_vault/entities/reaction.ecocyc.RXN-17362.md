---
entity_id: "reaction.ecocyc.RXN-17362"
entity_type: "reaction"
name: "RXN-17362"
source_database: "EcoCyc"
source_id: "RXN-17362"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "BACTERIAL LEADER PEPTIDASE I"
  - "SPASE II"
  - "PREMUREIN-LEADER PEPTIDASE"
  - "PROLIPOPROTEIN-SIGNAL PEPTIDASE"
  - "LIPOPROTEIN SIGNAL PEPTIDASE"
---

# RXN-17362

`reaction.ecocyc.RXN-17362`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17362`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MONOMER0-4342 + WATER -> Diacylglycerol-Prolipoproteins + Lipoprotein-signal-peptide; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: MONOMER0-4342 + WATER -> Diacylglycerol-Prolipoproteins + Lipoprotein-signal-peptide; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lspA (protein.P00804). Substrates: H2O (molecule.C00001), a [prolipoprotein]-S-1,2-diacyl-sn-glyceryl-L-cysteine (molecule.ecocyc.MONOMER0-4342). Products: an (S-diacyl-sn-glyceryl)-L-cysteinyl-[apolipoprotein] (molecule.ecocyc.Diacylglycerol-Prolipoproteins), a lipoprotein signal peptide (molecule.ecocyc.Lipoprotein-signal-peptide).

## Enriched Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Annotation

MONOMER0-4342 + WATER -> Diacylglycerol-Prolipoproteins + Lipoprotein-signal-peptide; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00804|protein.P00804]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Diacylglycerol-Prolipoproteins|molecule.ecocyc.Diacylglycerol-Prolipoproteins]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Lipoprotein-signal-peptide|molecule.ecocyc.Lipoprotein-signal-peptide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MONOMER0-4342|molecule.ecocyc.MONOMER0-4342]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.GLOBOMYCIN|molecule.ecocyc.GLOBOMYCIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-17362`

## Notes

MONOMER0-4342 + WATER -> Diacylglycerol-Prolipoproteins + Lipoprotein-signal-peptide; direction=PHYSIOL-LEFT-TO-RIGHT
