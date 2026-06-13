---
entity_id: "complex.ecocyc.CPLX0-7888"
entity_type: "complex"
name: "glutamate—pyruvate aminotransferase AlaA"
source_database: "EcoCyc"
source_id: "CPLX0-7888"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutamate—pyruvate aminotransferase AlaA

`complex.ecocyc.CPLX0-7888`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7888`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A959|protein.P0A959]]

## Enriched Summary

The G7184 gene was first identified as a mutant with a leaky requirement for L-ALPHA-ALANINE or VAL . AlaA is one of three major alanine-synthesizing transaminases. AlaA and AlaC together account for 90% of glutamate-pyruvate transaminase (GPT) activity in the cell . A crystal structure of AlaA has been solved at 2.11 Å resolution. The structure shows a symmetric α2 homodimer typical of fold type I aminotransferases . An alaA deletion strain has no growth defect, but an alaA avtA double mutant forms small colonies on agar plates. An alaA avtA alaC triple mutant has a slow growth phenotype in liquid medium. The defects of the double and triple mutants can be rescued by addition of alanine . Fitness and competitive growth experiments were performed under different growth conditions. Particularly under oxygen-limiting conditions, the doubling time of the ΔalaA strain in minimal media is increased compared to growth in rich media. Under competitive growth conditions, the ΔalaA mutation confers a disadvantage compared to wild type even in rich media . alaA was identified in a screen for genes that reduce the lethal effects of stress. An alaA insertion mutant is more sensitive than wild type to mitomycin C and other stresses and less sensitive to 10% SDS...

## Biological Role

Catalyzes ALANINE-AMINOTRANSFERASE-RXN (reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN).

## Annotation

The G7184 gene was first identified as a mutant with a leaky requirement for L-ALPHA-ALANINE or VAL . AlaA is one of three major alanine-synthesizing transaminases. AlaA and AlaC together account for 90% of glutamate-pyruvate transaminase (GPT) activity in the cell . A crystal structure of AlaA has been solved at 2.11 Å resolution. The structure shows a symmetric α2 homodimer typical of fold type I aminotransferases . An alaA deletion strain has no growth defect, but an alaA avtA double mutant forms small colonies on agar plates. An alaA avtA alaC triple mutant has a slow growth phenotype in liquid medium. The defects of the double and triple mutants can be rescued by addition of alanine . Fitness and competitive growth experiments were performed under different growth conditions. Particularly under oxygen-limiting conditions, the doubling time of the ΔalaA strain in minimal media is increased compared to growth in rich media. Under competitive growth conditions, the ΔalaA mutation confers a disadvantage compared to wild type even in rich media . alaA was identified in a screen for genes that reduce the lethal effects of stress. An alaA insertion mutant is more sensitive than wild type to mitomycin C and other stresses and less sensitive to 10% SDS . Studies with a ΔEG10372 Δ EG10403-EG10404 strain, which is not able to use GLT as an amine donor, showed that L-ALPHA-ALANINE could not be used as an amine donor. However, when the EG11408 gene was also mutated, resulting in a higher L-ALPHA-ALANINE concentration, L-ALPHA-ALANINE served as an amine donor due to the activity of AlaA . alaA and yfbR may form an operon .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A959|protein.P0A959]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7888`
- `QSPROTEOME:QS00195497`

## Notes

2*protein.P0A959
