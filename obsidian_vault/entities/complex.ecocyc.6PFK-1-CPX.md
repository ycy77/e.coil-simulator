---
entity_id: "complex.ecocyc.6PFK-1-CPX"
entity_type: "complex"
name: "6-phosphofructokinase 1"
source_database: "EcoCyc"
source_id: "6PFK-1-CPX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PFK I"
---

# 6-phosphofructokinase 1

`complex.ecocyc.6PFK-1-CPX`

## Static

- Type: `complex`
- Source: `EcoCyc:6PFK-1-CPX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A796|protein.P0A796]]

## Enriched Summary

6-phosphofructokinase I (PFK I, PfkA) catalyzes the phosphorylation of fructose-6-phosphate and is a key enzyme regulating the GLYCOLYSIS glycolysis pathway. The enzyme can not catalyze the reverse reaction in vivo. E. coli contains two PFK isozymes, PFK I and 6PFK-2-CPX PFK II, which do not share sequence similarity . More than 90% of the phosphofructokinase activity present in wild type E. coli can be attributed to PFK I . The enzyme shows cooperative kinetics with the substrate fructose-6-phosphate, but not with the other substrate, ATP . PFK I also catalyzes phosphorylation of sedoheptulose-7-phosphate as part of the PWY0-1517 . Ligand-detected NMR spectroscopy revealed additional functional interactions between endogenous metabolites and PfkA . The active site, kinetic mechanism, pH dependence, allosteric properties, and effector binding sites of the enzyme have been studied in depth. Mutants in the active site that change cooperativity have been generated . pH affects both cooperativity and maximum velocity of the enzyme . Also see publications on the kinetic mechanism , allosteric properties , and the effector binding site . A kinetic model of the enzyme has been constructed . The folding and subunit association pathway of E. coli Pfk I has also been studied . Crystal structures of PFK I have been solved with and without activators and inhibitors...

## Biological Role

Catalyzes 6PFRUCTPHOS-RXN (reaction.ecocyc.6PFRUCTPHOS-RXN), RXN0-6541 (reaction.ecocyc.RXN0-6541). Bound by Magnesium cation (molecule.C00305).

## Annotation

6-phosphofructokinase I (PFK I, PfkA) catalyzes the phosphorylation of fructose-6-phosphate and is a key enzyme regulating the GLYCOLYSIS glycolysis pathway. The enzyme can not catalyze the reverse reaction in vivo. E. coli contains two PFK isozymes, PFK I and 6PFK-2-CPX PFK II, which do not share sequence similarity . More than 90% of the phosphofructokinase activity present in wild type E. coli can be attributed to PFK I . The enzyme shows cooperative kinetics with the substrate fructose-6-phosphate, but not with the other substrate, ATP . PFK I also catalyzes phosphorylation of sedoheptulose-7-phosphate as part of the PWY0-1517 . Ligand-detected NMR spectroscopy revealed additional functional interactions between endogenous metabolites and PfkA . The active site, kinetic mechanism, pH dependence, allosteric properties, and effector binding sites of the enzyme have been studied in depth. Mutants in the active site that change cooperativity have been generated . pH affects both cooperativity and maximum velocity of the enzyme . Also see publications on the kinetic mechanism , allosteric properties , and the effector binding site . A kinetic model of the enzyme has been constructed . The folding and subunit association pathway of E. coli Pfk I has also been studied . Crystal structures of PFK I have been solved with and without activators and inhibitors . Based on sequence similarity, PfkA was predicted to be an NAD+ kinase . In a strain containing the hypomorphic csrA51 allele grown in M9 glucose medium, expression of pfkA is reduced. Overexpression of PfkA partially rescues the growth defect of the csrA51 mutant . A pfkA mutant shows a very low growth rate on glucose as the sole source of carbon and energy . A ΔpfkA mutant shows increased flux through the OXIDATIVEPEN

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.6PFRUCTPHOS-RXN|reaction.ecocyc.6PFRUCTPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6541|reaction.ecocyc.RXN0-6541]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A796|protein.P0A796]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:6PFK-1-CPX`
- `QSPROTEOME:QS00182731`

## Notes

4*protein.P0A796
