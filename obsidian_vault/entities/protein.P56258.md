---
entity_id: "protein.P56258"
entity_type: "protein"
name: "wecF"
source_database: "UniProt"
source_id: "P56258"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wecF rffT yifM b4481 JW5596"
---

# wecF

`protein.P56258`

## Static

- Type: `protein`
- Source: `UniProt:P56258`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the synthesis of Und-PP-GlcNAc-ManNAcA-Fuc4NAc (Lipid III), the third lipid-linked intermediate involved in ECA synthesis. {ECO:0000269|PubMed:11673418}. The rffT gene encodes Fuc4NAc (4-acetamido-4,6-dideoxy-D-galactose) transferase, which catalyzes the synthesis of lipid III, the final intermediate in the enterobacterial common antigen (ECA) biosynthetic pathway. Lipid III constitutes the trisaccharide repeat unit of ECA, which is utilized for the synthesis of ECA heteropolysaccharide chains. A rffT mutant exhibits a defect in lipid III biosynthesis . A wecF/rffT mutant exhibits several phenotypes that are indirect effects of outer membrane defects due to buildup of ECA-lipid II, including increased transcription from the degP promoter, sensitivity to LamB or to bile salts, and stimulation of SigmaE and Cpx signaling . A wecF/rffT mutant shows a defect in production of a cyclic form of enterobacterial common antigen that is water-soluble and found in wild type cells . The rff-726 mutation is a rffT allele and exhibits a defect in biosynthesis of ECA-lipid II and lipid III , but does not exhibit a defect in biosynthesis of ECA-lipid I . The rff-726 mutant exhibits a defect in enterobacterial common antigen (ECA) biosynthesis, but shows biosynthesis of ECA intermediates including N-acetyl-D-mannosaminuronic acid...

## Biological Role

Catalyzes FUC4NACTRANS-RXN (reaction.ecocyc.FUC4NACTRANS-RXN).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of Und-PP-GlcNAc-ManNAcA-Fuc4NAc (Lipid III), the third lipid-linked intermediate involved in ECA synthesis. {ECO:0000269|PubMed:11673418}.

## Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.FUC4NACTRANS-RXN|reaction.ecocyc.FUC4NACTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4481|gene.b4481]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P56258`
- `KEGG:ecj:JW5596;eco:b4481;ecoc:C3026_20535;`
- `GeneID:2847677;`
- `GO:GO:0005886; GO:0008417; GO:0009246; GO:0102031`
- `EC:2.4.1.325`

## Notes

TDP-N-acetylfucosamine:lipid II N-acetylfucosaminyltransferase (EC 2.4.1.325) (4-alpha-L-fucosyltransferase) (TDP-Fuc4NAc:lipid II Fuc4NAc transferase) (Fuc4NAc transferase)
