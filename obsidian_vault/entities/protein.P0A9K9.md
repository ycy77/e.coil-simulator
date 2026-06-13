---
entity_id: "protein.P0A9K9"
entity_type: "protein"
name: "slyD"
source_database: "UniProt"
source_id: "P0A9K9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "slyD b3349 JW3311"
---

# slyD

`protein.P0A9K9`

## Static

- Type: `protein`
- Source: `UniProt:P0A9K9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Folding helper with both chaperone and peptidyl-prolyl cis-trans isomerase (PPIase) activities. Chaperone activity prevents aggregation of unfolded or partially folded proteins and promotes their correct folding. PPIases catalyze the cis-trans isomerization of Xaa-Pro bonds of peptides, which accelerates slow steps of protein folding and thus shortens the lifetime of intermediates. Both strategies lower the concentration of intermediates and increase the productivity and yield of the folding reaction. SlyD could be involved in Tat-dependent translocation, by binding to the Tat-type signal of folded proteins. The PPIase substrate specificity, carried out with synthetic peptides of the 'suc-Ala-Xaa-Pro-Phe-4NA' type (where Xaa is the AA tested), was found to be Phe > Ala > Leu.; FUNCTION: Required for lysis of phiX174 infected cells by stabilizing the hydrophobic viral lysis protein E and allowing it to accumulate to the levels required to exert its lytic effect. May act by a chaperone-like mechanism.; FUNCTION: Also involved in hydrogenase metallocenter assembly, probably by participating in the nickel insertion step. This function in hydrogenase biosynthesis requires chaperone activity and the presence of the metal-binding domain, but not PPIase activity. SlyD is a peptidyl prolyl cis/trans-isomerase (PPIase) and metallochaperone...

## Biological Role

Component of FKBP-type peptidyl-prolyl cis-trans isomerase SlyD (complex.ecocyc.CPLX0-7536).

## Annotation

FUNCTION: Folding helper with both chaperone and peptidyl-prolyl cis-trans isomerase (PPIase) activities. Chaperone activity prevents aggregation of unfolded or partially folded proteins and promotes their correct folding. PPIases catalyze the cis-trans isomerization of Xaa-Pro bonds of peptides, which accelerates slow steps of protein folding and thus shortens the lifetime of intermediates. Both strategies lower the concentration of intermediates and increase the productivity and yield of the folding reaction. SlyD could be involved in Tat-dependent translocation, by binding to the Tat-type signal of folded proteins. The PPIase substrate specificity, carried out with synthetic peptides of the 'suc-Ala-Xaa-Pro-Phe-4NA' type (where Xaa is the AA tested), was found to be Phe > Ala > Leu.; FUNCTION: Required for lysis of phiX174 infected cells by stabilizing the hydrophobic viral lysis protein E and allowing it to accumulate to the levels required to exert its lytic effect. May act by a chaperone-like mechanism.; FUNCTION: Also involved in hydrogenase metallocenter assembly, probably by participating in the nickel insertion step. This function in hydrogenase biosynthesis requires chaperone activity and the presence of the metal-binding domain, but not PPIase activity.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7536|complex.ecocyc.CPLX0-7536]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3349|gene.b3349]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9K9`
- `KEGG:ecj:JW3311;eco:b3349;ecoc:C3026_18185;`
- `GeneID:86948199;93778649;947859;`
- `GO:GO:0003755; GO:0005507; GO:0005829; GO:0008270; GO:0009408; GO:0016151; GO:0042026; GO:0050821; GO:0050897; GO:0051082; GO:0051604`
- `EC:5.2.1.8`

## Notes

FKBP-type peptidyl-prolyl cis-trans isomerase SlyD (PPIase) (EC 5.2.1.8) (Histidine-rich protein) (Metallochaperone SlyD) (Rotamase) (Sensitivity to lysis protein D) (WHP)
