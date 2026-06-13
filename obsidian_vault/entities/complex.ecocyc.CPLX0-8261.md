---
entity_id: "complex.ecocyc.CPLX0-8261"
entity_type: "complex"
name: "thymidine kinase / deoxyuridine kinase"
source_database: "EcoCyc"
source_id: "CPLX0-8261"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# thymidine kinase / deoxyuridine kinase

`complex.ecocyc.CPLX0-8261`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8261`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P23331|protein.P23331]]

## Enriched Summary

Deoxythymidine kinase catalyzes the ATP-dependent conversion of deoxythymidine to dTMP and is an enzyme of the PWY0-181 . Biochemical analysis of thymidine kinase and its allosteric regulation was largely performed with the E. coli B enzyme. Early studies indicated that the enzyme dimerizes in the presence of an activator or an inhibitor deoxynucleotide ; in the absence of regulatory nucleotides, temperature affects the affinity of the enzyme for its substrates . Gel filtration experiments with crude extracts resulted in a native molecular weight of 82 kDa, suggesting that the E. coli K-12 enzyme also forms a homomultimeric complex . Mutants resistant to fluorodeoxyuridine (FUdR) are deficient in thymidine kinase activity . A tdk deletion mutant grows normally, but is RecA-dependent . A tdk deletion and the dut-1 allele as well as tdk and ndk are synthetically lethal. Tdk: "deoxythymidine kinase" Deoxythymidine kinase catalyzes the ATP-dependent conversion of deoxythymidine to dTMP and is an enzyme of the PWY0-181 . Biochemical analysis of thymidine kinase and its allosteric regulation was largely performed with the E. coli B enzyme. Early studies indicated that the enzyme dimerizes in the presence of an activator or an inhibitor deoxynucleotide ; in the absence of regulatory nucleotides, temperature affects the affinity of the enzyme for its substrates...

## Biological Role

Catalyzes DURIDKI-RXN (reaction.ecocyc.DURIDKI-RXN), THYKI-RXN (reaction.ecocyc.THYKI-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Deoxythymidine kinase catalyzes the ATP-dependent conversion of deoxythymidine to dTMP and is an enzyme of the PWY0-181 . Biochemical analysis of thymidine kinase and its allosteric regulation was largely performed with the E. coli B enzyme. Early studies indicated that the enzyme dimerizes in the presence of an activator or an inhibitor deoxynucleotide ; in the absence of regulatory nucleotides, temperature affects the affinity of the enzyme for its substrates . Gel filtration experiments with crude extracts resulted in a native molecular weight of 82 kDa, suggesting that the E. coli K-12 enzyme also forms a homomultimeric complex . Mutants resistant to fluorodeoxyuridine (FUdR) are deficient in thymidine kinase activity . A tdk deletion mutant grows normally, but is RecA-dependent . A tdk deletion and the dut-1 allele as well as tdk and ndk are synthetically lethal. Tdk: "deoxythymidine kinase"

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.DURIDKI-RXN|reaction.ecocyc.DURIDKI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P23331|protein.P23331]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-8261`

## Notes

protein.P23331
