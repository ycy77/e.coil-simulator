---
entity_id: "complex.ecocyc.CPLX0-13310"
entity_type: "complex"
name: "formate dehydrogenase O"
source_database: "EcoCyc"
source_id: "CPLX0-13310"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# formate dehydrogenase O

`complex.ecocyc.CPLX0-13310`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-13310`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.FORMATEDEHYDROGO-CPLX|complex.ecocyc.FORMATEDEHYDROGO-CPLX]]

## Enriched Summary

fdoGHI encodes formate dehydrogenase O (FDH-O) - a respiratory molybdoenzyme that catalyses the oxidation of formate to carbon dioxide, donating electrons to the membrane soluble quinone pool for the reduction of nitrate. FDH-O and nitrate reductase Z participate in a formate to nitrate electron transport pathway that is active when cells are shifted from aerobic to anaerobic conditions. The pathway operates with either menaquinone or ubiquinone . FDH-O appears to be expressed constitutively; unlike formate dehydrogenase N (FDH-N), it is not regulated by Fnr or NarL . Expression of FDH-O is increased under aerobic conditions; under anaerobic conditions, nitrate stimulates expression slightly; the global regulators H-NS and CRP may play a role in regulation of FDH-O expression. FDH-O may contribute to the cells ability to rapidly adapt to anaerobiosis while levels of FDH-N are still insufficient . FDH-O is a heterotrimeric complex consisting of an α (FdoG), a β (FdoH) and a γ (FdoI) subunit - it shares extensive sequence similarity and immunological properties with the anaerobically expressed FDH-N . The presence of a formate oxidase supercomplex consisting of cytochromes bo and bd-1 plus formate dehydrogenase-O in a 1:1:1 stoichiometry has been suggested by electrophoretic and spectrometric analyses . E...

## Biological Role

Catalyzes formate dehydrogenase (menaquinone) (reaction.ecocyc.FORMATEDEHYDROG-RXN). Bound by Heme (molecule.C00032), bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

fdoGHI encodes formate dehydrogenase O (FDH-O) - a respiratory molybdoenzyme that catalyses the oxidation of formate to carbon dioxide, donating electrons to the membrane soluble quinone pool for the reduction of nitrate. FDH-O and nitrate reductase Z participate in a formate to nitrate electron transport pathway that is active when cells are shifted from aerobic to anaerobic conditions. The pathway operates with either menaquinone or ubiquinone . FDH-O appears to be expressed constitutively; unlike formate dehydrogenase N (FDH-N), it is not regulated by Fnr or NarL . Expression of FDH-O is increased under aerobic conditions; under anaerobic conditions, nitrate stimulates expression slightly; the global regulators H-NS and CRP may play a role in regulation of FDH-O expression. FDH-O may contribute to the cells ability to rapidly adapt to anaerobiosis while levels of FDH-N are still insufficient . FDH-O is a heterotrimeric complex consisting of an α (FdoG), a β (FdoH) and a γ (FdoI) subunit - it shares extensive sequence similarity and immunological properties with the anaerobically expressed FDH-N . The presence of a formate oxidase supercomplex consisting of cytochromes bo and bd-1 plus formate dehydrogenase-O in a 1:1:1 stoichiometry has been suggested by electrophoretic and spectrometric analyses . E. coli K-12 contains two other formate dehydrogenases - the anaerobically expressed FORMATEDEHYDROGN-CPLX "formate dehydrogenase-N" complex and FORMATEDEHYDROGH-MONOMER "formate dehydrogenase-H" - a component of the fermentative formate-hydrogenlyase complex. Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.FORMATEDEHYDROG-RXN|reaction.ecocyc.FORMATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (7)

- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.FORMATEDEHYDROGO-CPLX|complex.ecocyc.FORMATEDEHYDROGO-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3
- `is_component_of` <-- [[protein.P0AAJ5|protein.P0AAJ5]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P0AEL0|protein.P0AEL0]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P32176|protein.P32176]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-13310`

## Notes

3*complex.ecocyc.FORMATEDEHYDROGO-CPLX
