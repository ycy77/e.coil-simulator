---
entity_id: "complex.ecocyc.GUANYL-KIN-CPLX"
entity_type: "complex"
name: "guanylate kinase"
source_database: "EcoCyc"
source_id: "GUANYL-KIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "GMP kinase"
---

# guanylate kinase

`complex.ecocyc.GUANYL-KIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GUANYL-KIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60546|protein.P60546]]

## Enriched Summary

Nucleotide monophosphate kinases are important enzymes in the maintenance of nucleotide pools. They are specific for the nucleobase of the phosphate acceptor substrate. They belong to the nucleoside monophosphate kinase (NMPK) superfamily The product of gene gmk reversibly transfers the γ-phosphoryl group of the nucleoside triphosphate donor (ATP) to the acceptor nucleoside monophosphate (GMP or dGMP) to produce the corresponding nucleoside diphosphate (GDP or dGDP) and ADP . The E. coli K-12 enzyme is multimeric, and its protomeric state is determined by ionic strength conditions. Under high ionic strength the enzyme is a dimer of 43 kDa and under low ionic strength the enzyme is a tetramer of 92.5 kDa. Tetramerization lowers the level of interaction between binding sites and decreases the total activity . Later structural and calorimetric studies showed E. coli Gmk to be in equilibrium between a dimeric and a hexameric form, which shifts to the dimeric form under physiological conditions. The hexamer was observed in four different crystal forms . The human enzyme is a target for chemotherapeutic agents and also plays a role in activation of antiviral and antineoplastic drugs . The bacterial enzyme is of interest as a drug target. The crystal structure of the E. coli enzyme has been used as a model for these applications...

## Biological Role

Catalyzes GMKALT-RXN (reaction.ecocyc.GMKALT-RXN), GUANYL-KIN-RXN (reaction.ecocyc.GUANYL-KIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Nucleotide monophosphate kinases are important enzymes in the maintenance of nucleotide pools. They are specific for the nucleobase of the phosphate acceptor substrate. They belong to the nucleoside monophosphate kinase (NMPK) superfamily The product of gene gmk reversibly transfers the γ-phosphoryl group of the nucleoside triphosphate donor (ATP) to the acceptor nucleoside monophosphate (GMP or dGMP) to produce the corresponding nucleoside diphosphate (GDP or dGDP) and ADP . The E. coli K-12 enzyme is multimeric, and its protomeric state is determined by ionic strength conditions. Under high ionic strength the enzyme is a dimer of 43 kDa and under low ionic strength the enzyme is a tetramer of 92.5 kDa. Tetramerization lowers the level of interaction between binding sites and decreases the total activity . Later structural and calorimetric studies showed E. coli Gmk to be in equilibrium between a dimeric and a hexameric form, which shifts to the dimeric form under physiological conditions. The hexamer was observed in four different crystal forms . The human enzyme is a target for chemotherapeutic agents and also plays a role in activation of antiviral and antineoplastic drugs . The bacterial enzyme is of interest as a drug target. The crystal structure of the E. coli enzyme has been used as a model for these applications . A novel, conditional guanylate kinase-deficient strain of E. coli strain has been constructed for use in the evaluation of drug activation by this enzyme and to identify drug-resistant variants . Review: Review: Jensen, K.F., G. Dandanell, B. Hove-Jensen, and M. Willemoes (2008) "Nucleotides, Nucleosides and Nucleobases" EcoSal 3.6.2

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GMKALT-RXN|reaction.ecocyc.GMKALT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GUANYL-KIN-RXN|reaction.ecocyc.GUANYL-KIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P60546|protein.P60546]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GUANYL-KIN-CPLX`
- `QSPROTEOME:QS00203773`

## Notes

2*protein.P60546
