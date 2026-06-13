---
entity_id: "protein.P77239"
entity_type: "protein"
name: "cusB"
source_database: "UniProt"
source_id: "P77239"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cusB ylcD b0574 JW0563"
---

# cusB

`protein.P77239`

## Static

- Type: `protein`
- Source: `UniProt:P77239`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of a cation efflux system that mediates resistance to copper and silver. {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:12813074}. CusB is a membrane fusion protein involved in the detoxification of copper and silver ions in E. coli as part of the CusCFBA copper/silver efflux system. CusB is monomeric in solution . Three methionine residues (M21, M36, M38) ligate the metal substrate in a 1:1 stoichiometry . Crystal structures of CusB in the absence and presence of silver and copper ions have been described; CusB consists of 4 major domains: 3 β-strand domains and one α-helical domain; two distinct conformations of CusB were found in single crystals suggesting that CusB exhibits conformational flexibility . The function of a membrane fusion protein like CusB may be to bring the outer membrane factor, CusC, closer to the resistance-nodulation-division permease, CusA, consistent with the 'funnel' model of efflux. Alternatively CusB may act as a switch whereby metal binding to CusB promotes opening of a CusA channel and docking of substrate-loaded CusF (reviewed in ). Using selenomethionine labeling of active site methionine residues provide in vitro evidence that loaded CusB activates CusA to accept copper from CusF...

## Biological Role

Component of copper/silver export system (complex.ecocyc.CPLX0-1721).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of a cation efflux system that mediates resistance to copper and silver. {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:12813074}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1721|complex.ecocyc.CPLX0-1721]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6 | EcoCyc transporter component coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0574|gene.b0574]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77239`
- `KEGG:ecj:JW0563;eco:b0574;ecoc:C3026_02850;`
- `GeneID:945189;`
- `GO:GO:0005375; GO:0005507; GO:0006878; GO:0009636; GO:0010272; GO:0010273; GO:0015679; GO:0016020; GO:0030288; GO:0030313; GO:0035434; GO:0046688; GO:0046914; GO:0060003; GO:1902601`

## Notes

Cation efflux system protein CusB
