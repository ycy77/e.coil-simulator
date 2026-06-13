---
entity_id: "complex.ecocyc.CPLX0-10380"
entity_type: "complex"
name: "6-N-hydroxylaminopurine resistance protein"
source_database: "EcoCyc"
source_id: "CPLX0-10380"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 6-N-hydroxylaminopurine resistance protein

`complex.ecocyc.CPLX0-10380`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-10380`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P75863|protein.P75863]]

## Enriched Summary

YcbX functions in the molybdenum cofactor-dependent pathway for detoxification of N-hydroxylated base analogs, which appears to involve their reduction to adenine . The ALPHACOMP-MONOMER CysJ flavin reductase functions as a partner of YcbX, potentially by providing the reducing equivalents required for a YcbX-catalyzed detoxification reaction. This function is independent of EG10190 CysI, with which CysJ forms an SULFITE-REDUCT-CPLX . YcbX contains three domains, an N-terminal β-barrel domain , a central MOSC (MoCo sulfurase C-terminal) domain, and a C-terminal [2Fe-2S]-ferredoxin-like domain . YcbX is not involved in biosynthesis of the molybdenum cofactor . A ycbX mutant shows increased sensitivity to the toxic effects of the purine analogues CPD-15922 and CPD-15921, but not hydroxylamine . A ΔEG11939 ghxP mutation suppresses the sensitivity of a ΔycbX strain to these purine analogues . YcbX is specific for N-hydroxylated substrates and does not catalytically reduce N-oxides. Activity is highest at a pH optimum of 7.1 with pKa values of 6.2 and 8.1 , very similar to another Mo-dependent enzyme, EG11870-MONOMER . The cofactor used by the enzyme appears to be the GMP-free CPD-15870 rather than CPD-582 . The coordination environment for the CPD-15870 was characterized in two different oxidation states...

## Biological Role

Catalyzes RXN0-7398 (reaction.ecocyc.RXN0-7398). Bound by Molybdoenzyme molybdenum cofactor (molecule.C18237), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6).

## Annotation

YcbX functions in the molybdenum cofactor-dependent pathway for detoxification of N-hydroxylated base analogs, which appears to involve their reduction to adenine . The ALPHACOMP-MONOMER CysJ flavin reductase functions as a partner of YcbX, potentially by providing the reducing equivalents required for a YcbX-catalyzed detoxification reaction. This function is independent of EG10190 CysI, with which CysJ forms an SULFITE-REDUCT-CPLX . YcbX contains three domains, an N-terminal β-barrel domain , a central MOSC (MoCo sulfurase C-terminal) domain, and a C-terminal [2Fe-2S]-ferredoxin-like domain . YcbX is not involved in biosynthesis of the molybdenum cofactor . A ycbX mutant shows increased sensitivity to the toxic effects of the purine analogues CPD-15922 and CPD-15921, but not hydroxylamine . A ΔEG11939 ghxP mutation suppresses the sensitivity of a ΔycbX strain to these purine analogues . YcbX is specific for N-hydroxylated substrates and does not catalytically reduce N-oxides. Activity is highest at a pH optimum of 7.1 with pKa values of 6.2 and 8.1 , very similar to another Mo-dependent enzyme, EG11870-MONOMER . The cofactor used by the enzyme appears to be the GMP-free CPD-15870 rather than CPD-582 . The coordination environment for the CPD-15870 was characterized in two different oxidation states. When oxidized, the Mo(VI) ion is coordinated by two terminal oxo ligands and three S donors (a thiolate S atom from cysteine, and two S donors from the pyranopterin ring). When reduced, the Mo(IV) ion is coordinated by a single terminal oxo ligand, three S donors, and a hydroxyl.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7398|reaction.ecocyc.RXN0-7398]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C18237|molecule.C18237]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P75863|protein.P75863]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-10380`
- `QSPROTEOME:QS00196513`

## Notes

2*protein.P75863
