---
entity_id: "complex.ecocyc.CPLX0-9039"
entity_type: "complex"
name: "sensor histidine kinase HprS"
source_database: "EcoCyc"
source_id: "CPLX0-9039"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase HprS

`complex.ecocyc.CPLX0-9039`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-9039`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P76339|protein.P76339]]

## Enriched Summary

HprS is the sensor histidine kinase of the HprSR two component system initially implicated in the response to hydrogen peroxide and later shown to detect and respond to reactive chlorine species (RCS) . HprS may respond to hypochlorite through a methionine redox switch . HprS is an 'orthodox' histidine kinase; it consists of an input domain and a 'transmitter' region which contains a dimerization and histidine phosphotransfer (DHp) domain containing the histidine site of phosphorylation (His-245) and a catalytic and ATP binding (CA) domain (see ). The purified cytoplasmic histidine kinase domain of HprS has autocatalytic self-phosphorylation activity in vitro; a small amount of trans-phosphorylation of HprR and non-cognate response regulators is also observed . HprS is predicted to be an inner membrane protein with two transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . A functional HprSR two-component system is required for induced synthesis of the periplasmic methionine sulfoxide reductase, G7059-MONOMER "MsrP", in response to HOCl and related RCS . HprSR regulates the hiuH-msrPQ operon . hprS transcription is increased by copper-shock in a CusR-dependent manner . Bacterial histidine kinases typically function as homodimers; both cis- and trans-autophosphorylation mechanisms have been documented (see )...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

HprS is the sensor histidine kinase of the HprSR two component system initially implicated in the response to hydrogen peroxide and later shown to detect and respond to reactive chlorine species (RCS) . HprS may respond to hypochlorite through a methionine redox switch . HprS is an 'orthodox' histidine kinase; it consists of an input domain and a 'transmitter' region which contains a dimerization and histidine phosphotransfer (DHp) domain containing the histidine site of phosphorylation (His-245) and a catalytic and ATP binding (CA) domain (see ). The purified cytoplasmic histidine kinase domain of HprS has autocatalytic self-phosphorylation activity in vitro; a small amount of trans-phosphorylation of HprR and non-cognate response regulators is also observed . HprS is predicted to be an inner membrane protein with two transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm . A functional HprSR two-component system is required for induced synthesis of the periplasmic methionine sulfoxide reductase, G7059-MONOMER "MsrP", in response to HOCl and related RCS . HprSR regulates the hiuH-msrPQ operon . hprS transcription is increased by copper-shock in a CusR-dependent manner . Bacterial histidine kinases typically function as homodimers; both cis- and trans-autophosphorylation mechanisms have been documented (see ). HprS exhibits a cis-autophosphorylation mode .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76339|protein.P76339]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-9039`
- `QSPROTEOME:QS00196213`
- `PDB:9EPN`

## Notes

2*protein.P76339
