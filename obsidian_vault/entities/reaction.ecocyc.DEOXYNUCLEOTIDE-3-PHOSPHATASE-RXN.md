---
entity_id: "reaction.ecocyc.DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN

`reaction.ecocyc.DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Deoxy-Ribonucleoside-3P + WATER -> Deoxy-Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Deoxy-Ribonucleoside-3P + WATER -> Deoxy-Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX). Substrates: H2O (molecule.C00001), a 2'-deoxyribonucleoside 3'-monophosphate (molecule.ecocyc.Deoxy-Ribonucleoside-3P). Products: a 2'-deoxyribonucleoside (molecule.ecocyc.Deoxy-Ribonucleosides), phosphate (molecule.ecocyc.Pi).

## Annotation

Deoxy-Ribonucleoside-3P + WATER -> Deoxy-Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleosides|molecule.ecocyc.Deoxy-Ribonucleosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleoside-3P|molecule.ecocyc.Deoxy-Ribonucleoside-3P]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN`

## Notes

Deoxy-Ribonucleoside-3P + WATER -> Deoxy-Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
