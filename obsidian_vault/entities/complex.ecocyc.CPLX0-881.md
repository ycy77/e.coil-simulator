---
entity_id: "complex.ecocyc.CPLX0-881"
entity_type: "complex"
name: "ClpA ATP-dependent protease specificity component and chaperone"
source_database: "EcoCyc"
source_id: "CPLX0-881"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ClpA ATP-dependent protease specificity component and chaperone

`complex.ecocyc.CPLX0-881`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-881`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABH9|protein.P0ABH9]]

## Enriched Summary

ClpA is an ATP-dependent molecular chaperone of the Hsp100 type that serves as a substrate-specifying adapter for the ClpP serine protease in the ClpAP and ClpAXP protease complexes. ClpA is a member of the AAA+ (ATPases associated with diverse cellular activities) superfamily of ATPases . Each ClpA monomer has two domains, leading to a double-stacked ring structure in the complete ClpA hexamer . The putative substrate-recognition domain of ClpA is stable and folds independently, unlike the matching domains in ClpB and ClpX . Each ClpA monomer has two AAA+ modules (consensus ATP-binding sites), the first of which interacts with the amino-terminal domain of the protein . A lysine mutation in either ATP-binding site prevents the ATP-dependent formation of the ClpA hexamer, as well as disrupting ATPase activity and removing the ability to activate ClpP. Mutants in the second ATP-binding site were still able to stimulate degradation of some shorter peptide substrates requiring nucleotide binding, but not hydrolysis . ClpA lacking its own amino-terminal domain is still able to function as both chaperone and protease adaptor, though it is less effective in both roles than the wild-type protein . The ClpA hexamer forms in an ATP-dependent manner . Successful formation of the hexamer and subsequent interaction with ClpP requires the carboxy-terminus of ClpA...

## Biological Role

Component of ClpAP (complex.ecocyc.CPLX0-3104), ClpAXP (complex.ecocyc.CPLX0-3108).

## Annotation

ClpA is an ATP-dependent molecular chaperone of the Hsp100 type that serves as a substrate-specifying adapter for the ClpP serine protease in the ClpAP and ClpAXP protease complexes. ClpA is a member of the AAA+ (ATPases associated with diverse cellular activities) superfamily of ATPases . Each ClpA monomer has two domains, leading to a double-stacked ring structure in the complete ClpA hexamer . The putative substrate-recognition domain of ClpA is stable and folds independently, unlike the matching domains in ClpB and ClpX . Each ClpA monomer has two AAA+ modules (consensus ATP-binding sites), the first of which interacts with the amino-terminal domain of the protein . A lysine mutation in either ATP-binding site prevents the ATP-dependent formation of the ClpA hexamer, as well as disrupting ATPase activity and removing the ability to activate ClpP. Mutants in the second ATP-binding site were still able to stimulate degradation of some shorter peptide substrates requiring nucleotide binding, but not hydrolysis . ClpA lacking its own amino-terminal domain is still able to function as both chaperone and protease adaptor, though it is less effective in both roles than the wild-type protein . The ClpA hexamer forms in an ATP-dependent manner . Successful formation of the hexamer and subsequent interaction with ClpP requires the carboxy-terminus of ClpA. In its ATP-bound state, ClpA is protease resistant . ClpA is required for the ATP-dependent degradation of certain substrates by ClpP, including some abnormal proteins and the in vitro test substrate casein . ClpA binds to the SsrA degradation peptide tag, with one tag binding per ClpA hexamer. This interaction does not depend on either ATP-binding domain in ClpA . The amino-terminal domain of ClpA is required for binding n

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3104|complex.ecocyc.CPLX0-3104]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3108|complex.ecocyc.CPLX0-3108]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ABH9|protein.P0ABH9]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-881`
- `QSPROTEOME:QS00181873`

## Notes

6*protein.P0ABH9
