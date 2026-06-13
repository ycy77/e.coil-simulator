---
entity_id: "reaction.ecocyc.RXN0-7454"
entity_type: "reaction"
name: "RXN0-7454"
source_database: "EcoCyc"
source_id: "RXN0-7454"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7454

`reaction.ecocyc.RXN0-7454`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7454`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CcmE-Protein-Heme + Donor-H1 -> CcmE-Protein-Heme-Ox + Acceptor + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CcmE-Protein-Heme + Donor-H1 -> CcmE-Protein-Heme-Ox + Acceptor + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ccmF (protein.P33927). Products: H+ (molecule.C00080).

## Annotation

CcmE-Protein-Heme + Donor-H1 -> CcmE-Protein-Heme-Ox + Acceptor + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P33927|protein.P33927]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN0-7454`

## Notes

CcmE-Protein-Heme + Donor-H1 -> CcmE-Protein-Heme-Ox + Acceptor + PROTON; direction=LEFT-TO-RIGHT
