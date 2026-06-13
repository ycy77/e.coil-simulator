---
entity_id: "complex.ecocyc.CPLX0-8095"
entity_type: "complex"
name: "CP4-57 prophage; RNase LS, toxin of the RnlAB toxin-antitoxin system"
source_database: "EcoCyc"
source_id: "CPLX0-8095"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# CP4-57 prophage; RNase LS, toxin of the RnlAB toxin-antitoxin system

`complex.ecocyc.CPLX0-8095`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8095`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P52129|protein.P52129]]

## Enriched Summary

RNase LS (RnlA) is the toxin of a novel toxin-antitoxin system. Overexpression of RnlA in ΔrnlAB cells inhibits cell growth and causes mRNA degradation, while overexpression of RnlB in wild-type cells suppresses the growth defect of the T4 dmd mutant, indicating that RnlB inhibits RnlA activity. RnlA and RnlB interact directly. The RnlA protein is relatively stable compared to RnlB . RnlA was first identified as an endoribonuclease that cleaves bacteriophage T4 late mRNA in T4 dmd mutants . EG10860-MONOMER RNase HI is required for this RnlA activity; it also enhances RnlA-mediated cell toxicity . Interestingly, the T4 Dmd protein acts as a promiscuous antitoxin in vivo, binding to both RnlA and LsoA, the toxin of a plasmid-derived TA system . RnlA also plays a role in cellular mRNA degradation. rnlA mutants display slowed degradation of many mRNAs as well as accumulation of a 307-nucleotide fragment derived from 23S rRNA . The cyaA mRNA was shown to be a target of RnlA . A crystal structure of RnlA has been solved. The protein consists of three domains, an N-terminal domain, a central N repeated domain and a C-terminal Dmd-binding domain (DBD); the overall structure is unique. The DBD domain is responsible for dimerization of RnlA, its interaction with the antitoxins RnlB and T4 Dmd, and its toxicity . The cleavage of T4 soc mRNA depends on translation termination...

## Biological Role

Catalyzes RXN0-5509 (reaction.ecocyc.RXN0-5509).

## Annotation

RNase LS (RnlA) is the toxin of a novel toxin-antitoxin system. Overexpression of RnlA in ΔrnlAB cells inhibits cell growth and causes mRNA degradation, while overexpression of RnlB in wild-type cells suppresses the growth defect of the T4 dmd mutant, indicating that RnlB inhibits RnlA activity. RnlA and RnlB interact directly. The RnlA protein is relatively stable compared to RnlB . RnlA was first identified as an endoribonuclease that cleaves bacteriophage T4 late mRNA in T4 dmd mutants . EG10860-MONOMER RNase HI is required for this RnlA activity; it also enhances RnlA-mediated cell toxicity . Interestingly, the T4 Dmd protein acts as a promiscuous antitoxin in vivo, binding to both RnlA and LsoA, the toxin of a plasmid-derived TA system . RnlA also plays a role in cellular mRNA degradation. rnlA mutants display slowed degradation of many mRNAs as well as accumulation of a 307-nucleotide fragment derived from 23S rRNA . The cyaA mRNA was shown to be a target of RnlA . A crystal structure of RnlA has been solved. The protein consists of three domains, an N-terminal domain, a central N repeated domain and a C-terminal Dmd-binding domain (DBD); the overall structure is unique. The DBD domain is responsible for dimerization of RnlA, its interaction with the antitoxins RnlB and T4 Dmd, and its toxicity . The cleavage of T4 soc mRNA depends on translation termination . RNase LS activity purifies as a large multi-component complex with the RnlA gene product as a central component . EG10860-MONOMER RNase HI interacts with RnlA in vivo and enhances the RNA cleavage activity of RnlA in vitro . An rnlA mutant is sensitive to high salt concentrations. The effect is due to stabilization of the cyaA mRNA . rnlA expression is induced 2-fold upon overexpression of rpoH and is negati

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5509|reaction.ecocyc.RXN0-5509]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P52129|protein.P52129]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8095`
- `QSPROTEOME:QS00196979`

## Notes

2*protein.P52129
