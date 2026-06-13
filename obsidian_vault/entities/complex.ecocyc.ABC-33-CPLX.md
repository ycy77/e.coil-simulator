---
entity_id: "complex.ecocyc.ABC-33-CPLX"
entity_type: "complex"
name: "xylose ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-33-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "XylFGH"
---

# xylose ABC transporter

`complex.ecocyc.ABC-33-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-33-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P37388|protein.P37388]], [[protein.P0AGI4|protein.P0AGI4]], [[protein.P37387|protein.P37387]]

## Enriched Summary

XylFGH is a high-affinity D-xylose uptake system belonging to the ATP Binding Cassette (ABC) Superfamily of transporters. XylF is the periplasmic binding protein , XylG is the predicted ATP-binding subunit and XylH is the predicted integral membrane component of the transporter complex . Transcription of xylFGH is regulated by EG20253-MONOMER "XylR and CRP; its expression is induced by xylose in the absence of glucose . An inhibitory effect on xylFGH induced by xylose appeared in the presence of a higher concentration of arabinose . D-xylose - a pentose sugar that is abundant in plant biomass - can be utilized by E. coli as a sole carbon and energy source source and is metabolized through the pentose phosphate pathway (see XYLCAT-PWY). Early studies identified two uptake systems for D-xylose in E. coli (see and the references within) - now known to be the high-affinity ATP-dependent system described above and the relatively low-affinity XYLE-MONOMER, XylE . The complex stoichiometry depicted (XylGXylH2XylF) is based on an archetypal ABC transporter. XylFGH is a high-affinity D-xylose uptake system belonging to the ATP Binding Cassette (ABC) Superfamily of transporters. XylF is the periplasmic binding protein , XylG is the predicted ATP-binding subunit and XylH is the predicted integral membrane component of the transporter complex...

## Biological Role

Catalyzes xylose ABC transporter (reaction.ecocyc.ABC-33-RXN). Transports D-Xylose (molecule.C00181), hν (molecule.ecocyc.Light).

## Annotation

XylFGH is a high-affinity D-xylose uptake system belonging to the ATP Binding Cassette (ABC) Superfamily of transporters. XylF is the periplasmic binding protein , XylG is the predicted ATP-binding subunit and XylH is the predicted integral membrane component of the transporter complex . Transcription of xylFGH is regulated by EG20253-MONOMER "XylR and CRP; its expression is induced by xylose in the absence of glucose . An inhibitory effect on xylFGH induced by xylose appeared in the presence of a higher concentration of arabinose . D-xylose - a pentose sugar that is abundant in plant biomass - can be utilized by E. coli as a sole carbon and energy source source and is metabolized through the pentose phosphate pathway (see XYLCAT-PWY). Early studies identified two uptake systems for D-xylose in E. coli (see and the references within) - now known to be the high-affinity ATP-dependent system described above and the relatively low-affinity XYLE-MONOMER, XylE . The complex stoichiometry depicted (XylGXylH2XylF) is based on an archetypal ABC transporter.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-33-RXN|reaction.ecocyc.ABC-33-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00181|molecule.C00181]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AGI4|protein.P0AGI4]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P37387|protein.P37387]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P37388|protein.P37388]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-33-CPLX`
- `QSPROTEOME:QS00049317`

## Notes

1*protein.P37388|2*protein.P0AGI4|1*protein.P37387
