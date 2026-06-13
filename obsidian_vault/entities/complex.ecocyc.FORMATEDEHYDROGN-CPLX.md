---
entity_id: "complex.ecocyc.FORMATEDEHYDROGN-CPLX"
entity_type: "complex"
name: "formate dehydrogenase N"
source_database: "EcoCyc"
source_id: "FORMATEDEHYDROGN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Fdh-N"
  - "formate:menaquinone oxidoreductase"
---

# formate dehydrogenase N

`complex.ecocyc.FORMATEDEHYDROGN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FORMATEDEHYDROGN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.ALPHA-SUBUNIT-CPLX|complex.ecocyc.ALPHA-SUBUNIT-CPLX]]

## Enriched Summary

fdnGHI encodes membrane bound formate dehydrogenase N (FDH-N) - a respiratory enzyme that catalyses the oxidation of formate to carbon dioxide, donating electrons to the quinone pool for the reduction of anaerobic respiratory substrates such as nitrate and trimethylamine N-oxide (as seen by the multiple pathways it is associated with). FDH-N is a member of the complex iron sulfur molybdoenzyme (CISM) family . The oxidation of formate by FDH-N is electrogenic (H+/e- = 1); oxidation of formate in the periplasm is accompanied by menaquinone reduction at the cytoplasmic face of the inner membrane . Expression of formate dehydrogenase-N is induced by nitrate and anaerobiosis, mediated by NarL and Fnr, respectively . Purified FDH-N contains three subunits, designated α (FdnG), β (FdnH) and γ (FdnI) . A crystal structure, resolved at 1.6 Å, indicates that this subcomplex is further organised into physiologically relevant trimers with the α and β subunits located towards the periplasmic face of the inner membrane and the γ subunits located towards the cytoplasm. Electrons are tranferred from the site of formate oxidation in the α subunit across the membrane to the site of menaquinone reduction in the γ subunit. Protons are taken up from the cytoplasm at the menaquinone reduction site . E...

## Biological Role

Catalyzes formate dehydrogenase (menaquinone) (reaction.ecocyc.FORMATEDEHYDROG-RXN). Bound by Heme (molecule.C00032), bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

fdnGHI encodes membrane bound formate dehydrogenase N (FDH-N) - a respiratory enzyme that catalyses the oxidation of formate to carbon dioxide, donating electrons to the quinone pool for the reduction of anaerobic respiratory substrates such as nitrate and trimethylamine N-oxide (as seen by the multiple pathways it is associated with). FDH-N is a member of the complex iron sulfur molybdoenzyme (CISM) family . The oxidation of formate by FDH-N is electrogenic (H+/e- = 1); oxidation of formate in the periplasm is accompanied by menaquinone reduction at the cytoplasmic face of the inner membrane . Expression of formate dehydrogenase-N is induced by nitrate and anaerobiosis, mediated by NarL and Fnr, respectively . Purified FDH-N contains three subunits, designated α (FdnG), β (FdnH) and γ (FdnI) . A crystal structure, resolved at 1.6 Å, indicates that this subcomplex is further organised into physiologically relevant trimers with the α and β subunits located towards the periplasmic face of the inner membrane and the γ subunits located towards the cytoplasm. Electrons are tranferred from the site of formate oxidation in the α subunit across the membrane to the site of menaquinone reduction in the γ subunit. Protons are taken up from the cytoplasm at the menaquinone reduction site . E. coli K-12 contains two other formate dehydrogenases - CPLX0-13310 "formate dehydrogenase-O" (low level constitutive expression) and FORMATEDEHYDROGH-MONOMER "formate dehydrogenase-H" - a component of the fermentative formate-hydrogenlyase complex. Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.FORMATEDEHYDROG-RXN|reaction.ecocyc.FORMATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (7)

- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.ALPHA-SUBUNIT-CPLX|complex.ecocyc.ALPHA-SUBUNIT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3
- `is_component_of` <-- [[protein.P0AAJ3|protein.P0AAJ3]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P0AEK7|protein.P0AEK7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P24183|protein.P24183]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:FORMATEDEHYDROGN-CPLX`
- `PDB:1KQG`
- `PDB:1KQF`

## Notes

3*complex.ecocyc.ALPHA-SUBUNIT-CPLX
