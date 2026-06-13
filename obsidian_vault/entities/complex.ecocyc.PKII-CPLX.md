---
entity_id: "complex.ecocyc.PKII-CPLX"
entity_type: "complex"
name: "pyruvate kinase 2"
source_database: "EcoCyc"
source_id: "PKII-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "pyruvate kinase A"
  - "type II pyruvate kinase"
---

# pyruvate kinase 2

`complex.ecocyc.PKII-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PKII-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P21599|protein.P21599]]

## Enriched Summary

Pyruvate kinase is a key allosteric enzyme of GLYCOLYSIS glycolysis, catalyzing one of the two substrate-level phosphorylation steps that generate ATP. The second product, pyruvate, is either used in many metabolic pathways to synthesize cell materials, or is further oxidized via the TCA cycle. The transfer of the phosphoryl group of phosphoenolpyruvate to ADP to form pyruvate and ATP is the last step in the glycolytic pathway and is irreversible under physiological conditions . Two forms of pyruvate kinase have been described in E. coli. Pyruvate kinase I encoded by EG10804 and pyruvate kinase II encoded by EG10803 differ in physical and chemical properties as well as in their kinetic behavior. Although the two enzymes are under independent genetic control, they do coexist in a wide range of nutritional and metabolic states . The two enzymes are not interchangeable. Both show positive cooperative effects with respect to their substrate phosphoenolpyruvate, although pyruvate kinase II shows only limited cooperativity. Pyruvate kinase II is allosterically activated by AMP and several sugar phosphates, whereas pyruvate kinase I is activated by fructose 1,6-bisphosphate and inhibited by ATP and succinyl-CoA. Both enzymes are homotetramers...

## Biological Role

Catalyzes PEPDEPHOS-RXN (reaction.ecocyc.PEPDEPHOS-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

Pyruvate kinase is a key allosteric enzyme of GLYCOLYSIS glycolysis, catalyzing one of the two substrate-level phosphorylation steps that generate ATP. The second product, pyruvate, is either used in many metabolic pathways to synthesize cell materials, or is further oxidized via the TCA cycle. The transfer of the phosphoryl group of phosphoenolpyruvate to ADP to form pyruvate and ATP is the last step in the glycolytic pathway and is irreversible under physiological conditions . Two forms of pyruvate kinase have been described in E. coli. Pyruvate kinase I encoded by EG10804 and pyruvate kinase II encoded by EG10803 differ in physical and chemical properties as well as in their kinetic behavior. Although the two enzymes are under independent genetic control, they do coexist in a wide range of nutritional and metabolic states . The two enzymes are not interchangeable. Both show positive cooperative effects with respect to their substrate phosphoenolpyruvate, although pyruvate kinase II shows only limited cooperativity. Pyruvate kinase II is allosterically activated by AMP and several sugar phosphates, whereas pyruvate kinase I is activated by fructose 1,6-bisphosphate and inhibited by ATP and succinyl-CoA. Both enzymes are homotetramers . While the carbon source has little effect on the presence of pyruvate kinase II, expression of the enzyme is induced under anaerobic growth conditions . Pyruvate kinase activity from E. coli B showed a broad specificity for nucleotide diphosphate acceptors . The protein sequences of PykA from E. coli B REL606 and K-12 MG1655 are 100% identical. Genes pykF and pykA are often used in metabolic engineering due to their importance in the control of metabolic flux in glycolysis. In various strains of E. coli the effects of single and double

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P21599|protein.P21599]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:PKII-CPLX`
- `QSPROTEOME:QS00188845`

## Notes

4*protein.P21599
