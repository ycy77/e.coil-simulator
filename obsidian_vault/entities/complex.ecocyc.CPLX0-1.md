---
entity_id: "complex.ecocyc.CPLX0-1"
entity_type: "complex"
name: "reduced flavorubredoxin"
source_database: "EcoCyc"
source_id: "CPLX0-1"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "FlRd"
---

# reduced flavorubredoxin

`complex.ecocyc.CPLX0-1`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.Q46877|protein.Q46877]]

## Enriched Summary

The NorV/EG12450-MONOMER NorW system constitutes a nitric oxide reductase that couples NADH oxidation to NO reduction . The electron transfer chain begins with NADH oxidation by NorW, which then transfers the electron to the rubredoxin domain of NorV. Electrons travel through the protein to the catalytic di-iron site, where they are used for reduction of NO to N2O. NorV (flavorubredoxin, FlRd), a class B flavodiiron protein, is a multidomain protein containing an amino-terminal β-lactamase-like module with a non-heme di-iron site as the catalytic center, a short chain flavodoxin-like module and a rubredoxin (Rd)-like extension . A low-resolution structure was obtained by small-angle X-ray scattering, showing that the rubredoxin domain behaves as an independent domain . Crystal structures of oxidized and reduced NorV and a solution structure of the isolated Rd domain have been solved. The C-terminal Rd domain, although present in the purified protein, was not detected in the crystal structures, indicating disordered localization. Due to the head-to-tail dimerization of NorV subunits, the diiron site of one monomer is positioned close to the FMN of the second monomer . The redox properties of NorV have been characterized , and the kinetics of electron transfer from NADH via NorW and NorV to NO has been measured...

## Biological Role

Catalyzes RXN0-2721 (reaction.ecocyc.RXN0-2721).

## Annotation

The NorV/EG12450-MONOMER NorW system constitutes a nitric oxide reductase that couples NADH oxidation to NO reduction . The electron transfer chain begins with NADH oxidation by NorW, which then transfers the electron to the rubredoxin domain of NorV. Electrons travel through the protein to the catalytic di-iron site, where they are used for reduction of NO to N2O. NorV (flavorubredoxin, FlRd), a class B flavodiiron protein, is a multidomain protein containing an amino-terminal β-lactamase-like module with a non-heme di-iron site as the catalytic center, a short chain flavodoxin-like module and a rubredoxin (Rd)-like extension . A low-resolution structure was obtained by small-angle X-ray scattering, showing that the rubredoxin domain behaves as an independent domain . Crystal structures of oxidized and reduced NorV and a solution structure of the isolated Rd domain have been solved. The C-terminal Rd domain, although present in the purified protein, was not detected in the crystal structures, indicating disordered localization. Due to the head-to-tail dimerization of NorV subunits, the diiron site of one monomer is positioned close to the FMN of the second monomer . The redox properties of NorV have been characterized , and the kinetics of electron transfer from NADH via NorW and NorV to NO has been measured . The non-heme metal binding site of FlRd contains an atypical glutamate residue that is able to accomodate a zinc ion instead of iron . Nitric oxide has been shown to have diverse biologial functions; however, the molecule also inactivates essential cellular enzymes. It is therefore essential that NO is removed from the cell. A kinetic model of the fate of NO within E. coli has been constructed and tested. EG10456-MONOMER Hmp appears to be the major NO sink both a

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2721|reaction.ecocyc.RXN0-2721]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.Q46877|protein.Q46877]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-1`
- `QSPROTEOME:QS00183155`

## Notes

4*protein.Q46877
