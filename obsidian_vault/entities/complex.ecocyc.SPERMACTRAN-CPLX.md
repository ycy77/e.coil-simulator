---
entity_id: "complex.ecocyc.SPERMACTRAN-CPLX"
entity_type: "complex"
name: "spermidine N-acetyltransferase"
source_database: "EcoCyc"
source_id: "SPERMACTRAN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# spermidine N-acetyltransferase

`complex.ecocyc.SPERMACTRAN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SPERMACTRAN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A951|protein.P0A951]]

## Enriched Summary

Polyamines are necessary for optimal cell growth, but an excess can lead to growth inhibition. E. coli contains a diamine acetyltransferase that uses the polyamine spermidine as a substrate. It catalyzes the transfer of an acetyl group from acetyl-CoA to either the N-1 or N-8 position of spermidine, effectively reducing the intracellular concentration of polyamines. However, details of the catalytic mechanism and regulation of spermidine acetyltransferase remain to be elucidated . In E. coli K-12 the accumulation of mono-acetylated spermidine occurs in response to a variety of stresses including heat, cold, ethanol, or alkaline shock, but not oxidative stress. Spermidine acetyltransferase is a constitutively expressed enzyme. Its activity increases 2.5-3.5-fold under poor nutrient conditions . A speG-deficient mutant E. coli CAG2242 was shown to have greatly decreased cell viability when spermidine was added during the stationary phase of growth, resulting in the accumulation of intracellular spermidine. Cell viability of the mutant could be recovered by introduction of the cloned speG gene. Spermidine accumulation caused a decrease in protein synthesis, particularly ribosome modulation factor and OmpC . A revertant of this mutant was tolerant to high concentrations of spermidine...

## Biological Role

Catalyzes DIAMACTRANS-RXN (reaction.ecocyc.DIAMACTRANS-RXN), spermidine N8-acetyltransferase (reaction.ecocyc.RXN0-7165), SPERMACTRAN-RXN (reaction.ecocyc.SPERMACTRAN-RXN).

## Annotation

Polyamines are necessary for optimal cell growth, but an excess can lead to growth inhibition. E. coli contains a diamine acetyltransferase that uses the polyamine spermidine as a substrate. It catalyzes the transfer of an acetyl group from acetyl-CoA to either the N-1 or N-8 position of spermidine, effectively reducing the intracellular concentration of polyamines. However, details of the catalytic mechanism and regulation of spermidine acetyltransferase remain to be elucidated . In E. coli K-12 the accumulation of mono-acetylated spermidine occurs in response to a variety of stresses including heat, cold, ethanol, or alkaline shock, but not oxidative stress. Spermidine acetyltransferase is a constitutively expressed enzyme. Its activity increases 2.5-3.5-fold under poor nutrient conditions . A speG-deficient mutant E. coli CAG2242 was shown to have greatly decreased cell viability when spermidine was added during the stationary phase of growth, resulting in the accumulation of intracellular spermidine. Cell viability of the mutant could be recovered by introduction of the cloned speG gene. Spermidine accumulation caused a decrease in protein synthesis, particularly ribosome modulation factor and OmpC . A revertant of this mutant was tolerant to high concentrations of spermidine. It showed increased cell viability due to higher levels of L-glycerol-3-phosphate reducing the binding of excess spermidine to ribosomes which restored protein synthesis . This mutant was also used to show that during growth at low temperature the level of spermidine acetylation increases to prevent spermidine toxicity via ribosome inactivation . The enzyme was shown to be a homotetramer . Purified recombinant enzyme was subjected to preliminary crystallographic analysis at 2.5 Å resolution wh

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.DIAMACTRANS-RXN|reaction.ecocyc.DIAMACTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7165|reaction.ecocyc.RXN0-7165]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SPERMACTRAN-RXN|reaction.ecocyc.SPERMACTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A951|protein.P0A951]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:SPERMACTRAN-CPLX`
- `QSPROTEOME:QS00049551`

## Notes

4*protein.P0A951
