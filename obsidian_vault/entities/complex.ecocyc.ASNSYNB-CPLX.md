---
entity_id: "complex.ecocyc.ASNSYNB-CPLX"
entity_type: "complex"
name: "asparagine synthetase B"
source_database: "EcoCyc"
source_id: "ASNSYNB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# asparagine synthetase B

`complex.ecocyc.ASNSYNB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ASNSYNB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P22106|protein.P22106]]

## Enriched Summary

Asparagine synthetase B (AsnB) is one of two asparagine synthetases in E. coli that catalyzes the ATP-dependent conversion of aspartate to asparagine using either glutamine or ammonium as a nitrogen source . The other enzyme is ASNSYNA-CPLX "AsnA". AsnB is the less active of the two enzymes . AsnB belongs to the Ntn (N-terminal nucleophile) class of amidotransferases (also known as PurF type, or class II). This class utilizes an N-terminal cysteine residue as an active site nucleophile during the hydrolysis of glutamine to glutamate and ammonium . Unlike related Ntn amidotransferases, AsnB lacks a conserved histidine in its glutamine amindotransferase domain . In an effort to elucidate the reaction mechanism, recombinant wild-type and site-directed mutants of AsnB have been overexpressed, purified and kinetically characterized. The N-terminal cysteine (Cys-1) is important for both the glutaminase and glutamine-dependent activities of AsnB, but not for its ammonia-dependent asparagine synthesis activity. Cys-1 is not required for glutamine binding, but acts as the active site nucleophile . Asn-74 has a role in catalyzing nitrogen transfer from glutamine, and Arg-30 also has a role in glutamine-dependent asparagine synthesis . Alternative substrate data also suggest a role for Asn-74 in catalyzing glutamine-dependent nitrogen transfer...

## Biological Role

Catalyzes ASNSYNA-RXN (reaction.ecocyc.ASNSYNA-RXN), ASNSYNB-RXN (reaction.ecocyc.ASNSYNB-RXN), GLUTAMIN-RXN (reaction.ecocyc.GLUTAMIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Asparagine synthetase B (AsnB) is one of two asparagine synthetases in E. coli that catalyzes the ATP-dependent conversion of aspartate to asparagine using either glutamine or ammonium as a nitrogen source . The other enzyme is ASNSYNA-CPLX "AsnA". AsnB is the less active of the two enzymes . AsnB belongs to the Ntn (N-terminal nucleophile) class of amidotransferases (also known as PurF type, or class II). This class utilizes an N-terminal cysteine residue as an active site nucleophile during the hydrolysis of glutamine to glutamate and ammonium . Unlike related Ntn amidotransferases, AsnB lacks a conserved histidine in its glutamine amindotransferase domain . In an effort to elucidate the reaction mechanism, recombinant wild-type and site-directed mutants of AsnB have been overexpressed, purified and kinetically characterized. The N-terminal cysteine (Cys-1) is important for both the glutaminase and glutamine-dependent activities of AsnB, but not for its ammonia-dependent asparagine synthesis activity. Cys-1 is not required for glutamine binding, but acts as the active site nucleophile . Asn-74 has a role in catalyzing nitrogen transfer from glutamine, and Arg-30 also has a role in glutamine-dependent asparagine synthesis . Alternative substrate data also suggest a role for Asn-74 in catalyzing glutamine-dependent nitrogen transfer . The nitrogen transfer mechanism was probed by measuring heavy atom kinetic isotope effects for the glutamine-dependent activities of the enzyme, which suggested the formation of several possible intermediates . Cys-523 is involved in aspartate binding and is in close proximity to the ATP binding site . Residues involved in formation of a β-aspartyl-AMP reaction intermediate in the nitrogen transfer reaction include Arg-325, Thr-322 and Thr

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ASNSYNA-RXN|reaction.ecocyc.ASNSYNA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ASNSYNB-RXN|reaction.ecocyc.ASNSYNB-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GLUTAMIN-RXN|reaction.ecocyc.GLUTAMIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P22106|protein.P22106]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ASNSYNB-CPLX`
- `QSPROTEOME:QS00181799`

## Notes

2*protein.P22106
