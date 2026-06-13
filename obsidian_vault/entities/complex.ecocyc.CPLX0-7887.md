---
entity_id: "complex.ecocyc.CPLX0-7887"
entity_type: "complex"
name: "glutamate—pyruvate aminotransferase AlaC"
source_database: "EcoCyc"
source_id: "CPLX0-7887"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutamate—pyruvate aminotransferase AlaC

`complex.ecocyc.CPLX0-7887`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7887`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P77434|protein.P77434]]

## Enriched Summary

AlaC is one of three major alanine-synthesizing transaminases. AlaA and AlaC together account for 90% of glutamic-pyruvic transaminase (GPT) activity in the cell . A homology model of the enzyme based on the crystal structure of AlaA has been generated . An alaC deletion strain has no growth defect, but an alaA avtA alaC triple mutant has a slow growth phenotype in liquid medium. The defect can be rescued by addition of alanine . Fitness and competitive growth experiments were performed under different growth conditions. Particularly under oxygen-limiting conditions, the doubling time of the ΔalaC strain in minimal media is increased compared to growth in rich media; unlike for the alaA and avtA mutants, addition of L-alanine returns the doubling time to that observed in DMEM medium. Under competitive growth conditions, the ΔalaC mutation confers a disadvantage compared to wild type even in rich media . Expression of alaC is activated by the transcriptional regulator SgrR. AlaC may thus play a role in glucose-phosphate stress . However, an alaC deletion mutant does not show altered sensitivity to α-methylglucoside, which induces sugar-phosphate stress . AlaC is one of three major alanine-synthesizing transaminases. AlaA and AlaC together account for 90% of glutamic-pyruvic transaminase (GPT) activity in the cell...

## Biological Role

Catalyzes ALANINE-AMINOTRANSFERASE-RXN (reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN).

## Annotation

AlaC is one of three major alanine-synthesizing transaminases. AlaA and AlaC together account for 90% of glutamic-pyruvic transaminase (GPT) activity in the cell . A homology model of the enzyme based on the crystal structure of AlaA has been generated . An alaC deletion strain has no growth defect, but an alaA avtA alaC triple mutant has a slow growth phenotype in liquid medium. The defect can be rescued by addition of alanine . Fitness and competitive growth experiments were performed under different growth conditions. Particularly under oxygen-limiting conditions, the doubling time of the ΔalaC strain in minimal media is increased compared to growth in rich media; unlike for the alaA and avtA mutants, addition of L-alanine returns the doubling time to that observed in DMEM medium. Under competitive growth conditions, the ΔalaC mutation confers a disadvantage compared to wild type even in rich media . Expression of alaC is activated by the transcriptional regulator SgrR. AlaC may thus play a role in glucose-phosphate stress . However, an alaC deletion mutant does not show altered sensitivity to α-methylglucoside, which induces sugar-phosphate stress .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77434|protein.P77434]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7887`
- `QSPROTEOME:QS00049673`

## Notes

2*protein.P77434
