---
entity_id: "complex.ecocyc.ABC-57-CPLX"
entity_type: "complex"
name: "ABC exporter YbhFSR"
source_database: "EcoCyc"
source_id: "ABC-57-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ABC exporter YbhFSR

`complex.ecocyc.ABC-57-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-57-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AFQ2|protein.P0AFQ2]], [[protein.P0AFP9|protein.P0AFP9]], [[protein.P0A9U1|protein.P0A9U1]]

## Enriched Summary

Sequence analysis suggests that ybhF, ybhS and ybhR encode the subunits of an ATP-binding cassette (ABC) transporter complex; YbhF is the predicted ATP binding component, YbhS and YbhR are the predicted membrane components . ΔybhF mutants show reduced growth in the presence of the third generation cephalosporin - cefoperazone - suggesting that YbhFSR can function as a drug exporter . Whole cell efflux assays implicate YbhFSR in the efflux of tetracycline drugs and the cationic compounds ethidium bromide and Hoechst33342; YbhFSR may also function as a Na+ / (Li+):proton antiporter ybhF, ybhS and ybhR form an operon with ybhG (encoding a putative membrance fusion protein) and cecR (a transcriptional regulator); transcription of cecR-ybhGFSR is negatively regulated by EG12406-MONOMER "CecR" . In the Transporter Classification Database YbhGFSR is annotated as a 4-component system within the ATP-binding Cassette (ABC) superfamily . Sequence analysis suggests that ybhF, ybhS and ybhR encode the subunits of an ATP-binding cassette (ABC) transporter complex; YbhF is the predicted ATP binding component, YbhS and YbhR are the predicted membrane components . ΔybhF mutants show reduced growth in the presence of the third generation cephalosporin - cefoperazone - suggesting that YbhFSR can function as a drug exporter...

## Biological Role

Catalyzes TRANS-RXN-366 (reaction.ecocyc.TRANS-RXN-366). Transports cefoperazone (molecule.ecocyc.CPD-19953), hν (molecule.ecocyc.Light).

## Annotation

Sequence analysis suggests that ybhF, ybhS and ybhR encode the subunits of an ATP-binding cassette (ABC) transporter complex; YbhF is the predicted ATP binding component, YbhS and YbhR are the predicted membrane components . ΔybhF mutants show reduced growth in the presence of the third generation cephalosporin - cefoperazone - suggesting that YbhFSR can function as a drug exporter . Whole cell efflux assays implicate YbhFSR in the efflux of tetracycline drugs and the cationic compounds ethidium bromide and Hoechst33342; YbhFSR may also function as a Na+ / (Li+):proton antiporter ybhF, ybhS and ybhR form an operon with ybhG (encoding a putative membrance fusion protein) and cecR (a transcriptional regulator); transcription of cecR-ybhGFSR is negatively regulated by EG12406-MONOMER "CecR" . In the Transporter Classification Database YbhGFSR is annotated as a 4-component system within the ATP-binding Cassette (ABC) superfamily .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-366|reaction.ecocyc.TRANS-RXN-366]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-19953|molecule.ecocyc.CPD-19953]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0A9U1|protein.P0A9U1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AFP9|protein.P0AFP9]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AFQ2|protein.P0AFQ2]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-57-CPLX`
- `QSPROTEOME:QS00049332`

## Notes

1*protein.P0AFQ2|1*protein.P0AFP9|1*protein.P0A9U1
