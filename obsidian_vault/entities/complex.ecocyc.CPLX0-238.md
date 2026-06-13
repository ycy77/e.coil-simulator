---
entity_id: "complex.ecocyc.CPLX0-238"
entity_type: "complex"
name: "argininosuccinate synthetase"
source_database: "EcoCyc"
source_id: "CPLX0-238"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# argininosuccinate synthetase

`complex.ecocyc.CPLX0-238`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-238`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6E4|protein.P0A6E4]]

## Enriched Summary

Argininosuccinate synthetase (ArgG) catalyzes the penultimate step of arginine biosynthesis. Although enzymological characterization of the E. coli enzyme is lacking, its crystal structure has been determined. The crystal structures of the uncomplexed enzyme and the enzyme in complex with aspartate and citrulline have been determined at 1.6 Å resolution . The crystal structures of the enzyme in complex with ATP, and with ATP and citrulline, have been determined at 2.0 Å resolution . The enzyme was present as a monomer in the crystallographic asymmetric unit. However, unpublished analytical gel filtration data for the E. coli enzyme, and biochemical data for the enzyme from mammals and yeast suggest that the enzyme is functional as a tetramer . The domain structure of the monomer also suggested its ability to form a dimer of dimers . Each monomer has two structural domains. One is a nucleotide binding domain similar to that of the N-type ATP pyrophosphate class of enzymes, the other is a novel catalytic/multimerization domain. The structural data suggested that citrulline binds at the cleft between the two domains and aspartate binds to a loop of the nucleotide binding domain . ATP-induced conformational changes in the nucleotide binding domain occur during catalysis . Based on the crystal structures, the proposed catalytic mechanism involves a two-step reaction...

## Biological Role

Catalyzes ARGSUCCINSYN-RXN (reaction.ecocyc.ARGSUCCINSYN-RXN).

## Annotation

Argininosuccinate synthetase (ArgG) catalyzes the penultimate step of arginine biosynthesis. Although enzymological characterization of the E. coli enzyme is lacking, its crystal structure has been determined. The crystal structures of the uncomplexed enzyme and the enzyme in complex with aspartate and citrulline have been determined at 1.6 Å resolution . The crystal structures of the enzyme in complex with ATP, and with ATP and citrulline, have been determined at 2.0 Å resolution . The enzyme was present as a monomer in the crystallographic asymmetric unit. However, unpublished analytical gel filtration data for the E. coli enzyme, and biochemical data for the enzyme from mammals and yeast suggest that the enzyme is functional as a tetramer . The domain structure of the monomer also suggested its ability to form a dimer of dimers . Each monomer has two structural domains. One is a nucleotide binding domain similar to that of the N-type ATP pyrophosphate class of enzymes, the other is a novel catalytic/multimerization domain. The structural data suggested that citrulline binds at the cleft between the two domains and aspartate binds to a loop of the nucleotide binding domain . ATP-induced conformational changes in the nucleotide binding domain occur during catalysis . Based on the crystal structures, the proposed catalytic mechanism involves a two-step reaction. In the first step, the activation of citrulline is brought about by the nucleophilic attack of the ureido oxygen of citrulline on the α-phosphate of ATP, forming citrulline-adenylate. Formation of this intermediate is enhanced in presence of aspartate. In the second step, the ureido carbon of citrulline-adenylate undergoes a nucleophilic attack by the amino group of aspartate, forming argininosuccinate and relea

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ARGSUCCINSYN-RXN|reaction.ecocyc.ARGSUCCINSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6E4|protein.P0A6E4]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-238`
- `QSPROTEOME:QS00181939`

## Notes

4*protein.P0A6E4
