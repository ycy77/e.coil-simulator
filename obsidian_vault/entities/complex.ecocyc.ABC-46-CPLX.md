---
entity_id: "complex.ecocyc.ABC-46-CPLX"
entity_type: "complex"
name: "galactofuranose ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-46-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# galactofuranose ABC transporter

`complex.ecocyc.ABC-46-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-46-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P37772|protein.P37772]], [[protein.Q6BEX0|protein.Q6BEX0]], [[protein.P39328|protein.P39328]], [[protein.P39325|protein.P39325]]

## Enriched Summary

YtfQRT/YjfF is a galactofuranose transporter that is a member of the ATP-Binding Cassette (ABC) superfamily of transporters. Sequence analysis predicts thats YtfT and YjfF, YtfR (YtfRS), and YtfQ are the membrane components, ATP-binding protein and periplasmic binding protein respectively, of an ABC transporter in E. coli K-12 . Purified YtfQ binds galactose and exhibits selective binding of galactofuranose over galactopyranose . YtfQRT/YjfF is a galactofuranose transporter that is a member of the ATP-Binding Cassette (ABC) superfamily of transporters. Sequence analysis predicts thats YtfT and YjfF, YtfR (YtfRS), and YtfQ are the membrane components, ATP-binding protein and periplasmic binding protein respectively, of an ABC transporter in E. coli K-12 . Purified YtfQ binds galactose and exhibits selective binding of galactofuranose over galactopyranose .

## Biological Role

Catalyzes TRANS-RXN0-491 (reaction.ecocyc.TRANS-RXN0-491), TRANS-RXN0-492 (reaction.ecocyc.TRANS-RXN0-492). Transports hν (molecule.ecocyc.Light).

## Annotation

YtfQRT/YjfF is a galactofuranose transporter that is a member of the ATP-Binding Cassette (ABC) superfamily of transporters. Sequence analysis predicts thats YtfT and YjfF, YtfR (YtfRS), and YtfQ are the membrane components, ATP-binding protein and periplasmic binding protein respectively, of an ABC transporter in E. coli K-12 . Purified YtfQ binds galactose and exhibits selective binding of galactofuranose over galactopyranose .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-491|reaction.ecocyc.TRANS-RXN0-491]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-492|reaction.ecocyc.TRANS-RXN0-492]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P37772|protein.P37772]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P39325|protein.P39325]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P39328|protein.P39328]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.Q6BEX0|protein.Q6BEX0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-46-CPLX`
- `QSPROTEOME:QS00049324`

## Notes

1*protein.P37772|1*protein.Q6BEX0|1*protein.P39328|1*protein.P39325
