---
entity_id: "complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX"
entity_type: "complex"
name: "acetoacetyl-CoA transferase"
source_database: "EcoCyc"
source_id: "ACETOACETYL-COA-TRANSFER-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# acetoacetyl-CoA transferase

`complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACETOACETYL-COA-TRANSFER-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.ATOA-CPLX|complex.ecocyc.ATOA-CPLX]], [[complex.ecocyc.ATOD-CPLX|complex.ecocyc.ATOD-CPLX]]

## Enriched Summary

The growth of E. coli on short-chain fatty acids (C3-C6) requires the activation of the acids to their respective thioesters. This activation is catalyzed by acetoacetyl-CoA transferase . The reaction takes place in two half-reactions which involves a covalent enzyme-CoA . The enzyme undergoes two detectable conformational changes during the reaction . It is thought likely that the reaction proceeds by a ping-pong mechanism . The enzyme can utilize a variety of short-chain acyl-CoA and carboxylic acid substrates but exhibits maximal activity with normal and 3-keto substrates . The growth of E. coli on short-chain fatty acids (C3-C6) requires the activation of the acids to their respective thioesters. This activation is catalyzed by acetoacetyl-CoA transferase . The reaction takes place in two half-reactions which involves a covalent enzyme-CoA . The enzyme undergoes two detectable conformational changes during the reaction . It is thought likely that the reaction proceeds by a ping-pong mechanism . The enzyme can utilize a variety of short-chain acyl-CoA and carboxylic acid substrates but exhibits maximal activity with normal and 3-keto substrates .

## Biological Role

Catalyzes ACETOACETYL-COA-TRANSFER-RXN (reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN).

## Annotation

The growth of E. coli on short-chain fatty acids (C3-C6) requires the activation of the acids to their respective thioesters. This activation is catalyzed by acetoacetyl-CoA transferase . The reaction takes place in two half-reactions which involves a covalent enzyme-CoA . The enzyme undergoes two detectable conformational changes during the reaction . It is thought likely that the reaction proceeds by a ping-pong mechanism . The enzyme can utilize a variety of short-chain acyl-CoA and carboxylic acid substrates but exhibits maximal activity with normal and 3-keto substrates .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN|reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.ATOA-CPLX|complex.ecocyc.ATOA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.ATOD-CPLX|complex.ecocyc.ATOD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P76458|protein.P76458]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P76459|protein.P76459]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ACETOACETYL-COA-TRANSFER-CPLX`
- `PDB:5DBN`
- `QSPROTEOME:QS00182025`

## Notes

1*complex.ecocyc.ATOA-CPLX|1*complex.ecocyc.ATOD-CPLX
