---
entity_id: "complex.ecocyc.ABC-63-CPLX"
entity_type: "complex"
name: "Zn2+ ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-63-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Zn2+ ABC transporter

`complex.ecocyc.ABC-63-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-63-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9X1|protein.P0A9X1]], [[protein.P39832|protein.P39832]], [[protein.P39172|protein.P39172]]

## Enriched Summary

ZnuABC is a high-affinity zinc uptake system that is a member of the ATP Binding Cassette (ABC) Superfamily of transporters. Characterization of znuA::MudX and znuB::MudX insertion mutants implicates both genes in the high-affinity uptake of Zn2+ ; znuA encodes a periplasmic Zn2+ binding protein while znuB and znuC encode the predicted integral membrane subunit and ATP-binding subunit respectively of a binding protein dependent transport system . znuABC on a low-copy plasmid complements the growth defect of znuA::MudX and znuB::MudX insertion mutants on TY plates containing EDTA and restores transport of labeled Zn2+ in uptake studies . znuA and znuBC are transcribed divergently . Expression is regulated by the transcriptional repressor Zur in response to the intracellular zinc concentration . The complex stoichiometry depicted (ZnuC2ZnuB2ZnuA) is based on an archetypal ABC transporter. znu: Zn2+ uptake ZnuABC is a high-affinity zinc uptake system that is a member of the ATP Binding Cassette (ABC) Superfamily of transporters. Characterization of znuA::MudX and znuB::MudX insertion mutants implicates both genes in the high-affinity uptake of Zn2+ ; znuA encodes a periplasmic Zn2+ binding protein while znuB and znuC encode the predicted integral membrane subunit and ATP-binding subunit respectively of a binding protein dependent transport system...

## Biological Role

Catalyzes ABC-63-RXN (reaction.ecocyc.ABC-63-RXN). Transports Zinc cation (molecule.C00038), hν (molecule.ecocyc.Light).

## Annotation

ZnuABC is a high-affinity zinc uptake system that is a member of the ATP Binding Cassette (ABC) Superfamily of transporters. Characterization of znuA::MudX and znuB::MudX insertion mutants implicates both genes in the high-affinity uptake of Zn2+ ; znuA encodes a periplasmic Zn2+ binding protein while znuB and znuC encode the predicted integral membrane subunit and ATP-binding subunit respectively of a binding protein dependent transport system . znuABC on a low-copy plasmid complements the growth defect of znuA::MudX and znuB::MudX insertion mutants on TY plates containing EDTA and restores transport of labeled Zn2+ in uptake studies . znuA and znuBC are transcribed divergently . Expression is regulated by the transcriptional repressor Zur in response to the intracellular zinc concentration . The complex stoichiometry depicted (ZnuC2ZnuB2ZnuA) is based on an archetypal ABC transporter. znu: Zn2+ uptake

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-63-RXN|reaction.ecocyc.ABC-63-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0A9X1|protein.P0A9X1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P39172|protein.P39172]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P39832|protein.P39832]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-63-CPLX`
- `QSPROTEOME:QS00049338`

## Notes

2*protein.P0A9X1|2*protein.P39832|1*protein.P39172
