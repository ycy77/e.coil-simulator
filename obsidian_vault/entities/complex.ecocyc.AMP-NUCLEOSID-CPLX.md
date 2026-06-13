---
entity_id: "complex.ecocyc.AMP-NUCLEOSID-CPLX"
entity_type: "complex"
name: "AMP nucleosidase"
source_database: "EcoCyc"
source_id: "AMP-NUCLEOSID-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# AMP nucleosidase

`complex.ecocyc.AMP-NUCLEOSID-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AMP-NUCLEOSID-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AE12|protein.P0AE12]]

## Enriched Summary

AMP nucleosidase is the primary intracellular mechanism for AMP degradation in E. coli. The adenine which is produced in the nucleosidase reaction can be reincorporated into the purine pool . The enzyme catalyzes the hydrolysis of the N-glycosidic bond of AMP producing produce adenine and D-ribose 5-phosphate. An amp mutant carrying a small deletion has been used to analyze structure-function relationships . The reaction mechanism has been studied by analysis of kinetic isotope effects . Amn is a member of the nucleoside phosphorylase (nucleosidase) family I which includes, for example, E. coli DeoD and Udp . Expression of amp is induced under limiting phosphate conditions . Expression of amn is activated by PhoB . Crystal structures of AMP nucleosidase in the unliganded form and in complex with formycin 5'-monophosphate or inorganic phosphate have been determined . The enzyme is a homohexamer , and each monomer consists of a catalytic and a proposed regulatory domain. The catalytic domain resembles nucleoside phosphorylases . The enzyme appears to be found only in prokaryotes and is of interest as an antimicrobial drug target . In E. coli knockout of amn by mutation caused an over 30% increase in ATP levels across its viable temperature range and the mutants also had significantly higher viability at low temperatures than wild-type cells...

## Biological Role

Catalyzes AMP-NUCLEOSID-RXN (reaction.ecocyc.AMP-NUCLEOSID-RXN).

## Annotation

AMP nucleosidase is the primary intracellular mechanism for AMP degradation in E. coli. The adenine which is produced in the nucleosidase reaction can be reincorporated into the purine pool . The enzyme catalyzes the hydrolysis of the N-glycosidic bond of AMP producing produce adenine and D-ribose 5-phosphate. An amp mutant carrying a small deletion has been used to analyze structure-function relationships . The reaction mechanism has been studied by analysis of kinetic isotope effects . Amn is a member of the nucleoside phosphorylase (nucleosidase) family I which includes, for example, E. coli DeoD and Udp . Expression of amp is induced under limiting phosphate conditions . Expression of amn is activated by PhoB . Crystal structures of AMP nucleosidase in the unliganded form and in complex with formycin 5'-monophosphate or inorganic phosphate have been determined . The enzyme is a homohexamer , and each monomer consists of a catalytic and a proposed regulatory domain. The catalytic domain resembles nucleoside phosphorylases . The enzyme appears to be found only in prokaryotes and is of interest as an antimicrobial drug target . In E. coli knockout of amn by mutation caused an over 30% increase in ATP levels across its viable temperature range and the mutants also had significantly higher viability at low temperatures than wild-type cells . These data, along with pathway engineering studies , suggest that Amn may be important in the regulation of intracellular pools of adenine nucleotides.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.AMP-NUCLEOSID-RXN|reaction.ecocyc.AMP-NUCLEOSID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AE12|protein.P0AE12]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:AMP-NUCLEOSID-CPLX`
- `QSPROTEOME:QS00181723`

## Notes

6*protein.P0AE12
