---
entity_id: "complex.ecocyc.GLUTKIN-CPLX"
entity_type: "complex"
name: "glutamate 5-kinase"
source_database: "EcoCyc"
source_id: "GLUTKIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "G5K"
---

# glutamate 5-kinase

`complex.ecocyc.GLUTKIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUTKIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A7B5|protein.P0A7B5]]

## Enriched Summary

Glutamate 5-kinase (G5K) catalyzes the first step in the L-proline biosynthesis pathway. G5K activity is feedback-inhibited by L-proline, providing the primary point of control in this pathway . Although G5K activity produces the highly reactive intermediate L-GLUTAMATE-5-P (GP), suggesting channeling of this compound to the following enzyme, a stable complex between G5K and GLUTSEMIALDEHYDROG-CPLX could not be isolated . The channeling of GP has subsequently been challenged by evidence that a protein-protein interaction is not required between G5K and GLUTSEMIALDEHYDROG-MONOMER ProA for proline synthesis, and the measured half-life of GP is long enough to reach ProA . It has been observed that in a EG10768 mutant, which is blocked in L-proline biosynthesis, many single mutations occurred in EG10383 that resulted in leaking of L-GLUTAMATE-5-P into the intracellular milieu, enabling proline biosynthesis . G5K consists of an N-terminal amino acid kinase (AAK) domain and a C-terminal PUA (PseudoUridine synthases and Archaeosine-specific transglycosylases) domain. Deletion of the PUA domain of G5K has demonstrated that the AAK domain alone, like the full-length protein, can form tetramers, catalyze the formation of L-glutamate-5-phosphate and is feedback inhibited by proline...

## Biological Role

Catalyzes GLUTKIN-RXN (reaction.ecocyc.GLUTKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Glutamate 5-kinase (G5K) catalyzes the first step in the L-proline biosynthesis pathway. G5K activity is feedback-inhibited by L-proline, providing the primary point of control in this pathway . Although G5K activity produces the highly reactive intermediate L-GLUTAMATE-5-P (GP), suggesting channeling of this compound to the following enzyme, a stable complex between G5K and GLUTSEMIALDEHYDROG-CPLX could not be isolated . The channeling of GP has subsequently been challenged by evidence that a protein-protein interaction is not required between G5K and GLUTSEMIALDEHYDROG-MONOMER ProA for proline synthesis, and the measured half-life of GP is long enough to reach ProA . It has been observed that in a EG10768 mutant, which is blocked in L-proline biosynthesis, many single mutations occurred in EG10383 that resulted in leaking of L-GLUTAMATE-5-P into the intracellular milieu, enabling proline biosynthesis . G5K consists of an N-terminal amino acid kinase (AAK) domain and a C-terminal PUA (PseudoUridine synthases and Archaeosine-specific transglycosylases) domain. Deletion of the PUA domain of G5K has demonstrated that the AAK domain alone, like the full-length protein, can form tetramers, catalyze the formation of L-glutamate-5-phosphate and is feedback inhibited by proline. However, the deletion greatly diminished the Mg2+ requirement of the enzyme and reduced its sensitivity to proline-mediated feedback inhibition . Site-directed mutagenesis has confirmed that the AAK domain is involved in substrate binding, catalysis, and feedback inhibition by proline . Crystal structures of G5K have been solved . G5K possesses a "dimer of dimers" architecture in which the tetramers are formed by the interaction of two dimers through their AAK domains . While the enzyme purifies as a t

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTKIN-RXN|reaction.ecocyc.GLUTKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7B5|protein.P0A7B5]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:GLUTKIN-CPLX`
- `QSPROTEOME:QS00049717`

## Notes

4*protein.P0A7B5
