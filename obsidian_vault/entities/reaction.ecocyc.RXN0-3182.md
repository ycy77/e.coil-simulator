---
entity_id: "reaction.ecocyc.RXN0-3182"
entity_type: "reaction"
name: "RXN0-3182"
source_database: "EcoCyc"
source_id: "RXN0-3182"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3182

`reaction.ecocyc.RXN0-3182`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3182`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction involves ATP-independent hydrolysis of a peptide bond following a valine or isoleucine. EcoCyc reaction equation: General-Protein-Substrates + WATER -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction involves ATP-independent hydrolysis of a peptide bond following a valine or isoleucine.

## Biological Role

Catalyzed by serine endoprotease (complex.ecocyc.CPLX0-8183), periplasmic serine endoprotease (complex.ecocyc.CPLX0-8187). Substrates: H2O (molecule.C00001).

## Annotation

This reaction involves ATP-independent hydrolysis of a peptide bond following a valine or isoleucine.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8183|complex.ecocyc.CPLX0-8183]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8187|complex.ecocyc.CPLX0-8187]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3182`

## Notes

General-Protein-Substrates + WATER -> Peptides-holder + Peptide-Holder-Alternative; direction=PHYSIOL-LEFT-TO-RIGHT
