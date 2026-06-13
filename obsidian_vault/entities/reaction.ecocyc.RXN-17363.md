---
entity_id: "reaction.ecocyc.RXN-17363"
entity_type: "reaction"
name: "RXN-17363"
source_database: "EcoCyc"
source_id: "RXN-17363"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17363

`reaction.ecocyc.RXN-17363`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17363`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Diacylglycerol-Prolipoproteins + Phosphoglycerides -> a-mature-triacylated-lipoprotein + 1-Lyso-phospholipids + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Diacylglycerol-Prolipoproteins + Phosphoglycerides -> a-mature-triacylated-lipoprotein + 1-Lyso-phospholipids + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lnt (protein.P23930). Substrates: an (S-diacyl-sn-glyceryl)-L-cysteinyl-[apolipoprotein] (molecule.ecocyc.Diacylglycerol-Prolipoproteins), a phosphoglyceride (molecule.ecocyc.Phosphoglycerides). Products: H+ (molecule.C00080), a 1-lysophospholipid (molecule.ecocyc.1-Lyso-phospholipids), an N-acyl-(S-diacyl-sn-glyceryl)-L-cysteinyl-[lipoprotein] (molecule.ecocyc.a-mature-triacylated-lipoprotein).

## Enriched Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Annotation

Diacylglycerol-Prolipoproteins + Phosphoglycerides -> a-mature-triacylated-lipoprotein + 1-Lyso-phospholipids + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P23930|protein.P23930]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.1-Lyso-phospholipids|molecule.ecocyc.1-Lyso-phospholipids]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.a-mature-triacylated-lipoprotein|molecule.ecocyc.a-mature-triacylated-lipoprotein]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Diacylglycerol-Prolipoproteins|molecule.ecocyc.Diacylglycerol-Prolipoproteins]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Phosphoglycerides|molecule.ecocyc.Phosphoglycerides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17363`

## Notes

Diacylglycerol-Prolipoproteins + Phosphoglycerides -> a-mature-triacylated-lipoprotein + 1-Lyso-phospholipids + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
