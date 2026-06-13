---
entity_id: "complex.ecocyc.CPLX0-2161"
entity_type: "complex"
name: "tripartite efflux pump EmrKY-TolC"
source_database: "EcoCyc"
source_id: "CPLX0-2161"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tripartite efflux pump EmrKY-TolC

`complex.ecocyc.CPLX0-2161`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2161`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]], [[protein.P52599|protein.P52599]], [[protein.P52600|protein.P52600]]

## Enriched Summary

EmrKY-TolC is a putative tripartite efflux pump complex in E. coli K-12. EmrK and EmrY are homologous to the efflux pump proteins, EG11354-MONOMER "EmrA" and EMRB-MONOMER "EmrB" respectively; EmrKY is implicated in tetracycline efflux . Expression of emrKY is regulated by the PWY0-1490 "EvgSA two-component system"; constitutive expression of emrKY (due to mutations in EvgS) in the K-12 strain MC4100 results in increased resistance to deoxycholate (see also . EmrKY requires TolC for efflux function . Deletion of emrKY in the K-12 strain W3110 does not affect susceptibility to a range of 35 compounds (dyes, detergents, antibiotics and others) . Overexpression of emrKY in the K-12 strain KAM3 which lacks AcrB (see ) does not affect resistance to a range of β-lactams . EmrKY-TolC is implicated in maintaining antibiotic tolerance under starvation; expression of the pump is upregulated during nutrient starvation and the starvation-induced ampicillin tolerance level of emrK and emrY single knockout strains is significantly reduced over both a 6 and 30 day period . EmrKY-TolC is a putative tripartite efflux pump complex in E. coli K-12. EmrK and EmrY are homologous to the efflux pump proteins, EG11354-MONOMER "EmrA" and EMRB-MONOMER "EmrB" respectively; EmrKY is implicated in tetracycline efflux...

## Biological Role

Catalyzes deoxycholate export (reaction.ecocyc.TRANS-RXN-365). Transports Deoxycholic acid (molecule.C04483), hν (molecule.ecocyc.Light).

## Annotation

EmrKY-TolC is a putative tripartite efflux pump complex in E. coli K-12. EmrK and EmrY are homologous to the efflux pump proteins, EG11354-MONOMER "EmrA" and EMRB-MONOMER "EmrB" respectively; EmrKY is implicated in tetracycline efflux . Expression of emrKY is regulated by the PWY0-1490 "EvgSA two-component system"; constitutive expression of emrKY (due to mutations in EvgS) in the K-12 strain MC4100 results in increased resistance to deoxycholate (see also . EmrKY requires TolC for efflux function . Deletion of emrKY in the K-12 strain W3110 does not affect susceptibility to a range of 35 compounds (dyes, detergents, antibiotics and others) . Overexpression of emrKY in the K-12 strain KAM3 which lacks AcrB (see ) does not affect resistance to a range of β-lactams . EmrKY-TolC is implicated in maintaining antibiotic tolerance under starvation; expression of the pump is upregulated during nutrient starvation and the starvation-induced ampicillin tolerance level of emrK and emrY single knockout strains is significantly reduced over both a 6 and 30 day period .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-365|reaction.ecocyc.TRANS-RXN-365]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P02930|protein.P02930]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P52599|protein.P52599]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P52600|protein.P52600]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-2161`
- `QSPROTEOME:QS00185195`

## Notes

complex.ecocyc.CPLX0-7964|protein.P52599|protein.P52600
