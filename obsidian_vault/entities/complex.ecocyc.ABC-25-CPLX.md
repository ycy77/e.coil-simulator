---
entity_id: "complex.ecocyc.ABC-25-CPLX"
entity_type: "complex"
name: "putrescine ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-25-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putrescine ABC transporter

`complex.ecocyc.ABC-25-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-25-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31134|protein.P31134]], [[protein.P31135|protein.P31135]], [[protein.P0AFL1|protein.P0AFL1]], [[protein.P31133|protein.P31133]]

## Enriched Summary

PotFGHI is an ATP-dependent, high affinity putrescine uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. PotG is the predicted ATP-binding subunit, PotH and PotI are the integral membrane subunits, and PotF is the periplasmic, putrescine binding protein of the transporter complex; expression of all four proteins from a plasmid is necessary for restoring putrescine transport in a polyamine-requiring strain that lacks both ATP-dependent polyamine transporters PotABCD and PotFGHI . The PotFGHI transporter is primarily responsible for importing putrescine necessary for cell growth in the presence of glucose whereas the putrescine symporter, PuuP, is required when putrescine is utilised as an energy source in the absence of glucose . PotFGHI enhances cell growth more effectively than B1296-MONOMER "PuuP" in media containing 0.4% glucose and 10mM putrescine; gradual inhibition of PotFGHI mediated putrescine transport occurs as the intracellular level of putrescine increases . In addition to PotFGHI, B1296-MONOMER "PuuP" and the spermidine preferential ABC transporter (ABC-24-CPLX "PotABCD"), E. coli K-12 may contain a fourth putrescine uptake system . Reviews: PotFGHI is an ATP-dependent, high affinity putrescine uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters...

## Biological Role

Catalyzes ABC-25-RXN (reaction.ecocyc.ABC-25-RXN).

## Annotation

PotFGHI is an ATP-dependent, high affinity putrescine uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. PotG is the predicted ATP-binding subunit, PotH and PotI are the integral membrane subunits, and PotF is the periplasmic, putrescine binding protein of the transporter complex; expression of all four proteins from a plasmid is necessary for restoring putrescine transport in a polyamine-requiring strain that lacks both ATP-dependent polyamine transporters PotABCD and PotFGHI . The PotFGHI transporter is primarily responsible for importing putrescine necessary for cell growth in the presence of glucose whereas the putrescine symporter, PuuP, is required when putrescine is utilised as an energy source in the absence of glucose . PotFGHI enhances cell growth more effectively than B1296-MONOMER "PuuP" in media containing 0.4% glucose and 10mM putrescine; gradual inhibition of PotFGHI mediated putrescine transport occurs as the intracellular level of putrescine increases . In addition to PotFGHI, B1296-MONOMER "PuuP" and the spermidine preferential ABC transporter (ABC-24-CPLX "PotABCD"), E. coli K-12 may contain a fourth putrescine uptake system . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ABC-25-RXN|reaction.ecocyc.ABC-25-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AFL1|protein.P0AFL1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P31133|protein.P31133]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P31134|protein.P31134]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P31135|protein.P31135]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:ABC-25-CPLX`
- `QSPROTEOME:QS00177209`

## Notes

2*protein.P31134|1*protein.P31135|1*protein.P0AFL1|1*protein.P31133
