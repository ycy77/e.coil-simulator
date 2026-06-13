---
entity_id: "complex.ecocyc.PKI-COMPLEX"
entity_type: "complex"
name: "pyruvate kinase 1"
source_database: "EcoCyc"
source_id: "PKI-COMPLEX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "type I pyruvate kinase"
  - "pyruvate kinase type F"
  - "Pyk1"
---

# pyruvate kinase 1

`complex.ecocyc.PKI-COMPLEX`

## Static

- Type: `complex`
- Source: `EcoCyc:PKI-COMPLEX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AD61|protein.P0AD61]]

## Enriched Summary

Pyruvate kinase is a key allosteric enzyme of GLYCOLYSIS glycolysis, catalyzing one of the two substrate-level phosphorylation steps that generate ATP. The second product, pyruvate, is either used in many metabolic pathways to synthesize cell materials, or is further oxidized via the TCA cycle. The transfer of the phosphoryl group of phosphoenolpyruvate to ADP to form pyruvate and ATP is the last step in the glycolytic pathway and is irreversible under physiological conditions . Two forms of pyruvate kinase have been described in E. coli. Pyruvate kinase I (PykF) and pyruvate kinase II, encoded by EG10803, differ in physical and chemical properties as well as in their kinetic behavior. Although the two enzymes are under independent genetic control, they do coexist in a wide range of nutritional and metabolic states . The two enzymes are not interchangeable. Both show positive cooperative effects with respect to their substrate phosphoenolpyruvate, although pyruvate kinase II shows only limited cooperativity. Pyruvate kinase I is activated by fructose 1,6-bisphosphate and inhibited by ATP and succinyl-CoA, whereas pyruvate kinase II is allosterically activated by AMP and several sugar phosphates. Both enzymes are homotetramers...

## Biological Role

Catalyzes PEPDEPHOS-RXN (reaction.ecocyc.PEPDEPHOS-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

Pyruvate kinase is a key allosteric enzyme of GLYCOLYSIS glycolysis, catalyzing one of the two substrate-level phosphorylation steps that generate ATP. The second product, pyruvate, is either used in many metabolic pathways to synthesize cell materials, or is further oxidized via the TCA cycle. The transfer of the phosphoryl group of phosphoenolpyruvate to ADP to form pyruvate and ATP is the last step in the glycolytic pathway and is irreversible under physiological conditions . Two forms of pyruvate kinase have been described in E. coli. Pyruvate kinase I (PykF) and pyruvate kinase II, encoded by EG10803, differ in physical and chemical properties as well as in their kinetic behavior. Although the two enzymes are under independent genetic control, they do coexist in a wide range of nutritional and metabolic states . The two enzymes are not interchangeable. Both show positive cooperative effects with respect to their substrate phosphoenolpyruvate, although pyruvate kinase II shows only limited cooperativity. Pyruvate kinase I is activated by fructose 1,6-bisphosphate and inhibited by ATP and succinyl-CoA, whereas pyruvate kinase II is allosterically activated by AMP and several sugar phosphates. Both enzymes are homotetramers . Mutation of pykF, but not pykA, results in significant enhancement of the pyruvate concentration oscillations which are observed by exposure of starved E. coli cells to glycolytic carbon sources . Pyruvate kinase I has been purified and characterized from cell extracts of E. coli K-12 , and recombinant enzyme has been overproduced and characterized . A detailed kinetic analysis of pyruvate kinase I demonstrated the dependence of the reaction rate on the concentrations of various substrates, and the resulting sigmoid or hyperbolic curves. Several

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPDEPHOS-RXN|reaction.ecocyc.PEPDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AD61|protein.P0AD61]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:PKI-COMPLEX`
- `QSPROTEOME:QS00199263`

## Notes

4*protein.P0AD61
