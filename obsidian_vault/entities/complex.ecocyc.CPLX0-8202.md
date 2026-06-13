---
entity_id: "complex.ecocyc.CPLX0-8202"
entity_type: "complex"
name: "alanine racemase 1"
source_database: "EcoCyc"
source_id: "CPLX0-8202"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# alanine racemase 1

`complex.ecocyc.CPLX0-8202`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8202`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6B4|protein.P0A6B4]]

## Enriched Summary

Alanine racemase 1 (Alr) catalyzes the pyridoxal-5'-phosphate-dependent interconversion of D- and L-alanine. D-alanine is a key component of bacterial peptidoglycan (see pathway PWY-6387). E. coli has two alanine racemases, the constitutive Alr and the metabolically regulated CPLX0-7465 DadX. Alr is much less abundant than derepressed DadX . Crystal structures of wild-type Alr, a D-cycloserine-bound enzyme, and several mutant enzymes have been determined . Four monomers form two identical dimers in the crystallographic asymmetric unit. The subunits, each composed of an N-terminal (βα)8 barrel domain containing the PLP binding site and a C-terminal domain containing β sheet structures, dimerize in a head-to-tail formation . Gel filtration chromatography, native PAGE and analytical ultracentrifugation studies suggest that bacterial alanine racemases exist in a dynamic monomer-dimer equilibrium. Enzymes with low Vmax values had lower association constants than those with high Vmax values . Mutations in the conserved Asp164 and Glu165 residues, which are at the site of substrate entry, reduce catalytic activity of Alr in both directions . Alr was found to be a multicopy suppressor of a ΔEG10583 metC mutant . Despite this suppression, no cystathionine β-lyase (CBL) activity by Alr could be measured in vitro; however, a Y274F mutation in Alr yields low, but measurable CBL activity...

## Biological Role

Catalyzes ALARACECAT-RXN (reaction.ecocyc.ALARACECAT-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Alanine racemase 1 (Alr) catalyzes the pyridoxal-5'-phosphate-dependent interconversion of D- and L-alanine. D-alanine is a key component of bacterial peptidoglycan (see pathway PWY-6387). E. coli has two alanine racemases, the constitutive Alr and the metabolically regulated CPLX0-7465 DadX. Alr is much less abundant than derepressed DadX . Crystal structures of wild-type Alr, a D-cycloserine-bound enzyme, and several mutant enzymes have been determined . Four monomers form two identical dimers in the crystallographic asymmetric unit. The subunits, each composed of an N-terminal (βα)8 barrel domain containing the PLP binding site and a C-terminal domain containing β sheet structures, dimerize in a head-to-tail formation . Gel filtration chromatography, native PAGE and analytical ultracentrifugation studies suggest that bacterial alanine racemases exist in a dynamic monomer-dimer equilibrium. Enzymes with low Vmax values had lower association constants than those with high Vmax values . Mutations in the conserved Asp164 and Glu165 residues, which are at the site of substrate entry, reduce catalytic activity of Alr in both directions . Alr was found to be a multicopy suppressor of a ΔEG10583 metC mutant . Despite this suppression, no cystathionine β-lyase (CBL) activity by Alr could be measured in vitro; however, a Y274F mutation in Alr yields low, but measurable CBL activity. CBL is also a pyridoxal 5-phosphate-dependent activity, but the primary enzyme, MetC, has a different protein fold . Alanine racemase has been a target for antibacterial drug development . Using liquid chromatography/tandem mass spectrometry, D-cycloserine was shown to be an in vivo inhibitor of D-alanine production by alanine racemase . The unsubstituted N(2) moiety of D,L-cycloserine is important

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ALARACECAT-RXN|reaction.ecocyc.ALARACECAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6B4|protein.P0A6B4]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8202`
- `QSPROTEOME:QS00183185`

## Notes

2*protein.P0A6B4
