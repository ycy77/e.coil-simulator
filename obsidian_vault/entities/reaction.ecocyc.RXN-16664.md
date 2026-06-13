---
entity_id: "reaction.ecocyc.RXN-16664"
entity_type: "reaction"
name: "RXN-16664"
source_database: "EcoCyc"
source_id: "RXN-16664"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16664

`reaction.ecocyc.RXN-16664`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16664`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction may also be catalysed by the L,D-transpeptidases LdtA, LdtB, LdtC and LdtE . EcoCyc reaction equation: CPD-17926 + WATER -> CPD-17968 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction may also be catalysed by the L,D-transpeptidases LdtA, LdtB, LdtC and LdtE .

## Biological Role

Catalyzed by mepS (protein.P0AFV4), ycbB (protein.P22525), mepH (protein.P76190). Substrates: H2O (molecule.C00001), a nascent peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine) tetrapeptide (molecule.ecocyc.CPD-17926). Products: D-Alanine (molecule.C00133), a nascent peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimelate) tripeptide (molecule.ecocyc.CPD-17968).

## Enriched Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This reaction may also be catalysed by the L,D-transpeptidases LdtA, LdtB, LdtC and LdtE .

## Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AFV4|protein.P0AFV4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P22525|protein.P22525]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76190|protein.P76190]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-17968|molecule.ecocyc.CPD-17968]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-17926|molecule.ecocyc.CPD-17926]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16664`

## Notes

CPD-17926 + WATER -> CPD-17968 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
