---
entity_id: "reaction.ecocyc.RXN-19774"
entity_type: "reaction"
name: "RXN-19774"
source_database: "EcoCyc"
source_id: "RXN-19774"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19774

`reaction.ecocyc.RXN-19774`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19774`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Diacylglycerol-Prolipoproteins + L-1-PHOSPHATIDYL-ETHANOLAMINE -> a-mature-triacylated-lipoprotein + 2-ACYL-GPE + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Diacylglycerol-Prolipoproteins + L-1-PHOSPHATIDYL-ETHANOLAMINE -> a-mature-triacylated-lipoprotein + 2-ACYL-GPE + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lnt (protein.P23930). Substrates: Phosphatidylethanolamine (molecule.C00350), an (S-diacyl-sn-glyceryl)-L-cysteinyl-[apolipoprotein] (molecule.ecocyc.Diacylglycerol-Prolipoproteins). Products: H+ (molecule.C00080), 2-Acyl-sn-glycero-3-phosphoethanolamine (molecule.C05973), an N-acyl-(S-diacyl-sn-glyceryl)-L-cysteinyl-[lipoprotein] (molecule.ecocyc.a-mature-triacylated-lipoprotein).

## Annotation

Diacylglycerol-Prolipoproteins + L-1-PHOSPHATIDYL-ETHANOLAMINE -> a-mature-triacylated-lipoprotein + 2-ACYL-GPE + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P23930|protein.P23930]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05973|molecule.C05973]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.a-mature-triacylated-lipoprotein|molecule.ecocyc.a-mature-triacylated-lipoprotein]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Diacylglycerol-Prolipoproteins|molecule.ecocyc.Diacylglycerol-Prolipoproteins]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19774`

## Notes

Diacylglycerol-Prolipoproteins + L-1-PHOSPHATIDYL-ETHANOLAMINE -> a-mature-triacylated-lipoprotein + 2-ACYL-GPE + PROTON; direction=LEFT-TO-RIGHT
