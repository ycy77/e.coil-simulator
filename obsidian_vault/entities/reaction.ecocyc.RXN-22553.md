---
entity_id: "reaction.ecocyc.RXN-22553"
entity_type: "reaction"
name: "RXN-22553"
source_database: "EcoCyc"
source_id: "RXN-22553"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22553

`reaction.ecocyc.RXN-22553`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22553`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

LolA-Lipoprotein-Complex -> a-mature-triacylated-lipoprotein + LolA; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: LolA-Lipoprotein-Complex -> a-mature-triacylated-lipoprotein + LolA; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lolB (protein.P61320). Products: an N-acyl-(S-diacyl-sn-glyceryl)-L-cysteinyl-[lipoprotein] (molecule.ecocyc.a-mature-triacylated-lipoprotein).

## Enriched Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Annotation

LolA-Lipoprotein-Complex -> a-mature-triacylated-lipoprotein + LolA; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P61320|protein.P61320]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.a-mature-triacylated-lipoprotein|molecule.ecocyc.a-mature-triacylated-lipoprotein]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN-22553`

## Notes

LolA-Lipoprotein-Complex -> a-mature-triacylated-lipoprotein + LolA; direction=PHYSIOL-LEFT-TO-RIGHT
