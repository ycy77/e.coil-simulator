---
entity_id: "reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN"
entity_type: "reaction"
name: "XANTHOSINEPHOSPHORY-RXN"
source_database: "EcoCyc"
source_id: "XANTHOSINEPHOSPHORY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# XANTHOSINEPHOSPHORY-RXN

`reaction.ecocyc.XANTHOSINEPHOSPHORY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:XANTHOSINEPHOSPHORY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of nucleotide metabolism. EcoCyc reaction equation: XANTHOSINE + Pi -> XANTHINE + RIBOSE-1P; direction=REVERSIBLE. This reaction is part of nucleotide metabolism.

## Biological Role

Catalyzed by nucleoside phosphorylase PpnP (complex.ecocyc.CPLX0-8619), xanthosine phosphorylase (complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX). Substrates: Xanthosine (molecule.C01762), phosphate (molecule.ecocyc.Pi). Products: Xanthine (molecule.C00385), alpha-D-Ribose 1-phosphate (molecule.C00620).

## Enriched Pathways

- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)
- `ecocyc.SALVPURINE2-PWY` xanthine and xanthosine salvage (EcoCyc)

## Annotation

This reaction is part of nucleotide metabolism.

## Pathways

- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)
- `ecocyc.SALVPURINE2-PWY` xanthine and xanthosine salvage (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8619|complex.ecocyc.CPLX0-8619]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX|complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00620|molecule.C00620]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01762|molecule.C01762]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:XANTHOSINEPHOSPHORY-RXN`

## Notes

XANTHOSINE + Pi -> XANTHINE + RIBOSE-1P; direction=REVERSIBLE
