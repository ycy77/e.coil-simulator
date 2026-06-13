---
entity_id: "protein.P11290"
entity_type: "protein"
name: "yibD"
source_database: "UniProt"
source_id: "P11290"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yibD b3615 JW3590"
---

# yibD

`protein.P11290`

## Static

- Type: `protein`
- Source: `UniProt:P11290`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized glycosyltransferase YibD (EC 2.4.-.-) WaaH is a glucuronic acid transferase involved in modification of the core oligosaccharide in E. coli K-12. WaaH catalyses the addition of glucuronic acid to the third heptose of the inner core oligosaccharide . This modified lipopolysaccharide (LPS) is produced when E. coli is grown under phosphate limiting conditions with sub millimolar concentrations of Zn2+ and Fe3+ . The glucuronic acid modification coincides with the absence of phosphate on the second heptose, is absent in the LPS of waaC, waaO, waaP, waaG or waaQ deletion mutants but can be identified in waaR and waaB deletion mutants . The LPS of a phoB deletion mutant does not contain glucuronic acid . WaaH is membrane associated . Structural analysis of the modified LPS indicates that a β-glucuronate residue is attached to the O7 atom of the side chain heptose (heptose III) . Transcription of a waaH-lacZ promoter fusion is induced by growth in phosphate limited medium and abolished in a phoB deleted strain but not in a basR deleted strain . Two PhoB binding sites are located directly upstream of the waaH gene . Transcription of a ugd-lacZ promoter fusion is also induced by growth in phosphate limited medium - (UGD-MONOMER catalyses the production of the nucleotide sugar UDP-glucuronate). waaH levels are increased 2...

## Biological Role

Catalyzes RXN-14361 (reaction.ecocyc.RXN-14361).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

Uncharacterized glycosyltransferase YibD (EC 2.4.-.-)

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-14361|reaction.ecocyc.RXN-14361]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3615|gene.b3615]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11290`
- `KEGG:ecj:JW3590;eco:b3615;ecoc:C3026_19600;`
- `GeneID:948140;`
- `GO:GO:0015020; GO:0016020; GO:0016036`
- `EC:2.4.-.-`

## Notes

Uncharacterized glycosyltransferase YibD (EC 2.4.-.-)
