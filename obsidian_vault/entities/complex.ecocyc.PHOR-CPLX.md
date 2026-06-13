---
entity_id: "complex.ecocyc.PHOR-CPLX"
entity_type: "complex"
name: "sensor histidine kinase PhoR"
source_database: "EcoCyc"
source_id: "PHOR-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PhoR"
---

# sensor histidine kinase PhoR

`complex.ecocyc.PHOR-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PHOR-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P08400|protein.P08400]]

## Enriched Summary

PhoR is the sensor kinase of the PhoRB two component signal transduction pathway. PhoR indirectly senses and responds to variations in the level of extracellular inorganic phosphate (Pi) by phosphorylating or dephosphorylating its cognate response regulator PhoB. PhoR is an anchored inner membrane protein comprised of five domains: an N-terminal transmembrane domain, a charged linker domain, a Per-Arnt-Sim (PAS) domain, a dimerisation and histidine phosphoacceptor (DHp) domain and a C-terminal kinase domain . PhoR is an atypical sensor kinase as it does not contain a large periplasmic domain; the signal sensing and kinase domains of PhoR are located in the cytoplasm . Under limiting environmental Pi, PhoR is believed to be in an active signaling conformation resulting in the phosphorylation and activation of PhoB and subsequent induction of the Pho regulon. Activation under limiting environmental Pi is considered to be the default state. Excess levels of Pi (>4uM) result in an inhibited form of PhoR which interferes with phosphorylation of PhoB and prevents its activity as a transcription factor . The phosphate transporter ABC-27-CPLX "PstSCAB" and the chaperone like protein CPLX0-8113 "PhoU" are both necessary for inhibition of the PhoRB system . PhoR interacts physically with PhoU; PhoU and PstSCAB are implicated in a model for phosphate signaling to PhoR...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN), RXN0-7329 (reaction.ecocyc.RXN0-7329).

## Annotation

PhoR is the sensor kinase of the PhoRB two component signal transduction pathway. PhoR indirectly senses and responds to variations in the level of extracellular inorganic phosphate (Pi) by phosphorylating or dephosphorylating its cognate response regulator PhoB. PhoR is an anchored inner membrane protein comprised of five domains: an N-terminal transmembrane domain, a charged linker domain, a Per-Arnt-Sim (PAS) domain, a dimerisation and histidine phosphoacceptor (DHp) domain and a C-terminal kinase domain . PhoR is an atypical sensor kinase as it does not contain a large periplasmic domain; the signal sensing and kinase domains of PhoR are located in the cytoplasm . Under limiting environmental Pi, PhoR is believed to be in an active signaling conformation resulting in the phosphorylation and activation of PhoB and subsequent induction of the Pho regulon. Activation under limiting environmental Pi is considered to be the default state. Excess levels of Pi (>4uM) result in an inhibited form of PhoR which interferes with phosphorylation of PhoB and prevents its activity as a transcription factor . The phosphate transporter ABC-27-CPLX "PstSCAB" and the chaperone like protein CPLX0-8113 "PhoU" are both necessary for inhibition of the PhoRB system . PhoR interacts physically with PhoU; PhoU and PstSCAB are implicated in a model for phosphate signaling to PhoR . The PhoR-PhoU complex may sense and respond to alternate conformations of the PstSCAB transporter . Soluble PhoR (PhoR*, residues 83-431) autophosphorylates in the presence of ATP and transfers a phosphate to PhoB; PhoR* also has phospho-PhoB phosphatase activity in vitro . PhoR autophosphorylates in cis, that is, the ATP-binding site and the phosphorylation site (His-213) are present on the same protomer of the Ar

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7329|reaction.ecocyc.RXN0-7329]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P08400|protein.P08400]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PHOR-CPLX`
- `QSPROTEOME:QS00049747`

## Notes

2*protein.P08400
