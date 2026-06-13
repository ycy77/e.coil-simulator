---
entity_id: "protein.P0ACL7"
entity_type: "protein"
name: "lldR"
source_database: "UniProt"
source_id: "P0ACL7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lldR lctR b3604 JW3579"
---

# lldR

`protein.P0ACL7`

## Static

- Type: `protein`
- Source: `UniProt:P0ACL7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May be a regulatory protein for the LCT genes. LldR, formerly named "lactate regulator," is a transcription factor that controls expression of genes involved in transport and catabolism of L-lactate and genes involved in acid stress . This regulator has a dual function and is positively and negatively autoregulated. In the absence of L-lactate and under anaerobic conditions, this regulator represses the transcription of the lldPRD operon . In this repression system, LldR binds to two operators and probably leads to repressor DNA looping . Expression of this regulator is also stimulated in the presence of L-lactate, and this inductor promotes a conformational change that probably destabilizes the DNA loop, promoting the transcription open complex . Both L-lactate and D-lactate are able to bind to LldR to regulate its activity . At a low concentration of the effector, LldR binds to the target sequence, but at high concentration it is dissociated . The affinity of LldR is greater in the lldPRD operon regulatory region than in other targets (genes related to acid stress) of this regulator . This fact suggests that at low concentrations of lactate, the effector of LldR, the lactate is used as a carbon source, but when the concentration increases, the role of LldR is to cope with the acid stress...

## Biological Role

Component of DNA-binding transcriptional dual regulator LldR-S-lactate (complex.ecocyc.CPLX0-7689).

## Annotation

FUNCTION: May be a regulatory protein for the LCT genes.

## Outgoing Edges (7)

- `activates` --> [[gene.b3603|gene.b3603]] `RegulonDB` `C` - regulator=LldR; target=lldP; function=-+
- `activates` --> [[gene.b3604|gene.b3604]] `RegulonDB` `C` - regulator=LldR; target=lldR; function=-+
- `activates` --> [[gene.b3605|gene.b3605]] `RegulonDB` `C` - regulator=LldR; target=lldD; function=-+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7689|complex.ecocyc.CPLX0-7689]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3603|gene.b3603]] `RegulonDB` `C` - regulator=LldR; target=lldP; function=-+
- `represses` --> [[gene.b3604|gene.b3604]] `RegulonDB` `C` - regulator=LldR; target=lldR; function=-+
- `represses` --> [[gene.b3605|gene.b3605]] `RegulonDB` `C` - regulator=LldR; target=lldD; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b3604|gene.b3604]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACL7`
- `KEGG:ecj:JW3579;eco:b3604;ecoc:C3026_19545;`
- `GeneID:93778318;948122;`
- `GO:GO:0000987; GO:0001216; GO:0001217; GO:0003700; GO:0006355; GO:0006974; GO:0044010; GO:2000143; GO:2000144`

## Notes

Putative L-lactate dehydrogenase operon regulatory protein
