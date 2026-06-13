---
entity_id: "complex.ecocyc.CPLX0-3102"
entity_type: "complex"
name: "ClpX ATP-dependent protease specificity component and chaperone"
source_database: "EcoCyc"
source_id: "CPLX0-3102"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ClpX ATP-dependent protease specificity component and chaperone

`complex.ecocyc.CPLX0-3102`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3102`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6H1|protein.P0A6H1]]

## Enriched Summary

ClpX is an ATP-dependent molecular chaperone that serves as a substrate-specifying adaptor for the CPLX0-3101 in the CPLX0-3107 ClpXP and CPLX0-3108 ClpAXP protease complexes. ClpX is a member of the AAA+ (ATPases associated with diverse cellular activities) family of ATPases ClpX protects the lambda O protein from heat-induced aggregation, disassembles lambda aggregates and enhances lambda DNA binding. ATP binding is required for all these effects, and disaggregation requires ATP hydrolysis . ClpX also converts inactive, dimeric TrfA into its monomeric form (capable of initiating replication of plasmid RK2) in an ATP-dependent manner . ClpX is required for normal replication of Mu transposase . ClpX catalyzes the ATP-dependent release of MuA from its active transposase tetramer form, allowing recruitment of host factors necessary for post-recombination steps in Mu transposition . ClpX is also able to globally unfold MuA monomers. ClpX recognizes a ten amino acid peptide from the carboxy-terminus of MuA when it is revealed by MuB. ClpX will recognize other proteins with this tag artificially attached . Each ClpX monomer has two PDZ domains that bind to the carboxy-terminus of target proteins. These domains show up as disordered sequence in NMR and are unstable when expressed independently...

## Biological Role

Component of ClpXP (complex.ecocyc.CPLX0-3107), ClpAXP (complex.ecocyc.CPLX0-3108).

## Annotation

ClpX is an ATP-dependent molecular chaperone that serves as a substrate-specifying adaptor for the CPLX0-3101 in the CPLX0-3107 ClpXP and CPLX0-3108 ClpAXP protease complexes. ClpX is a member of the AAA+ (ATPases associated with diverse cellular activities) family of ATPases ClpX protects the lambda O protein from heat-induced aggregation, disassembles lambda aggregates and enhances lambda DNA binding. ATP binding is required for all these effects, and disaggregation requires ATP hydrolysis . ClpX also converts inactive, dimeric TrfA into its monomeric form (capable of initiating replication of plasmid RK2) in an ATP-dependent manner . ClpX is required for normal replication of Mu transposase . ClpX catalyzes the ATP-dependent release of MuA from its active transposase tetramer form, allowing recruitment of host factors necessary for post-recombination steps in Mu transposition . ClpX is also able to globally unfold MuA monomers. ClpX recognizes a ten amino acid peptide from the carboxy-terminus of MuA when it is revealed by MuB. ClpX will recognize other proteins with this tag artificially attached . Each ClpX monomer has two PDZ domains that bind to the carboxy-terminus of target proteins. These domains show up as disordered sequence in NMR and are unstable when expressed independently . ClpX also has an ATP-binding site motif and a zinc-binding domain, the latter being a member of the treble clef zinc finger family, involved in macromolecular interactions . ClpX recognises C-terminal residues 9-11 of the SSRA-RNA "ssrA" peptide tag (AANDENYALAA) . Mutations in the central pore of the ClpX hexamer disrupt recognition of ssrA-tag containing substrates; the ssrA-tag interacts with pore loop regions (RKH loop; pore 1 loop and pore 2 loop) located in the central core of

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3107|complex.ecocyc.CPLX0-3107]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3108|complex.ecocyc.CPLX0-3108]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6H1|protein.P0A6H1]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-3102`
- `QSPROTEOME:QS00166353`
- `PDB:4I9K`
- `PDB:4I63`
- `PDB:4I5O`
- `PDB:4I34`
- `PDB:4I4L`
- `PDB:4I81`

## Notes

6*protein.P0A6H1
