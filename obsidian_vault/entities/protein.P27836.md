---
entity_id: "protein.P27836"
entity_type: "protein"
name: "wecG"
source_database: "UniProt"
source_id: "P27836"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wecG rffM b3794 JW3770"
---

# wecG

`protein.P27836`

## Static

- Type: `protein`
- Source: `UniProt:P27836`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of Und-PP-GlcNAc-ManNAcA (Lipid II), the second lipid-linked intermediate involved in enterobacterial common antigen (ECA) synthesis. {ECO:0000255|HAMAP-Rule:MF_01001, ECO:0000269|PubMed:1730666}. UDP-N-acetyl-D-mannosaminuronic acid transferase (RffM) is involved in the biosynthesis of enterobacterial common antigen (ECA) catalyzing the transfer of Fuc4NAc (4-acetamido-4,6-dideoxy-D-galactose) from TDP-Fuc4NAc to ManNAcA-GlcNAc-pyrophosphorylundecaprenol, also known as ECA-lipid II Mutants of rffM are defective in the synthesis of ECA-lipid II . Strains lacking WecG accumulate ECA intermediates, including novel diacylglycerol pyrophosphoryl (DAG-PP)-linked species . The Keio collection rffM mutant exhibits a 'low level' of resistance to lithium exposure .

## Biological Role

Catalyzes UDPMANACATRANS-RXN (reaction.ecocyc.UDPMANACATRANS-RXN).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of Und-PP-GlcNAc-ManNAcA (Lipid II), the second lipid-linked intermediate involved in enterobacterial common antigen (ECA) synthesis. {ECO:0000255|HAMAP-Rule:MF_01001, ECO:0000269|PubMed:1730666}.

## Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UDPMANACATRANS-RXN|reaction.ecocyc.UDPMANACATRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3794|gene.b3794]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27836`
- `KEGG:ecj:JW3770;eco:b3794;ecoc:C3026_20545;`
- `GeneID:948301;`
- `GO:GO:0009246; GO:0016758; GO:0047241`
- `EC:2.4.1.180`

## Notes

UDP-N-acetyl-D-mannosaminuronic acid transferase (UDP-ManNAcA transferase) (EC 2.4.1.180)
