---
entity_id: "complex.ecocyc.ANTHRANSYN-CPLX"
entity_type: "complex"
name: "anthranilate synthase"
source_database: "EcoCyc"
source_id: "ANTHRANSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# anthranilate synthase

`complex.ecocyc.ANTHRANSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ANTHRANSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00895|protein.P00895]], [[protein.P00904|protein.P00904]]

## Enriched Summary

Anthranilate synthase (TrpDE) catalyzes the first step in the pathway of tryptophan biosynthesis, and is subject to feedback regulation by the end product of the pathway, L-tryptophan . One of its component monomers also catalyzes the second step in the same pathway. TrpDE catalyzes the glutamine amidotransferase reaction that adds an amine group from glutamine to chorismate to yield anthranilate and glutamate . TrpE on its own can carry out an alternate version of this reaction, using ammonium sulfate rather than glutamine as an amino donor . TrpD dramatically increases the affinity of TrpE for glutamine over TrpE alone . TrpDE functions as a as complex comprising two TrpD and two TrpE monomers . In line with their role in synthesizing tryptophan, the components of this complex contain almost no tryptophan, with one residue in TrpD and none in TrpE . Translation of TrpE and TrpD is coordinated via a specialized intercistronic sequence between trpE and trpD. If the latter portion of the trpE mRNA is not translated, trpD mRNA translation is markedly reduced . The complex from Salmonella enterica subsp. enterica serovar Typhimurium (Salmonella typhimurium) has also been extensively studied. More recent reports have included its crystal structure 1...

## Biological Role

Catalyzes ANTHRANSYN-RXN (reaction.ecocyc.ANTHRANSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Anthranilate synthase (TrpDE) catalyzes the first step in the pathway of tryptophan biosynthesis, and is subject to feedback regulation by the end product of the pathway, L-tryptophan . One of its component monomers also catalyzes the second step in the same pathway. TrpDE catalyzes the glutamine amidotransferase reaction that adds an amine group from glutamine to chorismate to yield anthranilate and glutamate . TrpE on its own can carry out an alternate version of this reaction, using ammonium sulfate rather than glutamine as an amino donor . TrpD dramatically increases the affinity of TrpE for glutamine over TrpE alone . TrpDE functions as a as complex comprising two TrpD and two TrpE monomers . In line with their role in synthesizing tryptophan, the components of this complex contain almost no tryptophan, with one residue in TrpD and none in TrpE . Translation of TrpE and TrpD is coordinated via a specialized intercistronic sequence between trpE and trpD. If the latter portion of the trpE mRNA is not translated, trpD mRNA translation is markedly reduced . The complex from Salmonella enterica subsp. enterica serovar Typhimurium (Salmonella typhimurium) has also been extensively studied. More recent reports have included its crystal structure 1.9 Å resolution , the thermodynamics of complex-catalyzed reactions , intersubunit communication mechanisms , and aminodeoxyisochorismate as an enzyme-bound reaction intermediate .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ANTHRANSYN-RXN|reaction.ecocyc.ANTHRANSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00895|protein.P00895]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P00904|protein.P00904]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ANTHRANSYN-CPLX`
- `QSPROTEOME:QS00126970`

## Notes

2*protein.P00895|2*protein.P00904
