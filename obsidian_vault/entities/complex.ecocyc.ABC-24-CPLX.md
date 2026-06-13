---
entity_id: "complex.ecocyc.ABC-24-CPLX"
entity_type: "complex"
name: "spermidine preferential ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-24-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# spermidine preferential ABC transporter

`complex.ecocyc.ABC-24-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-24-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69874|protein.P69874]], [[protein.P0AFK4|protein.P0AFK4]], [[protein.P0AFK6|protein.P0AFK6]], [[protein.P0AFK9|protein.P0AFK9]]

## Enriched Summary

PotABCD is an ATP-dependent polyamine uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters; PotABCD transports both spermidine and putrescine but is considered to be spermidine-preferential. The transporter consists of a membrane associated ATPase (PotA), two transmembrane proteins (PotB and PotC), and a periplasmic substrate-binding protein (PotD) . Transport assays in a proton-translocating ATPase mutant indicate that ATP is essential for spermidine uptake and membrane potential is also involved . potABCD consititute an operon . Transcription of potABCD appears to be inhibited by prePotD; two PotD binding sites, located upstream and downstream of the potA initiation codon, have been identified . Reviews: PotABCD is an ATP-dependent polyamine uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters; PotABCD transports both spermidine and putrescine but is considered to be spermidine-preferential. The transporter consists of a membrane associated ATPase (PotA), two transmembrane proteins (PotB and PotC), and a periplasmic substrate-binding protein (PotD) . Transport assays in a proton-translocating ATPase mutant indicate that ATP is essential for spermidine uptake and membrane potential is also involved . potABCD consititute an operon...

## Biological Role

Catalyzes ABC-24-RXN (reaction.ecocyc.ABC-24-RXN), ABC-25-RXN (reaction.ecocyc.ABC-25-RXN). Transports Putrescine (molecule.C00134), Spermidine (molecule.C00315), hν (molecule.ecocyc.Light).

## Annotation

PotABCD is an ATP-dependent polyamine uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters; PotABCD transports both spermidine and putrescine but is considered to be spermidine-preferential. The transporter consists of a membrane associated ATPase (PotA), two transmembrane proteins (PotB and PotC), and a periplasmic substrate-binding protein (PotD) . Transport assays in a proton-translocating ATPase mutant indicate that ATP is essential for spermidine uptake and membrane potential is also involved . potABCD consititute an operon . Transcription of potABCD appears to be inhibited by prePotD; two PotD binding sites, located upstream and downstream of the potA initiation codon, have been identified . Reviews:

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ABC-24-RXN|reaction.ecocyc.ABC-24-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ABC-25-RXN|reaction.ecocyc.ABC-25-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AFK4|protein.P0AFK4]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AFK6|protein.P0AFK6]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AFK9|protein.P0AFK9]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69874|protein.P69874]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-24-CPLX`
- `QSPROTEOME:QS00192595`

## Notes

2*protein.P69874|1*protein.P0AFK4|1*protein.P0AFK6|1*protein.P0AFK9
