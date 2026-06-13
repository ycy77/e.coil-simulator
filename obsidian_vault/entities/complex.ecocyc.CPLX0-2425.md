---
entity_id: "complex.ecocyc.CPLX0-2425"
entity_type: "complex"
name: "DNA gyrase"
source_database: "EcoCyc"
source_id: "CPLX0-2425"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Topoisomerase II"
---

# DNA gyrase

`complex.ecocyc.CPLX0-2425`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2425`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AES4|protein.P0AES4]], [[protein.P0AES6|protein.P0AES6]]

## Enriched Summary

E. coli possess multiple DNA topoisomerases which coordinate, as well as compete, in order to maintain chromosomes in the appropriate topological state required for replication and transcription. DNA gyrase is one of two essential members of the type IIA topoisomerase family in E. coli; the other is CPLX0-2424. DNA gyrase carries out ATP-dependent supercoiling of chromosomal DNA, as well as being involved in decatenation of newly synthesized chromosomal and plasmid DNA. Gyrase consists of 2 GyrA and 2 GyrB subunits . Tyrosine 122 of the GyrA subunit covalently links the 5' DNA phosphoryl group of the DNA that is cleaved . The GyrA amino-termini form a dimeric core flanked by their carboxy-terminal domains, which form spirals that wrap the target DNA . These GyrA carboxy-terminal domains impart unidirectionality on gyrase supercoiling activity . The GyrB amino-terminal domain contains the gyrase ATPase activity and is a known binding site for antibiotics that inhibit gyrase function . GyrB dimerizes in a "V" shape, with the amino-termini coming together at the base to form the 20 Å ATP-operated DNA-binding clamp and the carboxy-termini at the ends of the "V" involved in protein-protein interaction . Other studies of the full gyrase tetramer have been carried out in the presence and absence of bound substrate...

## Biological Role

Catalyzes 5.99.1.3-RXN (reaction.ecocyc.5.99.1.3-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

E. coli possess multiple DNA topoisomerases which coordinate, as well as compete, in order to maintain chromosomes in the appropriate topological state required for replication and transcription. DNA gyrase is one of two essential members of the type IIA topoisomerase family in E. coli; the other is CPLX0-2424. DNA gyrase carries out ATP-dependent supercoiling of chromosomal DNA, as well as being involved in decatenation of newly synthesized chromosomal and plasmid DNA. Gyrase consists of 2 GyrA and 2 GyrB subunits . Tyrosine 122 of the GyrA subunit covalently links the 5' DNA phosphoryl group of the DNA that is cleaved . The GyrA amino-termini form a dimeric core flanked by their carboxy-terminal domains, which form spirals that wrap the target DNA . These GyrA carboxy-terminal domains impart unidirectionality on gyrase supercoiling activity . The GyrB amino-terminal domain contains the gyrase ATPase activity and is a known binding site for antibiotics that inhibit gyrase function . GyrB dimerizes in a "V" shape, with the amino-termini coming together at the base to form the 20 Å ATP-operated DNA-binding clamp and the carboxy-termini at the ends of the "V" involved in protein-protein interaction . Other studies of the full gyrase tetramer have been carried out in the presence and absence of bound substrate . Gyrase supercoils and relaxes DNA by cleaving one duplex strand entirely and passing the other, intact DNA duplex through it. The initial gyrase cleavage leaves a staggered cut with 5' overhangs, which remain covalently attached to the GyrA subunits throughout strand transfer . Indeed, inhibiting the gyrase ATPase stalls the reaction in the middle, yielding double-strand breaks with GyrA monomers attached to each 5' overhang . DNA supercoiling appears to operate th

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.5.99.1.3-RXN|reaction.ecocyc.5.99.1.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AES4|protein.P0AES4]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0AES6|protein.P0AES6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-2425`
- `PDB:3NUH`
- `PDB:6RKW`
- `PDB:6RKV`
- `PDB:6RKU`
- `PDB:6RKS`
- `PDB:7Z9M`
- `PDB:7Z9K`
- `PDB:7Z9G`
- `QSPROTEOME:QS00182621`

## Notes

2*protein.P0AES4|2*protein.P0AES6
