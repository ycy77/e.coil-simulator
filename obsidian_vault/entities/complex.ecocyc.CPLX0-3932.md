---
entity_id: "complex.ecocyc.CPLX0-3932"
entity_type: "complex"
name: "multidrug efflux pump AcrAD-TolC"
source_database: "EcoCyc"
source_id: "CPLX0-3932"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# multidrug efflux pump AcrAD-TolC

`complex.ecocyc.CPLX0-3932`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3932`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]], [[protein.P24177|protein.P24177]], [[protein.P0AE06|protein.P0AE06]]

## Enriched Summary

In E. coli K-12, the resistance-nodulation-division (RND) family proteins AcrD and AcrB each function with the membrane fusion protein AcrA and a multifunctional outer membrane channel TolC to export a wide range of toxic exogenous compounds (antibiotics, dyes, detergents, bile compounds, organic solvents) and some endogenous metabolites (enterobactin, porphyrinogens/porphyrins). The well characterized AcrB system (TRANS-CPLX-201 "AcrAB-TolC") is the major contributor to intrinsic resistance for many compounds ; the AcrD system (AcrAD-TolC) exports Aminoglycoside-Antibiotics "aminoglycoside" antibiotics, although a broader substrate range can be seen upon AcrD over-production or in the absence of AcrB (for greater detail see ACRD-MONOMER "AcrD"). The AcrAD-TolC subunit stoichiometry shown here is inferred by analogy with the AcrAB-TolC complex. In E. coli K-12, the resistance-nodulation-division (RND) family proteins AcrD and AcrB each function with the membrane fusion protein AcrA and a multifunctional outer membrane channel TolC to export a wide range of toxic exogenous compounds (antibiotics, dyes, detergents, bile compounds, organic solvents) and some endogenous metabolites (enterobactin, porphyrinogens/porphyrins)...

## Biological Role

Catalyzes aminoglycoside export (reaction.ecocyc.TRANS-RXN-1551), aminoglycoside export (reaction.ecocyc.TRANS-RXN-1552), gentamicin export (reaction.ecocyc.TRANS-RXN-360). Transports an aminoglycoside (molecule.ecocyc.Aminoglycosides), a gentamicin (molecule.ecocyc.Gentamycins), hν (molecule.ecocyc.Light).

## Annotation

In E. coli K-12, the resistance-nodulation-division (RND) family proteins AcrD and AcrB each function with the membrane fusion protein AcrA and a multifunctional outer membrane channel TolC to export a wide range of toxic exogenous compounds (antibiotics, dyes, detergents, bile compounds, organic solvents) and some endogenous metabolites (enterobactin, porphyrinogens/porphyrins). The well characterized AcrB system (TRANS-CPLX-201 "AcrAB-TolC") is the major contributor to intrinsic resistance for many compounds ; the AcrD system (AcrAD-TolC) exports Aminoglycoside-Antibiotics "aminoglycoside" antibiotics, although a broader substrate range can be seen upon AcrD over-production or in the absence of AcrB (for greater detail see ACRD-MONOMER "AcrD"). The AcrAD-TolC subunit stoichiometry shown here is inferred by analogy with the AcrAB-TolC complex.

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1551|reaction.ecocyc.TRANS-RXN-1551]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1552|reaction.ecocyc.TRANS-RXN-1552]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-360|reaction.ecocyc.TRANS-RXN-360]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Aminoglycosides|molecule.ecocyc.Aminoglycosides]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Gentamycins|molecule.ecocyc.Gentamycins]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P02930|protein.P02930]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P0AE06|protein.P0AE06]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6 | EcoCyc transporter component coefficient=6
- `is_component_of` <-- [[protein.P24177|protein.P24177]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## External IDs

- `EcoCyc:CPLX0-3932`
- `PDB:5V5S`
- `PDB:5O66`
- `PDB:5NG5`

## Notes

1*complex.ecocyc.CPLX0-7964|3*protein.P24177|6*protein.P0AE06
