---
entity_id: "complex.ecocyc.ABC-26-CPLX"
entity_type: "complex"
name: "glycine betaine ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-26-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PPIII"
  - "proline permease III"
  - "ProVWX"
---

# glycine betaine ABC transporter

`complex.ecocyc.ABC-26-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-26-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P14175|protein.P14175]], [[protein.P14176|protein.P14176]], [[protein.P0AFM2|protein.P0AFM2]]

## Enriched Summary

ProVWX, the high-affinity transport system for the osmoprotectant glycine betaine, is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. Early experiments characterized the osrA/proU operon as an osmoresponsive, high affinity, binding protein dependent uptake system for glycine betaine and to a lesser extent, proline . The proU operon consists of three genes: proV predicted to encode the ATP-binding subunit, proW predicted to encode the integral membrane subunit and proX encoding the experimentally characterized, periplasmic binding protein of the transport system . ATP is consumed during ProU mediated glycine betaine uptake at an initial stoichiometry of 1.8 molecules of ATP per molecule of substrate transported (declining to 1 as the assay proceeds) . Purified ProX binds glycine betaine (Kd of 1μM) and proline betaine (estimated Kd of 5.2μM) with high affinity indicating that the ProVWX system is well suited to scavenge glycine betaine and proline betaine from the environment. Other osmoprotectants (e.g. proline, taurine, ectoine and carnitine) can also be transported by the ProVWX transporter at lower affinities (see review by ) as can the betaine precursor, choline...

## Biological Role

Catalyzes ABC-26-RXN (reaction.ecocyc.ABC-26-RXN), RXN-8638 (reaction.ecocyc.RXN-8638). Transports L-Proline (molecule.C00148), hν (molecule.ecocyc.Light), a quaternary ammonium compound (molecule.ecocyc.Quaternary-Amines).

## Annotation

ProVWX, the high-affinity transport system for the osmoprotectant glycine betaine, is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. Early experiments characterized the osrA/proU operon as an osmoresponsive, high affinity, binding protein dependent uptake system for glycine betaine and to a lesser extent, proline . The proU operon consists of three genes: proV predicted to encode the ATP-binding subunit, proW predicted to encode the integral membrane subunit and proX encoding the experimentally characterized, periplasmic binding protein of the transport system . ATP is consumed during ProU mediated glycine betaine uptake at an initial stoichiometry of 1.8 molecules of ATP per molecule of substrate transported (declining to 1 as the assay proceeds) . Purified ProX binds glycine betaine (Kd of 1μM) and proline betaine (estimated Kd of 5.2μM) with high affinity indicating that the ProVWX system is well suited to scavenge glycine betaine and proline betaine from the environment. Other osmoprotectants (e.g. proline, taurine, ectoine and carnitine) can also be transported by the ProVWX transporter at lower affinities (see review by ) as can the betaine precursor, choline . proVWX expression increases with an increase in the osmolarity of the growth medium ; expression of a proU-lac fusion increases when NaCl (300mM) or sucrose (464mM) is added to the growth medium; expression is reduced in the presence of 1mM glycine betaine plus 300mM NaCl . High osmolarity also stimulates the activity of transporter . ProVWX, reconstituted in liposomes, transports glycine betaine in an ATP dependent manner; the rate of transport is stimulated when the external salt concentration is increased and activity is dependent on the fraction of anionic lipids in the reconsti

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ABC-26-RXN|reaction.ecocyc.ABC-26-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-8638|reaction.ecocyc.RXN-8638]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Quaternary-Amines|molecule.ecocyc.Quaternary-Amines]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AFM2|protein.P0AFM2]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P14175|protein.P14175]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P14176|protein.P14176]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:ABC-26-CPLX`
- `QSPROTEOME:QS00195509`

## Notes

2*protein.P14175|2*protein.P14176|1*protein.P0AFM2
