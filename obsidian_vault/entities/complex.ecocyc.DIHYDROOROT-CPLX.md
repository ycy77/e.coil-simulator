---
entity_id: "complex.ecocyc.DIHYDROOROT-CPLX"
entity_type: "complex"
name: "dihydroorotase"
source_database: "EcoCyc"
source_id: "DIHYDROOROT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dihydroorotase

`complex.ecocyc.DIHYDROOROT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DIHYDROOROT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P05020|protein.P05020]]

## Enriched Summary

Dihydroorotase (PyrC) catalyzes the cyclization of carbamoyl-aspartate to dihydroorotate, the third reaction in the pathway for de novo biosynthesis of pyrimidine nucleotides. The enzyme is of particular interest because of its potential as an antimalarial drug target. The structure of dihydroorotase has been determined to 1.7 Å resolution. Each subunit has a TIM motif with eight parallel β strands flanked by α helices, as well as a binuclear zinc center with two ions 3.6 Å apart . A 1.9 Å structure resolved in the presence of dihydroorotate shows that a loop in PyrC is in a different conformation in each subunit of the dimer . Additional crystal structures of mutant PyrC or complexed with inhibitors have been reported . The surface loop structure enables productive substrate binding and stabilizes the transition state intermediate . A mechanism has been proposed for the dihydroorotase reaction . The subunits operate cooperatively during catalysis . Translation of pyrC is regulated by transcription start site selection. When CTP is abundant, a site distal to the start codon is chosen, allowing formation of a hairpin that blocks ribosome binding. Otherwise, a proximal site is chosen that prevents hairpin formation, allowing translation...

## Biological Role

Catalyzes DIHYDROOROT-RXN (reaction.ecocyc.DIHYDROOROT-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

Dihydroorotase (PyrC) catalyzes the cyclization of carbamoyl-aspartate to dihydroorotate, the third reaction in the pathway for de novo biosynthesis of pyrimidine nucleotides. The enzyme is of particular interest because of its potential as an antimalarial drug target. The structure of dihydroorotase has been determined to 1.7 Å resolution. Each subunit has a TIM motif with eight parallel β strands flanked by α helices, as well as a binuclear zinc center with two ions 3.6 Å apart . A 1.9 Å structure resolved in the presence of dihydroorotate shows that a loop in PyrC is in a different conformation in each subunit of the dimer . Additional crystal structures of mutant PyrC or complexed with inhibitors have been reported . The surface loop structure enables productive substrate binding and stabilizes the transition state intermediate . A mechanism has been proposed for the dihydroorotase reaction . The subunits operate cooperatively during catalysis . Translation of pyrC is regulated by transcription start site selection. When CTP is abundant, a site distal to the start codon is chosen, allowing formation of a hairpin that blocks ribosome binding. Otherwise, a proximal site is chosen that prevents hairpin formation, allowing translation . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DIHYDROOROT-RXN|reaction.ecocyc.DIHYDROOROT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P05020|protein.P05020]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DIHYDROOROT-CPLX`
- `QSPROTEOME:QS00188479`

## Notes

2*protein.P05020
