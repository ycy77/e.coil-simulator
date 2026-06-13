---
entity_id: "complex.ecocyc.ABC-29-CPLX"
entity_type: "complex"
name: "putative antimicrobial peptide ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-29-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putative antimicrobial peptide ABC transporter

`complex.ecocyc.ABC-29-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-29-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AAH8|protein.P0AAH8]], [[protein.P0AGH5|protein.P0AGH5]], [[protein.P0AGH3|protein.P0AGH3]], [[protein.P0AAH4|protein.P0AAH4]], [[protein.Q47622|protein.Q47622]]

## Enriched Summary

The 5-cistron sap operon encodes the transmembrane (SapBC), ATP-binding (SapDF) and substrate-binding (SapA) components of an ATP-binding cassette (ABC)-family transporter complex. 'Sap family' transporters are widely present in Gram-negative pathogens where they contribute to resistance against antimicrobial peptides (AMPs) (see ). E. coli K-12 contains a 'consensus' sap operon (sapABCDF) encoding all five Sap components in tandem ; the complex may be involved in the uptake of a range of molecules, such as AMPs, dipeptides and heme . Separately, a CPLX0-13226 SapBCDF complex has been implicated in putrescine efflux at neutral pH . First characterized in the facultative intracellular bacteria TAX-90371, sap mutants are sensitive to antimicrobial peptides . Bacterial peptide transporters, including the sap-encoded ABC transporter, are targets for the development of novel peptide-based antibiotics . The 5-cistron sap operon encodes the transmembrane (SapBC), ATP-binding (SapDF) and substrate-binding (SapA) components of an ATP-binding cassette (ABC)-family transporter complex. 'Sap family' transporters are widely present in Gram-negative pathogens where they contribute to resistance against antimicrobial peptides (AMPs) (see ). E...

## Biological Role

Catalyzes TRANS-RXN-1594 (reaction.ecocyc.TRANS-RXN-1594). Transports an antimicrobial peptide (molecule.ecocyc.Antimicrobial-Peptides), hν (molecule.ecocyc.Light).

## Annotation

The 5-cistron sap operon encodes the transmembrane (SapBC), ATP-binding (SapDF) and substrate-binding (SapA) components of an ATP-binding cassette (ABC)-family transporter complex. 'Sap family' transporters are widely present in Gram-negative pathogens where they contribute to resistance against antimicrobial peptides (AMPs) (see ). E. coli K-12 contains a 'consensus' sap operon (sapABCDF) encoding all five Sap components in tandem ; the complex may be involved in the uptake of a range of molecules, such as AMPs, dipeptides and heme . Separately, a CPLX0-13226 SapBCDF complex has been implicated in putrescine efflux at neutral pH . First characterized in the facultative intracellular bacteria TAX-90371, sap mutants are sensitive to antimicrobial peptides . Bacterial peptide transporters, including the sap-encoded ABC transporter, are targets for the development of novel peptide-based antibiotics .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1594|reaction.ecocyc.TRANS-RXN-1594]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Antimicrobial-Peptides|molecule.ecocyc.Antimicrobial-Peptides]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[protein.P0AAH4|protein.P0AAH4]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AAH8|protein.P0AAH8]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AGH3|protein.P0AGH3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AGH5|protein.P0AGH5]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.Q47622|protein.Q47622]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-29-CPLX`
- `QSPROTEOME:QS00174441`

## Notes

1*protein.P0AAH8|1*protein.P0AGH5|1*protein.P0AGH3|1*protein.P0AAH4|protein.Q47622
