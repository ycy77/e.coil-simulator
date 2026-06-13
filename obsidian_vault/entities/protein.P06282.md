---
entity_id: "protein.P06282"
entity_type: "protein"
name: "cdh"
source_database: "UniProt"
source_id: "P06282"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Single-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cdh b3918 JW3889"
---

# cdh

`protein.P06282`

## Static

- Type: `protein`
- Source: `UniProt:P06282`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Single-pass membrane protein.

## Enriched Summary

CDP-diacylglycerol pyrophosphatase (EC 3.6.1.26) (CDP-diacylglycerol phosphatidylhydrolase) (CDP-diglyceride hydrolase) CDP-diacylglycerol pyrophosphatase (Cdh) catalyzes the hydrolysis of CDP-diacylglycerol . The enzyme can also catalyze the transfer of the CMP or dCMP moiety from (d)CDP-diacylglycerol to phosphate or a variety of phosphomonoesters . The true in vivo role of the enzyme is not known. Cdh is not required for lipid A biosynthesis in vivo. While the protein has UDP-2,3-diacylglucosamine pyrophosphatase activity in vitro and interferes with the assay of EG12666-MONOMER "LpxH" activity in crude cell extracts, the active site of the protein may be localized in the periplasm, explaining why it plays no role in the cytoplasmic steps of lipid A biosynthetic . were unable to detect Cdh protein and suggested that the protein is rapidly degraded in the cell. Cdh is predicted to be a bitopic inner membrane protein . cdh mutants contain elevated levels of CDP-diacylglycerol compared to wild type, but have no obvious growth defect . Cdh: CDP-diacylglycerol hydrolase

## Biological Role

Catalyzes CDPDIGLYPYPHOSPHA-RXN (reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

CDP-diacylglycerol pyrophosphatase (EC 3.6.1.26) (CDP-diacylglycerol phosphatidylhydrolase) (CDP-diglyceride hydrolase)

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN|reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3918|gene.b3918]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06282`
- `KEGG:ecj:JW3889;eco:b3918;ecoc:C3026_21180;`
- `GeneID:948410;`
- `GO:GO:0005886; GO:0008654; GO:0008715; GO:0046342`
- `EC:3.6.1.26`

## Notes

CDP-diacylglycerol pyrophosphatase (EC 3.6.1.26) (CDP-diacylglycerol phosphatidylhydrolase) (CDP-diglyceride hydrolase)
