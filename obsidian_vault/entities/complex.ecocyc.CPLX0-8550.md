---
entity_id: "complex.ecocyc.CPLX0-8550"
entity_type: "complex"
name: "protein-lysine deacetylase/desuccinylase/delipoylase"
source_database: "EcoCyc"
source_id: "CPLX0-8550"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "de-hydroxyisobutyrylase"
  - "delactylase"
---

# protein-lysine deacetylase/desuccinylase/delipoylase

`complex.ecocyc.CPLX0-8550`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8550`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P75960|protein.P75960]]

## Enriched Summary

The protein-lysine deacetylase, desuccinylase, de-2-hydroxyisobutyrylase, delactylase and lipoamidase CobB is a Class III sirtuin, a broadly conserved family of NAD+-dependent protein deacetylases. CobB deacetylates acetylated ACS-MONOMER "acetyl-CoA synthetase" and the acetylated chemotaxis response regulator CHEY-MONOMER CheY in vitro. Additional potential substrates for CobB were identified and include CPLX0-236 NhoA , RCSB-MONOMER RcsB and EG10900-MONOMER . The acetylation level of the Lys501 residue in EG11620-MONOMER RNase II, which is controlled by CobB and PatZ, regulates RNase II activity . Deacetylation of S-ADENMETSYN-MONOMER and PD03831 DnaA by CobB may regulate their activities. Acetylated lysine residues of PDXH-MONOMER , MALATE-DEHASE , EG11013-MONOMER , LEUS-MONOMER, ARGS-MONOMER , TYRS-CPLX , ALAS-CPLX alanine—tRNA ligase , THRS-CPLX , ISOCITDEH-SUBUNIT , CITRATE-SI-SYNTHASE , EG11643-MONOMER, and EG10270-MONOMER can be deacetylated by CobB in vitro. 69 acetyllysine residues on 51 proteins were identified as CobB substrates . A proteome microarray was used to identify 183 proteins that interact with CobB . CobB can deacetylate both enzymatically and non-enzymatically acetylated proteins. Acetyllysine residues that are substrates for CobB tend to be surface-exposed and adjacent to alanine, glycine, tyrosine, and negatively charged resides...

## Biological Role

Catalyzes RXN-22964 (reaction.ecocyc.RXN-22964), RXN0-6445 (reaction.ecocyc.RXN0-6445), RXN0-7078 (reaction.ecocyc.RXN0-7078). Bound by NAD+ (molecule.C00003).

## Annotation

The protein-lysine deacetylase, desuccinylase, de-2-hydroxyisobutyrylase, delactylase and lipoamidase CobB is a Class III sirtuin, a broadly conserved family of NAD+-dependent protein deacetylases. CobB deacetylates acetylated ACS-MONOMER "acetyl-CoA synthetase" and the acetylated chemotaxis response regulator CHEY-MONOMER CheY in vitro. Additional potential substrates for CobB were identified and include CPLX0-236 NhoA , RCSB-MONOMER RcsB and EG10900-MONOMER . The acetylation level of the Lys501 residue in EG11620-MONOMER RNase II, which is controlled by CobB and PatZ, regulates RNase II activity . Deacetylation of S-ADENMETSYN-MONOMER and PD03831 DnaA by CobB may regulate their activities. Acetylated lysine residues of PDXH-MONOMER , MALATE-DEHASE , EG11013-MONOMER , LEUS-MONOMER, ARGS-MONOMER , TYRS-CPLX , ALAS-CPLX alanine—tRNA ligase , THRS-CPLX , ISOCITDEH-SUBUNIT , CITRATE-SI-SYNTHASE , EG11643-MONOMER, and EG10270-MONOMER can be deacetylated by CobB in vitro. 69 acetyllysine residues on 51 proteins were identified as CobB substrates . A proteome microarray was used to identify 183 proteins that interact with CobB . CobB can deacetylate both enzymatically and non-enzymatically acetylated proteins. Acetyllysine residues that are substrates for CobB tend to be surface-exposed and adjacent to alanine, glycine, tyrosine, and negatively charged resides . The acetylome of cobB and patZ mutants has been determined under four different growth conditions ; additional proteome-scale datasets have been published . Metabolic differences between the E. coli B and K-12 strains that may involve peptidyl-lysine acetylation have been investigated . Proteome-wide lysine propionylation was compared between wild-type and a cobB mutant, leading to the identification of 13 sites that

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-22964|reaction.ecocyc.RXN-22964]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6445|reaction.ecocyc.RXN0-6445]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7078|reaction.ecocyc.RXN0-7078]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P75960|protein.P75960]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8550`
- `QSPROTEOME:QS00196987`

## Notes

2*protein.P75960
