---
entity_id: "complex.ecocyc.ABC-20-CPLX"
entity_type: "complex"
name: "Ni(2+) ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-20-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "nickel ABC transporter"
---

# Ni(2+) ABC transporter

`complex.ecocyc.ABC-20-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-20-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P33593|protein.P33593]], [[protein.P33594|protein.P33594]], [[protein.P33591|protein.P33591]], [[protein.P0AFA9|protein.P0AFA9]], [[protein.P33590|protein.P33590]]

## Enriched Summary

The multicistronic nik operon (nikABCDE) encodes the components of a high affinity nickel uptake system that is a member of the ATP-binding cassette (ABC) superfamily of transporters. Ni2+ is an essential cofactor of the E. coli hydrogenases (CPLX0-8167 "hydrogenase 1", FORMHYDROG2-CPLX, HYDROG3-CPLX and possibly CPLX0-250). Early studies characterized hydC mutants in which a defective hydrogenase phenotype is suppressed by high concentrations of Ni2+ in the growth media . The species transported by NikABCDE may be a CPD0-2714 Ni-(L-His)2 complex . Sequence analysis suggests that NikA is the periplasmic binding protein, NikB and NikC are the inner membrane components, and NikD and NikE are the ATP-binding components of the transporter complex; cells with transposon insertions in the nikC, nikD or nikE genes lack hydrogenase activity and display considerably reduced rates of nickel transport [assayed with 150nM nickel chloride in the presence of 10mM Mg(II)] . The nik operon is expresssed under anaerobic conditions and is a member of the CPLX0-7797 "FNR" regulon ; nikABCDE expression is repressed when nickel is replete, mediated by the nickel reponsive repressor, NikR...

## Biological Role

Catalyzes ABC-20-RXN (reaction.ecocyc.ABC-20-RXN), TRANS-RXN0-630 (reaction.ecocyc.TRANS-RXN0-630). Transports Nickel(2+) (molecule.C19609), bis(L-histidinate)nickel(II) (molecule.ecocyc.CPD0-2714), hν (molecule.ecocyc.Light).

## Annotation

The multicistronic nik operon (nikABCDE) encodes the components of a high affinity nickel uptake system that is a member of the ATP-binding cassette (ABC) superfamily of transporters. Ni2+ is an essential cofactor of the E. coli hydrogenases (CPLX0-8167 "hydrogenase 1", FORMHYDROG2-CPLX, HYDROG3-CPLX and possibly CPLX0-250). Early studies characterized hydC mutants in which a defective hydrogenase phenotype is suppressed by high concentrations of Ni2+ in the growth media . The species transported by NikABCDE may be a CPD0-2714 Ni-(L-His)2 complex . Sequence analysis suggests that NikA is the periplasmic binding protein, NikB and NikC are the inner membrane components, and NikD and NikE are the ATP-binding components of the transporter complex; cells with transposon insertions in the nikC, nikD or nikE genes lack hydrogenase activity and display considerably reduced rates of nickel transport [assayed with 150nM nickel chloride in the presence of 10mM Mg(II)] . The nik operon is expresssed under anaerobic conditions and is a member of the CPLX0-7797 "FNR" regulon ; nikABCDE expression is repressed when nickel is replete, mediated by the nickel reponsive repressor, NikR . The nik operon is under complex transcriptional control; expression patterns are closely linked to hydrogenase expression levels; nitrate represses expression via the NarLX two-component system Review:

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ABC-20-RXN|reaction.ecocyc.ABC-20-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-630|reaction.ecocyc.TRANS-RXN0-630]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD0-2714|molecule.ecocyc.CPD0-2714]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[protein.P0AFA9|protein.P0AFA9]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P33590|protein.P33590]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P33591|protein.P33591]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P33593|protein.P33593]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P33594|protein.P33594]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-20-CPLX`
- `QSPROTEOME:QS00181295`

## Notes

1*protein.P33593|1*protein.P33594|1*protein.P33591|1*protein.P0AFA9|1*protein.P33590
