---
entity_id: "reaction.ecocyc.RXN0-4961"
entity_type: "reaction"
name: "RXN0-4961"
source_database: "EcoCyc"
source_id: "RXN0-4961"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4961

`reaction.ecocyc.RXN0-4961`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4961`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the 3' to 5' exonucleolytic cleavage of DNA to yield 5'-mononucleotides. EcoCyc reaction equation: DNA-N + WATER -> Deoxy-Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the 3' to 5' exonucleolytic cleavage of DNA to yield 5'-mononucleotides.

## Biological Role

Catalyzed by polA (protein.P00582), dnaQ (protein.P03007), polB (protein.P21189). Substrates: H2O (molecule.C00001). Products: a 2'-deoxyribonucleoside 5'-monophosphate (molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates).

## Annotation

This reaction is the 3' to 5' exonucleolytic cleavage of DNA to yield 5'-mononucleotides.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P00582|protein.P00582]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P03007|protein.P03007]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P21189|protein.P21189]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates|molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4961`

## Notes

DNA-N + WATER -> Deoxy-Ribonucleoside-Monophosphates; direction=PHYSIOL-LEFT-TO-RIGHT
