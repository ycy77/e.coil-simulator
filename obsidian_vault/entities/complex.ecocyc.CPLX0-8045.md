---
entity_id: "complex.ecocyc.CPLX0-8045"
entity_type: "complex"
name: "molybdopterin molybdotransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8045"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# molybdopterin molybdotransferase

`complex.ecocyc.CPLX0-8045`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8045`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P12281|protein.P12281]]

## Enriched Summary

Molybdopterin molybdenumtransferase (MoeA) mediates the ligation of molybdenum to molybdopterin . Addition of the EG11511-MONOMER MogA protein in the presence of ATP and Mg2+ enhances this process . The activity of purified, recombinant E. coli MoeA was assayed in vitro by reconstitution of nitrate reductase activity in extracts of a Neurospora crassa nit-1 mutant. This assay required the addition of L-cysteine or glutathione . However, a later study reported that these compounds were inhibitory in an in vitro assay . Crystal structures of MoeA have been solved at 2.65 Å and 2.2 Å resolution. Dynamic light scattering data showed that MoeA forms dimers in solution . Site-directed mutagenesis of conserved residues was used to identify residues important for MoeA function . Further mutagenesis experiments and crystal structures of the resulting proteins defined the molybdopterin binding site and separable activities in the two assays employed . When present at high concentrations, other metals including Cu2+, Cd2+ and arsenite can become nonspecifically inserted into the MoO2-molybdopterin cofactor product of MoeA, which may be a basis for metal toxicity in E. coli . Studies using a bacterial two-hybrid system showed that MoeA directly interacts with MobA, MobB and MogA in vivo...

## Biological Role

Catalyzes RXN-21563 (reaction.ecocyc.RXN-21563).

## Annotation

Molybdopterin molybdenumtransferase (MoeA) mediates the ligation of molybdenum to molybdopterin . Addition of the EG11511-MONOMER MogA protein in the presence of ATP and Mg2+ enhances this process . The activity of purified, recombinant E. coli MoeA was assayed in vitro by reconstitution of nitrate reductase activity in extracts of a Neurospora crassa nit-1 mutant. This assay required the addition of L-cysteine or glutathione . However, a later study reported that these compounds were inhibitory in an in vitro assay . Crystal structures of MoeA have been solved at 2.65 Å and 2.2 Å resolution. Dynamic light scattering data showed that MoeA forms dimers in solution . Site-directed mutagenesis of conserved residues was used to identify residues important for MoeA function . Further mutagenesis experiments and crystal structures of the resulting proteins defined the molybdopterin binding site and separable activities in the two assays employed . When present at high concentrations, other metals including Cu2+, Cd2+ and arsenite can become nonspecifically inserted into the MoO2-molybdopterin cofactor product of MoeA, which may be a basis for metal toxicity in E. coli . Studies using a bacterial two-hybrid system showed that MoeA directly interacts with MobA, MobB and MogA in vivo . The MoO2-molybdopterin cofactor product of MoeA is required for optimal activation of the nar and hyc operons . In the presence of the enzyme-specific chaperone NarJ and the mature molybdenum cofactor, MobA, MobB, MoeA and MogA interact with apo-NarG . Mutations in moeA (chlE) were first identified as chlorate-resistant (chlE) and lack active nitrate reductase (narE), biotin sulfoxide reductase (bisB) and other molybdenum cofactor-requiring enzymes including formate dehydrogenase and predicted sel

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21563|reaction.ecocyc.RXN-21563]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P12281|protein.P12281]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8045`
- `QSPROTEOME:QS00197513`

## Notes

2*protein.P12281
