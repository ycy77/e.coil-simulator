---
entity_id: "reaction.ecocyc.ASPARAGHYD-RXN"
entity_type: "reaction"
name: "ASPARAGHYD-RXN"
source_database: "EcoCyc"
source_id: "ASPARAGHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ASPARAGHYD-RXN

`reaction.ecocyc.ASPARAGHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASPARAGHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

ASN + WATER -> L-ASPARTATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ASN + WATER -> L-ASPARTATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L-asparaginase 1 (complex.ecocyc.ANSA-CPLX), L-asparaginase 2 (complex.ecocyc.ANSB-CPLX), isoaspartyl dipeptidase / asparaginase 3 (complex.ecocyc.CPLX0-263). Substrates: H2O (molecule.C00001), L-Asparagine (molecule.C00152). Products: L-Aspartate (molecule.C00049), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.ASPARAGINE-DEG1-PWY` L-asparagine degradation I (EcoCyc)
- `ecocyc.ASPASN-PWY` superpathway of L-aspartate and L-asparagine biosynthesis (EcoCyc)

## Annotation

ASN + WATER -> L-ASPARTATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.ASPARAGINE-DEG1-PWY` L-asparagine degradation I (EcoCyc)
- `ecocyc.ASPASN-PWY` superpathway of L-aspartate and L-asparagine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ANSA-CPLX|complex.ecocyc.ANSA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ANSB-CPLX|complex.ecocyc.ANSB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-263|complex.ecocyc.CPLX0-263]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00152|molecule.C00152]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1541|molecule.ecocyc.CPD0-1541]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ASPARAGHYD-RXN`

## Notes

ASN + WATER -> L-ASPARTATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
