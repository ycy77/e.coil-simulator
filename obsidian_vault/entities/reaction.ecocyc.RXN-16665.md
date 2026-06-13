---
entity_id: "reaction.ecocyc.RXN-16665"
entity_type: "reaction"
name: "RXN-16665"
source_database: "EcoCyc"
source_id: "RXN-16665"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16665

`reaction.ecocyc.RXN-16665`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16665`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction may also be catalysed by the L,D-transpeptidases LdtA, LdtB, LdtC and LdtE EcoCyc reaction equation: A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE + GLY -> CPD-17969 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction may also be catalysed by the L,D-transpeptidases LdtA, LdtB, LdtC and LdtE

## Biological Role

Catalyzed by ycbB (protein.P22525). Substrates: Glycine (molecule.C00037), a donor peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine) tetrapeptide (molecule.ecocyc.A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE). Products: D-Alanine (molecule.C00133), a nascent peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-glycine) tetrapeptide (molecule.ecocyc.CPD-17969).

## Enriched Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This reaction may also be catalysed by the L,D-transpeptidases LdtA, LdtB, LdtC and LdtE

## Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P22525|protein.P22525]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-17969|molecule.ecocyc.CPD-17969]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE|molecule.ecocyc.A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16665`

## Notes

A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE + GLY -> CPD-17969 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
