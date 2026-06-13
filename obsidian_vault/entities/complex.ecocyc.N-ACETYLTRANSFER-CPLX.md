---
entity_id: "complex.ecocyc.N-ACETYLTRANSFER-CPLX"
entity_type: "complex"
name: "N-acetylglutamate synthase"
source_database: "EcoCyc"
source_id: "N-ACETYLTRANSFER-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "NAGS"
  - "acetyl-CoA:L-glutamate N-acetyltransferase"
  - "amino-acid-N-acetyltransferase"
---

# N-acetylglutamate synthase

`complex.ecocyc.N-ACETYLTRANSFER-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:N-ACETYLTRANSFER-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6C5|protein.P0A6C5]]

## Enriched Summary

N-acetylglutamate synthase (ArgA) carries out the first steps in the ARGSYN-PWY and the GLUTORN-PWY. ArgA catalyzes the synthesis of N-acetylglutamate from L-glutamate and acetyl-CoA . This activity is highly specific for acetyl-CoA and L-glutamate . L-arginine blocks synthesis of N-acetylglutamate both by directly inhibiting N-acetylglutamate synthase enzymatic activity and by limiting the synthesis of ArgA . The molecular weight of ArgA multimers can vary from 144-224 kD depending on the concentration of ArgA. However, the presence of either L-arginine or N-acetyl-L-glutamate stabilizes ArgA at 300 kD, indicating that it is active as a hexamer . ArgA is most stable at pH 7, though its maximal activity has been reported at pH 9 and pH 10 . A temperature-sensitive mutation in this gene was identified that showed potential as a growth-switch for genetic engineering . N-acetylglutamate synthase (ArgA) carries out the first steps in the ARGSYN-PWY and the GLUTORN-PWY. ArgA catalyzes the synthesis of N-acetylglutamate from L-glutamate and acetyl-CoA . This activity is highly specific for acetyl-CoA and L-glutamate . L-arginine blocks synthesis of N-acetylglutamate both by directly inhibiting N-acetylglutamate synthase enzymatic activity and by limiting the synthesis of ArgA . The molecular weight of ArgA multimers can vary from 144-224 kD depending on the concentration of ArgA...

## Biological Role

Catalyzes N-ACETYLTRANSFER-RXN (reaction.ecocyc.N-ACETYLTRANSFER-RXN).

## Annotation

N-acetylglutamate synthase (ArgA) carries out the first steps in the ARGSYN-PWY and the GLUTORN-PWY. ArgA catalyzes the synthesis of N-acetylglutamate from L-glutamate and acetyl-CoA . This activity is highly specific for acetyl-CoA and L-glutamate . L-arginine blocks synthesis of N-acetylglutamate both by directly inhibiting N-acetylglutamate synthase enzymatic activity and by limiting the synthesis of ArgA . The molecular weight of ArgA multimers can vary from 144-224 kD depending on the concentration of ArgA. However, the presence of either L-arginine or N-acetyl-L-glutamate stabilizes ArgA at 300 kD, indicating that it is active as a hexamer . ArgA is most stable at pH 7, though its maximal activity has been reported at pH 9 and pH 10 . A temperature-sensitive mutation in this gene was identified that showed potential as a growth-switch for genetic engineering .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.N-ACETYLTRANSFER-RXN|reaction.ecocyc.N-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6C5|protein.P0A6C5]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:N-ACETYLTRANSFER-CPLX`
- `QSPROTEOME:QS00188483`

## Notes

6*protein.P0A6C5
