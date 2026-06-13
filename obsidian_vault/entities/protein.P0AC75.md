---
entity_id: "protein.P0AC75"
entity_type: "protein"
name: "waaA"
source_database: "UniProt"
source_id: "P0AC75"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:1577828}; Single-pass membrane protein {ECO:0000305|PubMed:1577828}; Cytoplasmic side {ECO:0000305|PubMed:1577828}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaA kdtA b3633 JW3608"
---

# waaA

`protein.P0AC75`

## Static

- Type: `protein`
- Source: `UniProt:P0AC75`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:1577828}; Single-pass membrane protein {ECO:0000305|PubMed:1577828}; Cytoplasmic side {ECO:0000305|PubMed:1577828}.

## Enriched Summary

FUNCTION: Involved in lipopolysaccharide (LPS) biosynthesis. Catalyzes the transfer of two 3-deoxy-D-manno-octulosonate (Kdo) residues from CMP-Kdo to lipid IV(A), the tetraacyldisaccharide-1,4'-bisphosphate precursor of lipid A. {ECO:0000269|PubMed:10951204, ECO:0000269|PubMed:1577828}. 3-deoxy-D-manno-octulosonic acid (KDO) transferase (KdtA, WaaA) plays a key role in lipopolysaccharide biosynthesis. The enzyme is a single bifunctional polypeptide that incorporates the two innermost KDO residues into lipid IVA, the lipid A precursor. The KDO residues are transferred in two sequential steps . KDO transferase is an integral membrane protein . The N-terminal domain of WaaA determines the bifunctionality of E.coli WaaA which is in contrast to the KDO transferase of Haemophilus influenzae which adds only one KDO residue to Lipid A . KDO transferase is encoded by kdta (waaA) which has been sequenced, cloned and the gene product overexpressed . Deletion of kdtA resulted in highly attenuated growth, accumulation of free lipid IVA precursors, constitutively elevated levels of periplasmic protease HtrA, and severe membrane and cell division defects . KdtA is regulated by FtsH which is an ATP-dependent protease. Proteolysis of both KdtA and LpxC by FtsH ensures the regulation of both the lipid and sugar moiety of LPS. Reviews:

## Biological Role

Catalyzes CMP-3-deoxy-D-manno-oct-2-ulosonate:lipid IVA 3-deoxy-D-manno-oct-2-ulosonate transferase (reaction.R04658), KDOTRANS-RXN (reaction.ecocyc.KDOTRANS-RXN), KDOTRANS2-RXN (reaction.ecocyc.KDOTRANS2-RXN).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in lipopolysaccharide (LPS) biosynthesis. Catalyzes the transfer of two 3-deoxy-D-manno-octulosonate (Kdo) residues from CMP-Kdo to lipid IV(A), the tetraacyldisaccharide-1,4'-bisphosphate precursor of lipid A. {ECO:0000269|PubMed:10951204, ECO:0000269|PubMed:1577828}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R04658|reaction.R04658]] `KEGG` `database` - via EC:2.4.99.12
- `catalyzes` --> [[reaction.ecocyc.KDOTRANS-RXN|reaction.ecocyc.KDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.KDOTRANS2-RXN|reaction.ecocyc.KDOTRANS2-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3633|gene.b3633]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC75`
- `KEGG:ecj:JW3608;eco:b3633;ecoc:C3026_19690;`
- `GeneID:93778346;949048;`
- `GO:GO:0005886; GO:0009244; GO:0009245; GO:0016020; GO:0016740; GO:0036104; GO:0043842`
- `EC:2.4.99.12; 2.4.99.13`

## Notes

3-deoxy-D-manno-octulosonic acid transferase (Kdo transferase) (EC 2.4.99.12) (EC 2.4.99.13) (Bifunctional Kdo transferase) (Kdo-lipid IV(A) 3-deoxy-D-manno-octulosonic acid transferase) (Lipid IV(A) 3-deoxy-D-manno-octulosonic acid transferase)
