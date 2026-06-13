---
entity_id: "reaction.ecocyc.TRANS-RXN0-529"
entity_type: "reaction"
name: "TRANS-RXN0-529"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-529"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-529

`reaction.ecocyc.TRANS-RXN0-529`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-529`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hydroquinone is the product of the enzymatic splitting of the phosphorylated β-glucoside, arbutin-6-phosphate. E.coli K-12 do not utilise β-glucosides but inducible mutants (β-glu+) can be isolated which do (see CPLX-154). Hydroquinone can be detected in the supernatant of β-glu+ cells cultured with arbutin . EcoCyc reaction equation: HYDROQUINONE -> HYDROQUINONE; direction=LEFT-TO-RIGHT. Hydroquinone is the product of the enzymatic splitting of the phosphorylated β-glucoside, arbutin-6-phosphate. E.coli K-12 do not utilise β-glucosides but inducible mutants (β-glu+) can be isolated which do (see CPLX-154). Hydroquinone can be detected in the supernatant of β-glu+ cells cultured with arbutin .

## Biological Role

Substrates: Hydroquinone (molecule.C00530). Products: Hydroquinone (molecule.C00530).

## Annotation

Hydroquinone is the product of the enzymatic splitting of the phosphorylated β-glucoside, arbutin-6-phosphate. E.coli K-12 do not utilise β-glucosides but inducible mutants (β-glu+) can be isolated which do (see CPLX-154). Hydroquinone can be detected in the supernatant of β-glu+ cells cultured with arbutin .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00530|molecule.C00530]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00530|molecule.C00530]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-529`

## Notes

HYDROQUINONE -> HYDROQUINONE; direction=LEFT-TO-RIGHT
