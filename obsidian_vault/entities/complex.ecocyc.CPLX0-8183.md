---
entity_id: "complex.ecocyc.CPLX0-8183"
entity_type: "complex"
name: "serine endoprotease"
source_database: "EcoCyc"
source_id: "CPLX0-8183"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# serine endoprotease

`complex.ecocyc.CPLX0-8183`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8183`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AEE3|protein.P0AEE3]]

## Enriched Summary

DegS is one of three high temperature requirement (HtrA) proteases (CPLX0-2921 "DegP", G7682-MONOMER "DegQ" and DegS) which function to ensure cell protein quality by sensing and reacting to damaged and mislocalised proteins. DegS is a membrane anchored protease which senses misfolded/unfolded outer membrane proteins and in concert with the metalloprotease EG12436-MONOMER "RseP" catalyses cleavage of the antisigma factor EG12341-MONOMER "RseA" which ultimately results in the activation of the RPOE-MONOMER σE-mediated stress response . Crystallised, truncated (lacking its N-terminal membrane anchor) DegS is homotrimeric in structure. The DegS monomer consists of two globular domains: an N-terminal serine protease domain and a C-terminal PDZ (protein:protein interaction) domain . Formation of the trimer is mediated by the serine protease domains. Binding of peptides derived from the C-terminal sequence of outer membrane proteins (OMPs) induces a series of conformational changes that activate protease function . Different OMP peptides activate DegS to different degrees . 4 loop structures (L1, L2, L3 and LD) within the protease domain are involved in activation of DegS - L3 serves as a versatile sensor of the PDZ bound activator. In the absence of stress signals the PDZ domain and L3 interact to inhibit protease activity...

## Biological Role

Catalyzes RXN0-3182 (reaction.ecocyc.RXN0-3182).

## Annotation

DegS is one of three high temperature requirement (HtrA) proteases (CPLX0-2921 "DegP", G7682-MONOMER "DegQ" and DegS) which function to ensure cell protein quality by sensing and reacting to damaged and mislocalised proteins. DegS is a membrane anchored protease which senses misfolded/unfolded outer membrane proteins and in concert with the metalloprotease EG12436-MONOMER "RseP" catalyses cleavage of the antisigma factor EG12341-MONOMER "RseA" which ultimately results in the activation of the RPOE-MONOMER σE-mediated stress response . Crystallised, truncated (lacking its N-terminal membrane anchor) DegS is homotrimeric in structure. The DegS monomer consists of two globular domains: an N-terminal serine protease domain and a C-terminal PDZ (protein:protein interaction) domain . Formation of the trimer is mediated by the serine protease domains. Binding of peptides derived from the C-terminal sequence of outer membrane proteins (OMPs) induces a series of conformational changes that activate protease function . Different OMP peptides activate DegS to different degrees . 4 loop structures (L1, L2, L3 and LD) within the protease domain are involved in activation of DegS - L3 serves as a versatile sensor of the PDZ bound activator. In the absence of stress signals the PDZ domain and L3 interact to inhibit protease activity . Interaction between the L3 loop and an OMP-free PDZ domain stabilizes inactive DegS; binding of an OMP peptide to the PDZ domain requires conformational rearrangement which destabilizes this interaction and shifts the equilibrium to favour active DegS. A steric clash between Met319 in the PDZ domain and Asn182 in the L3 loop is an important determinant of DegS activation; replacement of Asn182 by residues with small side chains (glycine / alanine) result

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3182|reaction.ecocyc.RXN0-3182]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AEE3|protein.P0AEE3]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-8183`
- `QSPROTEOME:QS00196993`

## Notes

3*protein.P0AEE3
