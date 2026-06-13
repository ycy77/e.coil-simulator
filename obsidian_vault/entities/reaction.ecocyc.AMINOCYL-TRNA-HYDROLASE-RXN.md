---
entity_id: "reaction.ecocyc.AMINOCYL-TRNA-HYDROLASE-RXN"
entity_type: "reaction"
name: "AMINOCYL-TRNA-HYDROLASE-RXN"
source_database: "EcoCyc"
source_id: "AMINOCYL-TRNA-HYDROLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AMINOCYL-TRNA-HYDROLASE-RXN

`reaction.ecocyc.AMINOCYL-TRNA-HYDROLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AMINOCYL-TRNA-HYDROLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + N-Substituted-Aminoacyl-tRNA -> tRNAs + N-Substituted-Amino-Acids + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + N-Substituted-Aminoacyl-tRNA -> tRNAs + N-Substituted-Amino-Acids + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pth (protein.P0A7D1), arfB (protein.P40711). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), an N-modified amino acid (molecule.ecocyc.N-Substituted-Amino-Acids).

## Annotation

WATER + N-Substituted-Aminoacyl-tRNA -> tRNAs + N-Substituted-Amino-Acids + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A7D1|protein.P0A7D1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P40711|protein.P40711]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N-Substituted-Amino-Acids|molecule.ecocyc.N-Substituted-Amino-Acids]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:AMINOCYL-TRNA-HYDROLASE-RXN`

## Notes

WATER + N-Substituted-Aminoacyl-tRNA -> tRNAs + N-Substituted-Amino-Acids + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
