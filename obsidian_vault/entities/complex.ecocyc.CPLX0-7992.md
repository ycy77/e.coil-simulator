---
entity_id: "complex.ecocyc.CPLX0-7992"
entity_type: "complex"
name: "lipopolysaccharide transport system"
source_database: "EcoCyc"
source_id: "CPLX0-7992"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# lipopolysaccharide transport system

`complex.ecocyc.CPLX0-7992`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7992`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-7628|complex.ecocyc.CPLX0-7628]], [[protein.P0ADC6|protein.P0ADC6]], [[protein.P0ADV9|protein.P0ADV9]], [[protein.P0ADV1|protein.P0ADV1]], [[protein.P0A9V1|protein.P0A9V1]], [[protein.P0AF98|protein.P0AF98]]

## Enriched Summary

In E. coli K-12 the system responsible for transporting lipolysaccharide (LPS) from the inner membrane to the outer membrane consists of seven Lpt proteins - LptB, LptF, LptG, LptC, LptA, LptD and LptE. Together these proteins form a transenvelope bridge that transports LPS from the inner membrane, across the periplasm to the outer leaflet of the outer membrane. LptB2FG is an ATP Binding Cassette (ABC) transporter which, together with LptC, extracts LPS from the inner membrane. LptA is a periplasmic protein initially thought to be an LPS chaperone but now known to act as a bridge between the inner membrane and the outer membrane. LptDE is the outer membrane complex that functions to assemble LPS at the cell surface.The Lpt system acts downstream from an LPS flippase, CPLX0-7704 "MsbA", which is responsible for flipping the lipid A-core structure across the inner membrane. Cross-talk between the lipopolysaccharide transport system (the Lpt pathway) and the lipoprotein transport system (the Lol pathway) may facilitate trafficking of some surface-exposed lipoproteins . LptF and LptG are inner membrane proteins each with six predicted transmembrane segments and a C-terminus located in the cytoplasm . lptF and lptG are essential in E. coli...

## Biological Role

Catalyzes TRANS-RXN-237 (reaction.ecocyc.TRANS-RXN-237), TRANS-RXN0-638 (reaction.ecocyc.TRANS-RXN0-638). Transports lipid A-core oligosaccharide (E. coli K-12 core type) (molecule.ecocyc.CPD-21359), lipid A-core oligosaccharide (E. coli K-12 core type with D-GlcNAc) (molecule.ecocyc.CPD0-939), hν (molecule.ecocyc.Light).

## Annotation

In E. coli K-12 the system responsible for transporting lipolysaccharide (LPS) from the inner membrane to the outer membrane consists of seven Lpt proteins - LptB, LptF, LptG, LptC, LptA, LptD and LptE. Together these proteins form a transenvelope bridge that transports LPS from the inner membrane, across the periplasm to the outer leaflet of the outer membrane. LptB2FG is an ATP Binding Cassette (ABC) transporter which, together with LptC, extracts LPS from the inner membrane. LptA is a periplasmic protein initially thought to be an LPS chaperone but now known to act as a bridge between the inner membrane and the outer membrane. LptDE is the outer membrane complex that functions to assemble LPS at the cell surface.The Lpt system acts downstream from an LPS flippase, CPLX0-7704 "MsbA", which is responsible for flipping the lipid A-core structure across the inner membrane. Cross-talk between the lipopolysaccharide transport system (the Lpt pathway) and the lipoprotein transport system (the Lol pathway) may facilitate trafficking of some surface-exposed lipoproteins . LptF and LptG are inner membrane proteins each with six predicted transmembrane segments and a C-terminus located in the cytoplasm . lptF and lptG are essential in E. coli . Depletion of LptF and/or LptG results in increased outer membrane permeability and lipopolysaccharides do not reach the outer leaflet of the outer membrane . LptB contains an ATP-binding domain and purifies as part of a 140 kD inner membrane complex . LptC contains a predicted N-terminal membrane spanning domain and a large soluble domain oriented towards the periplasm . LptC binds smooth and rough LPS in vitro . LptC forms a complex with LptF, LptG and LptB and is implicated in regulating LptB2FG mediated extraction of LPS . Purified Lp

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-237|reaction.ecocyc.TRANS-RXN-237]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-638|reaction.ecocyc.TRANS-RXN0-638]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-21359|molecule.ecocyc.CPD-21359]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD0-939|molecule.ecocyc.CPD0-939]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (8)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7628|complex.ecocyc.CPLX0-7628]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A9V1|protein.P0A9V1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P0ADC1|protein.P0ADC1]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ADC6|protein.P0ADC6]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ADV1|protein.P0ADV1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ADV9|protein.P0ADV9]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AF98|protein.P0AF98]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P31554|protein.P31554]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-7992`
- `PDB:4RHB`
- `QSPROTEOME:QS00182721`

## Notes

1*complex.ecocyc.CPLX0-7628|1*protein.P0ADC6|1*protein.P0ADV9|1*protein.P0ADV1|2*protein.P0A9V1|1*protein.P0AF98
