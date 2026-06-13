---
entity_id: "protein.P77211"
entity_type: "protein"
name: "cusC"
source_database: "UniProt"
source_id: "P77211"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:21249122}; Multi-pass membrane protein {ECO:0000269|PubMed:21249122}. Cell outer membrane {ECO:0000269|PubMed:21249122}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303, ECO:0000269|PubMed:21249122}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cusC ibeB ylcB b0572 JW0561"
---

# cusC

`protein.P77211`

## Static

- Type: `protein`
- Source: `UniProt:P77211`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:21249122}; Multi-pass membrane protein {ECO:0000269|PubMed:21249122}. Cell outer membrane {ECO:0000269|PubMed:21249122}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303, ECO:0000269|PubMed:21249122}.

## Enriched Summary

FUNCTION: Forms pores that allow passive diffusion of cations across the outer membrane. Part of a cation efflux system that mediates resistance to copper and silver. In pathogenic strains it allows the bacteria to invade brain microvascular endothelial cells (BMEC) thus allowing it to cross the blood-brain barrier and cause neonatal meningitis. {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:12813074, ECO:0000269|PubMed:21249122}. CusC is an outer membrane lipoprotein involved in the detoxification of copper and silver ions in E. coli as part of the CusCFBA copper/silver efflux system. A crystal structure of CusC has been solved to 2.3 Å. The CusC trimer forms a large continuous internal cavity with a cylindrical shape. Each monomer contributes 4 β strands to the outer membrane β barrel structure and 4 α helices to the periplasmic α barrel. The structure also suggests that CusC is triacylated at the N-terminal cysteine residue of each monomer . cusC exhibits mosaic evolution patterns in E. coli .

## Biological Role

Component of copper/silver export system (complex.ecocyc.CPLX0-1721).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Forms pores that allow passive diffusion of cations across the outer membrane. Part of a cation efflux system that mediates resistance to copper and silver. In pathogenic strains it allows the bacteria to invade brain microvascular endothelial cells (BMEC) thus allowing it to cross the blood-brain barrier and cause neonatal meningitis. {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:12813074, ECO:0000269|PubMed:21249122}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1721|complex.ecocyc.CPLX0-1721]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0572|gene.b0572]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77211`
- `KEGG:ecj:JW0561;eco:b0572;ecoc:C3026_02840;`
- `GeneID:946288;`
- `GO:GO:0005375; GO:0005507; GO:0006878; GO:0009279; GO:0009636; GO:0010272; GO:0010273; GO:0015288; GO:0015562; GO:0016020; GO:0019992; GO:0022857; GO:0035434; GO:0042802; GO:0046688; GO:0046930; GO:0055085; GO:0060003; GO:0070207; GO:1902601`

## Notes

Cation efflux system protein CusC
