---
entity_id: "complex.ecocyc.CPLX0-8271"
entity_type: "complex"
name: "F- channel"
source_database: "EcoCyc"
source_id: "CPLX0-8271"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# F- channel

`complex.ecocyc.CPLX0-8271`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8271`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37002|protein.P37002]]

## Enriched Summary

crcB encodes an F- specific ion channel. CrcB mediated passive export of F- counteracts the weak acid accumulation, or ion trapping, effect of hydrogen fluoride that would otherwise concentrate F- in the cytoplasm to potentially toxic levels . E. coli crcB knock-out mutants show increased sensitivity to fluoride (see also ). In contrast to wild-type cells, an E. coli crcB knock out strain is unable to grow in the presence of 50mM F- and exhibits high expression of an F--responsive reporter construct at very low (0.2mM) fluoride ion concentration . CrcB is a member of the Fluc-family of highly selective F- channels . Fluc-family channels are constructed as dimers of identical or homologous membrane-embedded domains arranged in an inverted-topology fashion . Crystal structures of representative Fluc channels in complex with synthetic monobodies - high affinity inhibitors which block the channels and also act as crystallization chaperones - have been obtained. The structures (which include 'Fluc-Ec2' from an E. coli virulence plasmid) support a conclusion that Flucs are double-barrelled channels with two F- pathways spanning the membrane . PagP (CrcA), CspE, and CrcB together are involved in resistance to camphor-induced chromosome decondensation...

## Biological Role

Catalyzes export of F- (reaction.ecocyc.TRANS-RXN0-498).

## Annotation

crcB encodes an F- specific ion channel. CrcB mediated passive export of F- counteracts the weak acid accumulation, or ion trapping, effect of hydrogen fluoride that would otherwise concentrate F- in the cytoplasm to potentially toxic levels . E. coli crcB knock-out mutants show increased sensitivity to fluoride (see also ). In contrast to wild-type cells, an E. coli crcB knock out strain is unable to grow in the presence of 50mM F- and exhibits high expression of an F--responsive reporter construct at very low (0.2mM) fluoride ion concentration . CrcB is a member of the Fluc-family of highly selective F- channels . Fluc-family channels are constructed as dimers of identical or homologous membrane-embedded domains arranged in an inverted-topology fashion . Crystal structures of representative Fluc channels in complex with synthetic monobodies - high affinity inhibitors which block the channels and also act as crystallization chaperones - have been obtained. The structures (which include 'Fluc-Ec2' from an E. coli virulence plasmid) support a conclusion that Flucs are double-barrelled channels with two F- pathways spanning the membrane . PagP (CrcA), CspE, and CrcB together are involved in resistance to camphor-induced chromosome decondensation . A pagP cspE crcB triple null mutant exhibits greater than wild-type sensitivity to camphor, which causes chromosome decondensation, and enhances the nucleoid morphology phenotype of a topoisomerase IV mutant . Overexpression of pagP, cspE and crcB together results in resistance to camphor , increased DNA supercoiling and increased expression of rcsA . Overexpression of pagP, cspE and crcB together suppress phenotypes of a mukB mutant , a gyrase mutant, and a topoisomerase IV mutant . CrcB: "confers resistance to camphor B"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-498|reaction.ecocyc.TRANS-RXN0-498]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P37002|protein.P37002]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-8271`
- `QSPROTEOME:QS00196535`

## Notes

2*protein.P37002
