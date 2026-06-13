---
entity_id: "protein.P0ACS9"
entity_type: "protein"
name: "acrR"
source_database: "UniProt"
source_id: "P0ACS9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acrR ybaH b0464 JW0453"
---

# acrR

`protein.P0ACS9`

## Static

- Type: `protein`
- Source: `UniProt:P0ACS9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Potential regulator protein for the acrAB genes. The "acriflavine resistance regulator," AcrR, is classified in the nodulation-resistance division family and regulates the expression of genes involved in multidrug transport . It appears to be involved in resistance to ciprofloxacin , cefuroxime, gentamicin, and pyocyanin . This protein also regulates genes that contend with polyamine toxicity . In addition, AcrR acts as a global repressor for the mar-sox-rob regulon . Consistent with a broader in vivo principle observed for many transcription factors (including AcrR), TF action can primarily stabilize RNAP at promoters even when the net outcome is repression; accordingly, AcrR-dependent fold-changes scale approximately with the reciprocal of promoter constitutive (basal) activity and can buffer promoter-to-promoter variability, so AcrR-regulated promoters tend to converge toward more similar expression levels across diverse promoter contexts and perturbations . The crystal structure of AcrR shows that this protein is folded into nine α-helices distributed in two domains: the DNA-binding domain, which forms the typical helix-turn-helix in the N-terminal domain, and the ligand-binding domain, which forms a large internal cavity for multidrug binding in the C-terminal domain...

## Biological Role

Component of AcrR-ethidium (complex.ecocyc.CPLX0-8055), AcrR-3,6-diaminoacridine (complex.ecocyc.CPLX0-8952), AcrR-rhodamine 6G (complex.ecocyc.CPLX0-8953), AcrR-putrescine (complex.ecocyc.CPLX0-9742), AcrR-cadaverine (complex.ecocyc.CPLX0-9743), AcrR-spermidine (complex.ecocyc.CPLX0-9744), AcrR-ethidium bromide (complex.ecocyc.CPLX0-9750).

## Annotation

FUNCTION: Potential regulator protein for the acrAB genes.

## Outgoing Edges (15)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8055|complex.ecocyc.CPLX0-8055]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8952|complex.ecocyc.CPLX0-8952]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8953|complex.ecocyc.CPLX0-8953]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-9742|complex.ecocyc.CPLX0-9742]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-9743|complex.ecocyc.CPLX0-9743]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-9744|complex.ecocyc.CPLX0-9744]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-9750|complex.ecocyc.CPLX0-9750]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0462|gene.b0462]] `RegulonDB` `C` - regulator=AcrR; target=acrB; function=-
- `represses` --> [[gene.b0463|gene.b0463]] `RegulonDB` `C` - regulator=AcrR; target=acrA; function=-
- `represses` --> [[gene.b0464|gene.b0464]] `RegulonDB` `C` - regulator=AcrR; target=acrR; function=-
- `represses` --> [[gene.b1530|gene.b1530]] `RegulonDB` `S` - regulator=AcrR; target=marR; function=-
- `represses` --> [[gene.b1531|gene.b1531]] `RegulonDB` `S` - regulator=AcrR; target=marA; function=-
- `represses` --> [[gene.b1532|gene.b1532]] `RegulonDB` `S` - regulator=AcrR; target=marB; function=-
- `represses` --> [[gene.b4062|gene.b4062]] `RegulonDB` `S` - regulator=AcrR; target=soxS; function=-
- `represses` --> [[gene.b4063|gene.b4063]] `RegulonDB` `S` - regulator=AcrR; target=soxR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0464|gene.b0464]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACS9`
- `KEGG:ecj:JW0453;eco:b0464;ecoc:C3026_02275;`
- `GeneID:93776986;945516;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0009410; GO:0015643; GO:0043565; GO:0045892`

## Notes

HTH-type transcriptional regulator AcrR (Potential acrAB operon repressor)
