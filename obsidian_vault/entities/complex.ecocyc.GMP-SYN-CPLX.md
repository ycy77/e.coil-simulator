---
entity_id: "complex.ecocyc.GMP-SYN-CPLX"
entity_type: "complex"
name: "GMP synthetase"
source_database: "EcoCyc"
source_id: "GMP-SYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# GMP synthetase

`complex.ecocyc.GMP-SYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GMP-SYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P04079|protein.P04079]]

## Enriched Summary

GMP synthetase catalyzes the glutamine- or ammonia-dependent synthesis of GMP from XMP . GMP synthetase contains an N-terminal glutamine amide transfer (GAT) domain , a central ATP-pyrophosphatase (ATPP) domain, and a C-terminal dimerization domain . The GAT domain utilizes glutamine to generate ammonia, which is then transferred to the ATPP domain containing the adenylylated XMP intermediate via a substrate-protective channel or tunnel. A protein consisting only of the ATPP and dimerization domains of GMP synthetase dimerizes in solution and has similar Km values for ATP, XMP, and ammonia as the full-length protein. However, the rate of catalysis using ammonia as a substrate is dramatically increased, possibly due to enhanced access to the active site . Rapid kinetics studies of the full-length enzyme allowed analysis of the catalytic cycle, including observation of the enzyme-bound adenylylated XMP intermediate and the functional role of a substrate-induced conformational change . A model of a catalytically active structure of the enzyme showed the presence of an ammonia tunnel and an interdomain salt bridge at its edge, between H186 in the glutaminase domain and E383 in the synthetase domain. Mutagenesis of these residues resulted in significantly reduced glutaminase activity and uncoupling of the two half reactions...

## Biological Role

Catalyzes GMP-SYN-GLUT-RXN (reaction.ecocyc.GMP-SYN-GLUT-RXN), GMP-SYN-NH3-RXN (reaction.ecocyc.GMP-SYN-NH3-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

GMP synthetase catalyzes the glutamine- or ammonia-dependent synthesis of GMP from XMP . GMP synthetase contains an N-terminal glutamine amide transfer (GAT) domain , a central ATP-pyrophosphatase (ATPP) domain, and a C-terminal dimerization domain . The GAT domain utilizes glutamine to generate ammonia, which is then transferred to the ATPP domain containing the adenylylated XMP intermediate via a substrate-protective channel or tunnel. A protein consisting only of the ATPP and dimerization domains of GMP synthetase dimerizes in solution and has similar Km values for ATP, XMP, and ammonia as the full-length protein. However, the rate of catalysis using ammonia as a substrate is dramatically increased, possibly due to enhanced access to the active site . Rapid kinetics studies of the full-length enzyme allowed analysis of the catalytic cycle, including observation of the enzyme-bound adenylylated XMP intermediate and the functional role of a substrate-induced conformational change . A model of a catalytically active structure of the enzyme showed the presence of an ammonia tunnel and an interdomain salt bridge at its edge, between H186 in the glutaminase domain and E383 in the synthetase domain. Mutagenesis of these residues resulted in significantly reduced glutaminase activity and uncoupling of the two half reactions . A crystal stucture of GMP synthetase has been solved at 2.2 Å resolution . The enzyme from E. coli B is a dimer in solution , while the crystal structure of GMP synthetase contained a dimer of dimers. Strains containing a guaA null mutation are auxotrophic for guanine . A guaA null mutant contains modestly higher levels of xanthine in RNA, potentially interfering with RNA function . A guaA-disrupted mutant was used to shut down the XMP to GMP reaction i

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GMP-SYN-GLUT-RXN|reaction.ecocyc.GMP-SYN-GLUT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GMP-SYN-NH3-RXN|reaction.ecocyc.GMP-SYN-NH3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P04079|protein.P04079]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GMP-SYN-CPLX`
- `QSPROTEOME:QS00181695`

## Notes

2*protein.P04079
