---
entity_id: "complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX"
entity_type: "complex"
name: "nucleoside diphosphate kinase"
source_database: "EcoCyc"
source_id: "NUCLEOSIDE-DIP-KIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# nucleoside diphosphate kinase

`complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NUCLEOSIDE-DIP-KIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A763|protein.P0A763]]

## Enriched Summary

Nucleoside diphosphate kinase catalyzes the reaction in which the terminal phosphate of a nucleoside-triphosphate is transferred to a nucleoside-diphosphate. The enzyme exhibits broad substrate specificity. The reaction mechanism is an ordered bi-molecular ping-pong type . The intracellular levels of ATP are considerably higher than other nucleoside triphosphates. In addition, ATP is far more abundant than ADP or AMP, so there is a strong thermodynamic tendency for the potential energy of ATP to be used in the synthesis of other high-energy compounds. Therefore nucleoside diphosphate kinase is unlikely to be involved in the synthesis of ATP . In Escherichia coli the first product of the stringent response to amino acid starvation is pppGpp which is quickly converted to the more stable compound ppGpp. ppGpp is then hydrolyzed to GDP . A role for a kinase in converting GDP back to GTP to complete a cycle was proposed early (in ) and nucleoside diphosphate kinase, the product of gene ndk, was suggested as a likely candidate. This was supported by mutant studies in Salmonella enterica serovar Typhimurium (Salmonella typhimurium) although there is no direct evidence for a unique effect of Ndk on (p)ppGpp levels in E. coli or S. typhimurium (reviewed in Cashel, M., D.R. Gentry, V. J. Hernandez and D. Vinella (1996) "The Stringent Response", chapter 92, in )...

## Biological Role

Catalyzes CDPKIN-RXN (reaction.ecocyc.CDPKIN-RXN), DADPKIN-RXN (reaction.ecocyc.DADPKIN-RXN), DCDPKIN-RXN (reaction.ecocyc.DCDPKIN-RXN), DGDPKIN-RXN (reaction.ecocyc.DGDPKIN-RXN), DTDPKIN-RXN (reaction.ecocyc.DTDPKIN-RXN), DUDPKIN-RXN (reaction.ecocyc.DUDPKIN-RXN), GDPKIN-RXN (reaction.ecocyc.GDPKIN-RXN), NUCLEOSIDE-DIP-KIN-RXN (reaction.ecocyc.NUCLEOSIDE-DIP-KIN-RXN), and 1 more. Bound by Magnesium cation (molecule.C00305).

## Annotation

Nucleoside diphosphate kinase catalyzes the reaction in which the terminal phosphate of a nucleoside-triphosphate is transferred to a nucleoside-diphosphate. The enzyme exhibits broad substrate specificity. The reaction mechanism is an ordered bi-molecular ping-pong type . The intracellular levels of ATP are considerably higher than other nucleoside triphosphates. In addition, ATP is far more abundant than ADP or AMP, so there is a strong thermodynamic tendency for the potential energy of ATP to be used in the synthesis of other high-energy compounds. Therefore nucleoside diphosphate kinase is unlikely to be involved in the synthesis of ATP . In Escherichia coli the first product of the stringent response to amino acid starvation is pppGpp which is quickly converted to the more stable compound ppGpp. ppGpp is then hydrolyzed to GDP . A role for a kinase in converting GDP back to GTP to complete a cycle was proposed early (in ) and nucleoside diphosphate kinase, the product of gene ndk, was suggested as a likely candidate. This was supported by mutant studies in Salmonella enterica serovar Typhimurium (Salmonella typhimurium) although there is no direct evidence for a unique effect of Ndk on (p)ppGpp levels in E. coli or S. typhimurium (reviewed in Cashel, M., D.R. Gentry, V. J. Hernandez and D. Vinella (1996) "The Stringent Response", chapter 92, in ). The purified enzyme is tetrameric and was detected in the periplasmic fraction after cold osmotic shock . A periplasmic location for the enzyme appears inconsistent with its function . ndk is not essential for growth, but mutants display a mutator phenotype , generating high levels of mispairs that must be corrected by the mismatch-repair system . Later work has shown that ndk mutants are dependent on translesion DNA synt

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.ecocyc.CDPKIN-RXN|reaction.ecocyc.CDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DADPKIN-RXN|reaction.ecocyc.DADPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DCDPKIN-RXN|reaction.ecocyc.DCDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DGDPKIN-RXN|reaction.ecocyc.DGDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DTDPKIN-RXN|reaction.ecocyc.DTDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DUDPKIN-RXN|reaction.ecocyc.DUDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GDPKIN-RXN|reaction.ecocyc.GDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.NUCLEOSIDE-DIP-KIN-RXN|reaction.ecocyc.NUCLEOSIDE-DIP-KIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.UDPKIN-RXN|reaction.ecocyc.UDPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A763|protein.P0A763]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:NUCLEOSIDE-DIP-KIN-CPLX`
- `QSPROTEOME:QS00181713`

## Notes

4*protein.P0A763
