---
entity_id: "reaction.ecocyc.TRANS-RXN0-508"
entity_type: "reaction"
name: "TRANS-RXN0-508"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-508"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-508

`reaction.ecocyc.TRANS-RXN0-508`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-508`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E.coli strains that are unble to synthesize cysteine can use exogneous sulfur sources such cystine, cysteine or the related molecule, djenkolate, for growth . E. coli K-12 is positive for growth when djenkolate is supplied as the sole sulfur source on Biolog plates. A transport protein has not been experimentally determined, however there is some evidence that a putative ABC transport complex (YecCSFliY) may transport the related molecule, L-cystine . EcoCyc reaction equation: CPD-3740 + ATP + WATER -> CPD-3740 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. E.coli strains that are unble to synthesize cysteine can use exogneous sulfur sources such cystine, cysteine or the related molecule, djenkolate, for growth . E. coli K-12 is positive for growth when djenkolate is supplied as the sole sulfur source on Biolog plates. A transport protein has not been experimentally determined, however there is some evidence that a putative ABC transport complex (YecCSFliY) may transport the related molecule, L-cystine .

## Biological Role

Catalyzed by cystine ABC transporter (complex.ecocyc.CPLX0-8152). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-djenkolate (molecule.ecocyc.CPD-3740). Products: ADP (molecule.C00008), H+ (molecule.C00080), L-djenkolate (molecule.ecocyc.CPD-3740), phosphate (molecule.ecocyc.Pi).

## Annotation

E.coli strains that are unble to synthesize cysteine can use exogneous sulfur sources such cystine, cysteine or the related molecule, djenkolate, for growth . E. coli K-12 is positive for growth when djenkolate is supplied as the sole sulfur source on Biolog plates. A transport protein has not been experimentally determined, however there is some evidence that a putative ABC transport complex (YecCSFliY) may transport the related molecule, L-cystine .

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8152|complex.ecocyc.CPLX0-8152]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-3740|molecule.ecocyc.CPD-3740]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3740|molecule.ecocyc.CPD-3740]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-508`

## Notes

CPD-3740 + ATP + WATER -> CPD-3740 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
