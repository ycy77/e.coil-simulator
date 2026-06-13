---
entity_id: "complex.ecocyc.CTPSYN-CPLX"
entity_type: "complex"
name: "CTP synthetase"
source_database: "EcoCyc"
source_id: "CTPSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# CTP synthetase

`complex.ecocyc.CTPSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CTPSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A7E5|protein.P0A7E5]]

## Enriched Summary

CTP synthetase catalyzes the glutamine- or ammonia-dependent synthesis of CTP from UTP, the final step in the de novo biosynthesis of CTP. The activity of the enzyme is controlled in multiple ways: product inhibition by CTP (including by promoting polymerization of the enzyme ), positive cooperativity for its substrates, ATP and UTP , and concentration-dependent allosteric regulation by GTP . CTP synthetase contains an N-terminal synthetase domain and a C-terminal glutamine amide transfer (GAT) domain . The catalytic mechanism and kinetic properties of CTP synthetase have been studied. Within the synthetase domain , a phosphorylated UTP intermediate is formed . The K187 residue is required for CTP formation . D107 and L109 facilitate coupling between hydrolysis of glutamine and CTP synthesis . A G352P mutation in the GAT domain and a C379A active site mutation specifically inactivates the glutamine amide transfer activity of the enzyme. The initial step, glutamine hydrolysis, proceeds via a covalent glutamyl-enzyme intermediate at the C379 residue. Activation by GTP is at least partially due to enhancing interactions with the tetrahedral intermediate formed during glutamine hydrolysis...

## Biological Role

Catalyzes CTPSYN-RXN (reaction.ecocyc.CTPSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

CTP synthetase catalyzes the glutamine- or ammonia-dependent synthesis of CTP from UTP, the final step in the de novo biosynthesis of CTP. The activity of the enzyme is controlled in multiple ways: product inhibition by CTP (including by promoting polymerization of the enzyme ), positive cooperativity for its substrates, ATP and UTP , and concentration-dependent allosteric regulation by GTP . CTP synthetase contains an N-terminal synthetase domain and a C-terminal glutamine amide transfer (GAT) domain . The catalytic mechanism and kinetic properties of CTP synthetase have been studied. Within the synthetase domain , a phosphorylated UTP intermediate is formed . The K187 residue is required for CTP formation . D107 and L109 facilitate coupling between hydrolysis of glutamine and CTP synthesis . A G352P mutation in the GAT domain and a C379A active site mutation specifically inactivates the glutamine amide transfer activity of the enzyme. The initial step, glutamine hydrolysis, proceeds via a covalent glutamyl-enzyme intermediate at the C379 residue. Activation by GTP is at least partially due to enhancing interactions with the tetrahedral intermediate formed during glutamine hydrolysis . GTP analogs have been used to study the GTP structural features required for allosteric activation of glutamine hydrolysis, as well as inhibition of glutamine-dependent or ammonia-dependent CTP formation . The native enzyme equilibrates between the monomeric, dimeric and tetrameric forms . The G142 residue is critical for nucleotide-dependent formation of the active tetramer . Like its homolog in Caulobacter crescentus, the E. coli CTP synthetase forms filamentous structures both in vitro and in vivo . Polymerization into filaments is stimulated by the presence of CTP and reversibly decr

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CTPSYN-RXN|reaction.ecocyc.CTPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7E5|protein.P0A7E5]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CTPSYN-CPLX`
- `QSPROTEOME:QS00196997`

## Notes

4*protein.P0A7E5
