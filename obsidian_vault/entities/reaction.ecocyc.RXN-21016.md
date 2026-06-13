---
entity_id: "reaction.ecocyc.RXN-21016"
entity_type: "reaction"
name: "RXN-21016"
source_database: "EcoCyc"
source_id: "RXN-21016"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21016

`reaction.ecocyc.RXN-21016`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21016`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

a-YedK-protein-L-cysteine + A-SSDNA-WITH-RING-OPENED-AP-SITE -> a-single-stranded-DNA-YedK-thiazolidine- + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-YedK-protein-L-cysteine + A-SSDNA-WITH-RING-OPENED-AP-SITE -> a-single-stranded-DNA-YedK-thiazolidine- + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yedK (protein.P76318). Substrates: an N-terminal L-cysteinyl-[YedK-protein] (molecule.ecocyc.a-YedK-protein-L-cysteine). Products: H2O (molecule.C00001), a single stranded DNA-YedK thiazolidine linkage (molecule.ecocyc.a-single-stranded-DNA-YedK-thiazolidine-).

## Annotation

a-YedK-protein-L-cysteine + A-SSDNA-WITH-RING-OPENED-AP-SITE -> a-single-stranded-DNA-YedK-thiazolidine- + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P76318|protein.P76318]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.a-single-stranded-DNA-YedK-thiazolidine-|molecule.ecocyc.a-single-stranded-DNA-YedK-thiazolidine-]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.a-YedK-protein-L-cysteine|molecule.ecocyc.a-YedK-protein-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21016`

## Notes

a-YedK-protein-L-cysteine + A-SSDNA-WITH-RING-OPENED-AP-SITE -> a-single-stranded-DNA-YedK-thiazolidine- + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
