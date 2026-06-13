---
entity_id: "complex.ecocyc.CPLX0-8189"
entity_type: "complex"
name: "peptidyl-lysine N-acetyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8189"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# peptidyl-lysine N-acetyltransferase

`complex.ecocyc.CPLX0-8189`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8189`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76594|protein.P76594]]

## Enriched Summary

PatZ (also referred to as YfiQ) is the primary Nε-lysine acetyltransferase (KAT) in E. coli, though several additional KATs have been identified . It is required for glucose-dependent acetylation of several lysine residues within RNA polymerase , for acetylation of Lys544 in EG11259-MONOMER and Lys501 in EG11620-MONOMER , and for acetylation of PD03831 DnaA , of a large number of additional proteins that were identified by mass spectrometry and of CPLX0-226 when GUANOSINE-5DP-3DP is present . YfiQ acetylates EG10900-MONOMER under nutrient limitation , which in turn indirectly regulates translation of CRP, RelA and SpoT . A large fraction of peptidyl-lysine acetylation in E. coli is not dependent on PatZ . Metabolic differences between the E. coli B and K-12 strains that may involve peptidyl-lysine acetylation have been investigated . PatZ can auto-acetylate, leading to a conversion from a homotetrameric to a predominantly homooctameric form . A patZ mutant has decreased resistance to oxidative and heat stress. Overexpression of PatZ increases growth yield in rich medium . Deletion of patZ does not eliminate acetylation of a heterologous protein produced in E. coli . The "acetylome" of a ΔpatZ mutant compared to wild type shows significant increases in the ratio of peptide acetylation in acetate-grown cells and, to a lesser extent, in stationary phase glucose cultures...

## Biological Role

Catalyzes RXN0-7160 (reaction.ecocyc.RXN0-7160).

## Annotation

PatZ (also referred to as YfiQ) is the primary Nε-lysine acetyltransferase (KAT) in E. coli, though several additional KATs have been identified . It is required for glucose-dependent acetylation of several lysine residues within RNA polymerase , for acetylation of Lys544 in EG11259-MONOMER and Lys501 in EG11620-MONOMER , and for acetylation of PD03831 DnaA , of a large number of additional proteins that were identified by mass spectrometry and of CPLX0-226 when GUANOSINE-5DP-3DP is present . YfiQ acetylates EG10900-MONOMER under nutrient limitation , which in turn indirectly regulates translation of CRP, RelA and SpoT . A large fraction of peptidyl-lysine acetylation in E. coli is not dependent on PatZ . Metabolic differences between the E. coli B and K-12 strains that may involve peptidyl-lysine acetylation have been investigated . PatZ can auto-acetylate, leading to a conversion from a homotetrameric to a predominantly homooctameric form . A patZ mutant has decreased resistance to oxidative and heat stress. Overexpression of PatZ increases growth yield in rich medium . Deletion of patZ does not eliminate acetylation of a heterologous protein produced in E. coli . The "acetylome" of a ΔpatZ mutant compared to wild type shows significant increases in the ratio of peptide acetylation in acetate-grown cells and, to a lesser extent, in stationary phase glucose cultures. The increase in the patZ mutant may be caused by deregulation of chemical acetylation . ΔEG10027, ΔEG20173 and ΔpatZ mutant analyses found that acetyl phosphate metabolism affects lysine acetylation globally in cells, whereas PatZ did not affect global acetylation levels . Overexpression of patZ appears to increase the global level of protein-lysine propionylation , reduces motility of the K-12 strain BW25

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7160|reaction.ecocyc.RXN0-7160]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76594|protein.P76594]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8189`
- `QSPROTEOME:QS00195505`

## Notes

4*protein.P76594
