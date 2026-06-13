---
entity_id: "complex.ecocyc.ABC-32-CPLX"
entity_type: "complex"
name: "thiamine ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-32-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# thiamine ABC transporter

`complex.ecocyc.ABC-32-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-32-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31548|protein.P31548]], [[protein.P31549|protein.P31549]], [[protein.P31550|protein.P31550]]

## Enriched Summary

The ThiB, ThiP and ThiQ proteins are suggested to constitute an ATP-dependent thiamine uptake system in E. coli K-12; ThiB is the periplasmic thiamine binding protein , ThiP is the predicted inner membrane permease and ThiQ is the predicted energy transducing ATPase of the transporter complex . Thiamine uptake, studied in E. coli K-12 and in E. coli W, is a carrier-mediated, active process . An orthologous system in Salmonella typhimurium (ThiBPQ) is responsible for the uptake of both thiamine and thiamine pyrophosphate (TPP); there is also some evidence in E. coli for the transport of thiamine phosphate (see ). ThiBPQ is a member of the ATP-binding cassette (ABC) superfamily of transporters. The complex stoichiometry depicted (ThiQ2ThiP2ThiB) reflects an archetypal ABC transporter. The ThiB, ThiP and ThiQ proteins are suggested to constitute an ATP-dependent thiamine uptake system in E. coli K-12; ThiB is the periplasmic thiamine binding protein , ThiP is the predicted inner membrane permease and ThiQ is the predicted energy transducing ATPase of the transporter complex . Thiamine uptake, studied in E. coli K-12 and in E. coli W, is a carrier-mediated, active process . An orthologous system in Salmonella typhimurium (ThiBPQ) is responsible for the uptake of both thiamine and thiamine pyrophosphate (TPP); there is also some evidence in E...

## Biological Role

Catalyzes ABC-32-RXN (reaction.ecocyc.ABC-32-RXN). Transports Thiamine (molecule.C00378), hν (molecule.ecocyc.Light).

## Annotation

The ThiB, ThiP and ThiQ proteins are suggested to constitute an ATP-dependent thiamine uptake system in E. coli K-12; ThiB is the periplasmic thiamine binding protein , ThiP is the predicted inner membrane permease and ThiQ is the predicted energy transducing ATPase of the transporter complex . Thiamine uptake, studied in E. coli K-12 and in E. coli W, is a carrier-mediated, active process . An orthologous system in Salmonella typhimurium (ThiBPQ) is responsible for the uptake of both thiamine and thiamine pyrophosphate (TPP); there is also some evidence in E. coli for the transport of thiamine phosphate (see ). ThiBPQ is a member of the ATP-binding cassette (ABC) superfamily of transporters. The complex stoichiometry depicted (ThiQ2ThiP2ThiB) reflects an archetypal ABC transporter.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-32-RXN|reaction.ecocyc.ABC-32-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00378|molecule.C00378]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P31548|protein.P31548]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P31549|protein.P31549]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P31550|protein.P31550]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-32-CPLX`
- `QSPROTEOME:QS00049316`

## Notes

2*protein.P31548|2*protein.P31549|1*protein.P31550
