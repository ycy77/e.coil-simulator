---
entity_id: "reaction.ecocyc.RXN0-5199"
entity_type: "reaction"
name: "RXN0-5199"
source_database: "EcoCyc"
source_id: "RXN0-5199"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5199

`reaction.ecocyc.RXN0-5199`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5199`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GUANOSINE + Pi -> RIBOSE-1P + GUANINE; direction=REVERSIBLE EcoCyc reaction equation: GUANOSINE + Pi -> RIBOSE-1P + GUANINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by nucleoside phosphorylase PpnP (complex.ecocyc.CPLX0-8619), purine nucleoside phosphorylase (complex.ecocyc.DEOD-CPLX), xanthosine phosphorylase (complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX). Substrates: Guanosine (molecule.C00387), phosphate (molecule.ecocyc.Pi). Products: Guanine (molecule.C00242), alpha-D-Ribose 1-phosphate (molecule.C00620).

## Enriched Pathways

- `ecocyc.PWY-6608` guanosine nucleotides degradation III (EcoCyc)
- `ecocyc.PWY-6620` guanine and guanosine salvage I (EcoCyc)
- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)

## Annotation

GUANOSINE + Pi -> RIBOSE-1P + GUANINE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-6608` guanosine nucleotides degradation III (EcoCyc)
- `ecocyc.PWY-6620` guanine and guanosine salvage I (EcoCyc)
- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8619|complex.ecocyc.CPLX0-8619]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.DEOD-CPLX|complex.ecocyc.DEOD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX|complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00242|molecule.C00242]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00620|molecule.C00620]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5199`

## Notes

GUANOSINE + Pi -> RIBOSE-1P + GUANINE; direction=REVERSIBLE
