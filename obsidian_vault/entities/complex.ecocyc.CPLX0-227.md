---
entity_id: "complex.ecocyc.CPLX0-227"
entity_type: "complex"
name: "α-ketoglutarate-dependent taurine dioxygenase"
source_database: "EcoCyc"
source_id: "CPLX0-227"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "sulfate starvation-induced protein 3"
  - "SSI3"
---

# α-ketoglutarate-dependent taurine dioxygenase

`complex.ecocyc.CPLX0-227`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-227`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37610|protein.P37610]]

## Enriched Summary

Taurine dioxygenase (TauD) is a non-heme iron oxidase that catalyzes the oxygenolytic release of SO3 from TAURINE. It requires 2-KETOGLUTARATE (α-ketoglutarate) and FE+2, and is stimulated by ASCORBATE. The enzyme catalyzes the conversion of taurine to sulfite and CPD-1772 while decomposing 2-oxoglutarate to SUC and CARBON-DIOXIDE. Hydroxylation of the unactivated C1 carbon of taurine produces an unstable intermediate that decomposes to the final products. TauD has become a prototypical representative for the Fe2α-ketoglutarate-dependent dioxygenase class ( and in ). TauD is expressed only under conditions of sulfate starvation (see pathway PWY0-981. Mutants in tauD lose the ability to use taurine as a sulfur source, but can utilize other aliphatic sulfonates . However tauD-independent taurine assimilation was observed in an E. coli K-12 ΔtauD mutant when ssuD was artificially expressed in the tauD ssuD double mutant . TauD was originally reported to be a homodimer based on gel filtration chromatography and SDS-PAGE , and on crystallographic data . However, TauD from both E. coli and Pseudomonas putida KT2440 were later concluded to be homotetramers in solution and in crystals, based on structural data, analytical gel filtration chromatography, and sedimentation velocity analytical ultracentrifugation studies . Each subunit of TauD binds a single Fe2+ molecule...

## Biological Role

Catalyzes RXN0-299 (reaction.ecocyc.RXN0-299). Bound by Fe2+ (molecule.C14818).

## Annotation

Taurine dioxygenase (TauD) is a non-heme iron oxidase that catalyzes the oxygenolytic release of SO3 from TAURINE. It requires 2-KETOGLUTARATE (α-ketoglutarate) and FE+2, and is stimulated by ASCORBATE. The enzyme catalyzes the conversion of taurine to sulfite and CPD-1772 while decomposing 2-oxoglutarate to SUC and CARBON-DIOXIDE. Hydroxylation of the unactivated C1 carbon of taurine produces an unstable intermediate that decomposes to the final products. TauD has become a prototypical representative for the Fe2α-ketoglutarate-dependent dioxygenase class ( and in ). TauD is expressed only under conditions of sulfate starvation (see pathway PWY0-981. Mutants in tauD lose the ability to use taurine as a sulfur source, but can utilize other aliphatic sulfonates . However tauD-independent taurine assimilation was observed in an E. coli K-12 ΔtauD mutant when ssuD was artificially expressed in the tauD ssuD double mutant . TauD was originally reported to be a homodimer based on gel filtration chromatography and SDS-PAGE , and on crystallographic data . However, TauD from both E. coli and Pseudomonas putida KT2440 were later concluded to be homotetramers in solution and in crystals, based on structural data, analytical gel filtration chromatography, and sedimentation velocity analytical ultracentrifugation studies . Each subunit of TauD binds a single Fe2+ molecule . Kinetic analysis of the reaction mechanism of the enzyme has been performed . Kinetic and spectroscopic methods were used to characterize an oxidized iron intermediate involved in hydrogen abstraction from the C1 carbon of taurine, the site of hydroxylation . A number of subsequent spectroscopic, kinetic, site-directed mutagenesis, and inhibitor studies dissected the complex catalytic mechanism of TauD . Computa

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-299|reaction.ecocyc.RXN0-299]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P37610|protein.P37610]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-227`
- `QSPROTEOME:QS00171375`

## Notes

4*protein.P37610
