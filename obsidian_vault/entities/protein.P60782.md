---
entity_id: "protein.P60782"
entity_type: "protein"
name: "plsY"
source_database: "UniProt"
source_id: "P60782"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "plsY ygiH b3059 JW3031"
---

# plsY

`protein.P60782`

## Static

- Type: `protein`
- Source: `UniProt:P60782`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Catalyzes the transfer of an acyl group from acyl-ACP to glycerol-3-phosphate (G3P) to form lysophosphatidic acid (LPA). This enzyme can also utilize acyl-CoA as fatty acyl donor, but not acyl-PO(4) (Probable). {ECO:0000305|PubMed:17645809}. PlsY, together with EG11437-MONOMER PlsX, can substitute for GLYCEROL-3-P-ACYLTRANSFER-MONOMER (PlsB) in synthesis of 2-Acyl-sn-glycerol-3-phosphates required for initiation of phospholipid synthesis and fine-tune the levels of other lipids involved in the structure of the cell envelope . Most Gram-negative proteobacteria have both the PlsX/PlsY and PlsB systems . PlsY is an inner membrane protein with five predicted transmembrane domains. The C terminus is located in the cytoplasm . PlsY is similar to the Bacillus subtilis and Streptococcus pneumoniae PlsY proteins, which function as the glycerol-3-phosphate acyltransferase for phospholipid biosynthesis, a function that is filled by PlsB in E. coli. However, a plsX plsY double deletion is lethal . Yoshimura et al. hypothesize that PlsX and PlsY play a role in regulating the intracellular concentration of acyl-ACP . Using a suppressor screen approach, the plsX plsY double deletion synthetic lethality was confirmed, and rescue of this phenotype required increased levels of G3P that could be obtained through secondary mutations, such as in EG10400...

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of an acyl group from acyl-ACP to glycerol-3-phosphate (G3P) to form lysophosphatidic acid (LPA). This enzyme can also utilize acyl-CoA as fatty acyl donor, but not acyl-PO(4) (Probable). {ECO:0000305|PubMed:17645809}.

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3059|gene.b3059]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60782`
- `KEGG:ecj:JW3031;eco:b3059;ecoc:C3026_16715;`
- `GeneID:93778934;947561;`
- `GO:GO:0004366; GO:0005886; GO:0008654; GO:0042304; GO:0043772; GO:0055088`
- `EC:2.3.1.15; 2.3.1.n5`

## Notes

Probable glycerol-3-phosphate acyltransferase (G3P acyltransferase) (GPAT) (EC 2.3.1.15, EC 2.3.1.n5) (Lysophosphatidic acid synthase) (LPA synthase)
