---
entity_id: "protein.P69490"
entity_type: "protein"
name: "ccmE"
source_database: "UniProt"
source_id: "P69490"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01959}; Single-pass type II membrane protein {ECO:0000255|HAMAP-Rule:MF_01959}; Periplasmic side {ECO:0000255|HAMAP-Rule:MF_01959}. Note=Stabilized by CcmD in the membrane."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ccmE yejS b2197 JW2185"
---

# ccmE

`protein.P69490`

## Static

- Type: `protein`
- Source: `UniProt:P69490`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01959}; Single-pass type II membrane protein {ECO:0000255|HAMAP-Rule:MF_01959}; Periplasmic side {ECO:0000255|HAMAP-Rule:MF_01959}. Note=Stabilized by CcmD in the membrane.

## Enriched Summary

FUNCTION: Heme chaperone required for the biogenesis of c-type cytochromes. Transiently binds heme delivered by CcmC and transfers the heme to apo-cytochromes in a process facilitated by CcmF and CcmH. CcmE is a membrane anchored, periplasmic heme chaperone that is required for PWY-8147 "cytochrome c biogenesis". ccmE is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmE deletion mutant cannot produce mature c-type cytochromes ; CcmE binds heme covalently via a conserved histidine residue (His-30) . Heme ligation in CcmE exhibits flexibility and it has been extensively studied (see ). The presence of apocytochrome c triggers release of heme from CcmE; heme release is blocked in the absence of CcmFGH (see also ). During cyctochrome c biosynthesis, heme is moved across the inner membrane concomitant with the formation of a CcmC-heme-CcmE-CcmD complex; subsequent release of holo-CcmE (for eventual heme transfer to apocytochromes c) requires CcmAB-Complex CcmAB-mediated ATP hydolysis...

## Biological Role

Component of CcmCDE complex (complex.ecocyc.ABC-35-CPLX).

## Annotation

FUNCTION: Heme chaperone required for the biogenesis of c-type cytochromes. Transiently binds heme delivered by CcmC and transfers the heme to apo-cytochromes in a process facilitated by CcmF and CcmH.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-35-CPLX|complex.ecocyc.ABC-35-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2197|gene.b2197]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69490`
- `KEGG:ecj:JW2185;eco:b2197;ecoc:C3026_12280;`
- `GeneID:86860369;946697;`
- `GO:GO:0017003; GO:0017004; GO:0020037; GO:0043190; GO:0046872; GO:1903607; GO:1904334`

## Notes

Cytochrome c-type biogenesis protein CcmE (Cytochrome c maturation protein E) (Heme chaperone CcmE)
