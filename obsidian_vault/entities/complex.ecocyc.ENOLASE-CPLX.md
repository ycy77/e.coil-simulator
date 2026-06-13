---
entity_id: "complex.ecocyc.ENOLASE-CPLX"
entity_type: "complex"
name: "enolase"
source_database: "EcoCyc"
source_id: "ENOLASE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# enolase

`complex.ecocyc.ENOLASE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ENOLASE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6P9|protein.P0A6P9]]

## Enriched Summary

Enolase catalyzes the interconversion of 2-phosphoglycerate and phosphoenolpyruvate during glycolysis and gluconeogenesis in E. coli. It is also a component of the E. coli CPLX0-2381 complex that degrades RNA. In the degradosome enolase has been shown to bind to the C-terminal scaffold region of CPLX0-3461. However, the role of enolase in RNA metabolism has not been fully defined . Enolase has been purified from cell extracts of E. coli B and characterized. It was shown to be a dimer in solution and is dependent upon Mg2+ for its structure . The E. coli K-12 eno gene was later cloned, sequenced and functionally expressed in a temperature-sensitive eno mutant strain . Ligand-detected NMR spectroscopy revealed additional functional interactions between endogenous metabolites and enolase . The crystal structure of recombinant enolase from E. coli K-12 has been determined at 2.5 Å resolution, revealing that its dimer interface is enriched in charged residues relative to typical homodimer interfaces . A later 1.6 Å structure shows enolase bound to its recognition site on RNase E . E. coli enolase is functionally similar to enolases in other organisms, notably in its dependence on Mg2+, inhibition by fluoride in the presence of phosphate, and in its catalytic parameters...

## Biological Role

Catalyzes 2PGADEHYDRAT-RXN (reaction.ecocyc.2PGADEHYDRAT-RXN). Component of degradosome (complex.ecocyc.CPLX0-2381). Bound by Magnesium cation (molecule.C00305).

## Annotation

Enolase catalyzes the interconversion of 2-phosphoglycerate and phosphoenolpyruvate during glycolysis and gluconeogenesis in E. coli. It is also a component of the E. coli CPLX0-2381 complex that degrades RNA. In the degradosome enolase has been shown to bind to the C-terminal scaffold region of CPLX0-3461. However, the role of enolase in RNA metabolism has not been fully defined . Enolase has been purified from cell extracts of E. coli B and characterized. It was shown to be a dimer in solution and is dependent upon Mg2+ for its structure . The E. coli K-12 eno gene was later cloned, sequenced and functionally expressed in a temperature-sensitive eno mutant strain . Ligand-detected NMR spectroscopy revealed additional functional interactions between endogenous metabolites and enolase . The crystal structure of recombinant enolase from E. coli K-12 has been determined at 2.5 Å resolution, revealing that its dimer interface is enriched in charged residues relative to typical homodimer interfaces . A later 1.6 Å structure shows enolase bound to its recognition site on RNase E . E. coli enolase is functionally similar to enolases in other organisms, notably in its dependence on Mg2+, inhibition by fluoride in the presence of phosphate, and in its catalytic parameters. Its pH optimum is significantly higher than vertebrate enolases and is somewhat above those of yeast and plant enolases . E. coli K-12 enolase mutants were shown to grow on glycerate and succinate. They accumulated glycolytic pathway intermediates above the blocked enzyme upon addition of glucose or glycerol to resting cultures . Enolase is required for the rapid, degradosome-mediated degradation of ptsG mRNA in response to high levels of glucose 6-phosphate or fructose 6-phosphate . Immunofluorescence micros

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2PGADEHYDRAT-RXN|reaction.ecocyc.2PGADEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-2381|complex.ecocyc.CPLX0-2381]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6P9|protein.P0A6P9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ENOLASE-CPLX`
- `QSPROTEOME:QS00154565`

## Notes

2*protein.P0A6P9
