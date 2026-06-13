---
entity_id: "complex.ecocyc.ABC-58-CPLX"
entity_type: "complex"
name: "Autoinducer-2 ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-58-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "LsrACDB"
---

# Autoinducer-2 ABC transporter

`complex.ecocyc.ABC-58-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-58-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P76142|protein.P76142]], [[protein.P0AFS1|protein.P0AFS1]], [[protein.P77672|protein.P77672]], [[protein.P77257|protein.P77257]]

## Enriched Summary

Based on its similarity to the lsr operon in Salmonella typhimurium the LsrACDB ABC transporter is predicted to transport the quorum sensing autoinducer molecule AI-2. The Lsr ACDB transporter is active upon entry into stationary phase . E. coli strains with lsrCDB or with lsrACDBFG deletions remove AI-2 from culture medium significantly more slowly than wild type when grown in rich media without glucose. No difference is observed when cells are grown in the presence of glucose . The presence of a second low-affinity AI-2 transporter has been suggested . The identity of this second transport system is not known but internalization of AI-2 in a strain lacking the Lsr ACDB transporter is dependent on both CPLX0-7938 "Enzyme I" and to a lesser extent CRR-MONOMER "Enzyme IIAglc" of the phosphoenolpyruvate phosphotransferase (PTS) system . LsrA is the putative ATP-binding component. LsrC and LsrD are putative membrane components. LsrB is the putative periplasmic binding component. The genes lsrA, lsrC, lsrD and lsrB are located in a polycistronic operon that includes CPLX0-7820 "lsrF" encoding a predicted sugar aldolase, G6805-MONOMER "lsrG" encoding a protein involved in AI-2 degradation and G6806-MONOMER "tam" encoding a protein with trans-aconitate methyl-transferase activity...

## Biological Role

Catalyzes TRANS-RXN0-454 (reaction.ecocyc.TRANS-RXN0-454). Transports (4S)-4,5-dihydroxypentane-2,3-dione (molecule.ecocyc.DIHYDROXYPENTANEDIONE), hν (molecule.ecocyc.Light).

## Annotation

Based on its similarity to the lsr operon in Salmonella typhimurium the LsrACDB ABC transporter is predicted to transport the quorum sensing autoinducer molecule AI-2. The Lsr ACDB transporter is active upon entry into stationary phase . E. coli strains with lsrCDB or with lsrACDBFG deletions remove AI-2 from culture medium significantly more slowly than wild type when grown in rich media without glucose. No difference is observed when cells are grown in the presence of glucose . The presence of a second low-affinity AI-2 transporter has been suggested . The identity of this second transport system is not known but internalization of AI-2 in a strain lacking the Lsr ACDB transporter is dependent on both CPLX0-7938 "Enzyme I" and to a lesser extent CRR-MONOMER "Enzyme IIAglc" of the phosphoenolpyruvate phosphotransferase (PTS) system . LsrA is the putative ATP-binding component. LsrC and LsrD are putative membrane components. LsrB is the putative periplasmic binding component. The genes lsrA, lsrC, lsrD and lsrB are located in a polycistronic operon that includes CPLX0-7820 "lsrF" encoding a predicted sugar aldolase, G6805-MONOMER "lsrG" encoding a protein involved in AI-2 degradation and G6806-MONOMER "tam" encoding a protein with trans-aconitate methyl-transferase activity . The lsr operon is subject to complex transcriptional regulation involving cyclic AMP-CRP and the LsrR repressor . The function of AI-2 in E. coli K-12 remains unclear - it may play a role in interspecies signaling or it may be a toxic metabolite that is excluded during early growth but taken up and metabolised at a later stage (see also PWY-6153). lsr: luxS regulated

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-454|reaction.ecocyc.TRANS-RXN0-454]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.DIHYDROXYPENTANEDIONE|molecule.ecocyc.DIHYDROXYPENTANEDIONE]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AFS1|protein.P0AFS1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P76142|protein.P76142]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P77257|protein.P77257]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P77672|protein.P77672]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-58-CPLX`
- `QSPROTEOME:QS00049333`

## Notes

1*protein.P76142|1*protein.P0AFS1|1*protein.P77672|2*protein.P77257
