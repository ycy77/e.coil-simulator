---
entity_id: "complex.ecocyc.CPLX0-13226"
entity_type: "complex"
name: "putative putrescine ABC exporter"
source_database: "EcoCyc"
source_id: "CPLX0-13226"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putative putrescine ABC exporter

`complex.ecocyc.CPLX0-13226`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-13226`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AAH8|protein.P0AAH8]], [[protein.P0AAH4|protein.P0AAH4]], [[protein.P0AGH5|protein.P0AGH5]], [[protein.P0AGH3|protein.P0AGH3]]

## Enriched Summary

SapBCDF has been implicated in putrescine efflux at neutral pH . The concentration of putrescine in the culture supernatant of the single deletion strains ΔsapB, ΔsapC, ΔsapD and ΔsapF, is significantly reduced compared to wild type; the decrease in external putrescine concentration in a ΔsapBCDF strain is due to decreased export from the cell and can be complemented by expression of sapBCDF from a plasmid; labeled putrescine (metabolized from labeled intracellular arginine) is exported to the extracellular environment by SapBCDF . Separately, SapBCDF together with the substrate-binding protein SAPA-MONOMER SapA, may be involved in the uptake of a range of molecules, such as antimicrobial peptides, dipeptides and heme . An E. coli ΔsapBCDF strain is as susceptible to the antimicrobial peptide, LL-37, as wild type . SapBCDF has been implicated in putrescine efflux at neutral pH . The concentration of putrescine in the culture supernatant of the single deletion strains ΔsapB, ΔsapC, ΔsapD and ΔsapF, is significantly reduced compared to wild type; the decrease in external putrescine concentration in a ΔsapBCDF strain is due to decreased export from the cell and can be complemented by expression of sapBCDF from a plasmid; labeled putrescine (metabolized from labeled intracellular arginine) is exported to the extracellular environment by SapBCDF...

## Biological Role

Catalyzes TRANS-RXN-328 (reaction.ecocyc.TRANS-RXN-328). Transports Putrescine (molecule.C00134), hν (molecule.ecocyc.Light).

## Annotation

SapBCDF has been implicated in putrescine efflux at neutral pH . The concentration of putrescine in the culture supernatant of the single deletion strains ΔsapB, ΔsapC, ΔsapD and ΔsapF, is significantly reduced compared to wild type; the decrease in external putrescine concentration in a ΔsapBCDF strain is due to decreased export from the cell and can be complemented by expression of sapBCDF from a plasmid; labeled putrescine (metabolized from labeled intracellular arginine) is exported to the extracellular environment by SapBCDF . Separately, SapBCDF together with the substrate-binding protein SAPA-MONOMER SapA, may be involved in the uptake of a range of molecules, such as antimicrobial peptides, dipeptides and heme . An E. coli ΔsapBCDF strain is as susceptible to the antimicrobial peptide, LL-37, as wild type .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-328|reaction.ecocyc.TRANS-RXN-328]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AAH4|protein.P0AAH4]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AAH8|protein.P0AAH8]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AGH3|protein.P0AGH3]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AGH5|protein.P0AGH5]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-13226`

## Notes

protein.P0AAH8|protein.P0AAH4|protein.P0AGH5|protein.P0AGH3
