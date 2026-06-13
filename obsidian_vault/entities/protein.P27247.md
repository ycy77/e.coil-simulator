---
entity_id: "protein.P27247"
entity_type: "protein"
name: "plsX"
source_database: "UniProt"
source_id: "P27247"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm. Note=Associated with the membrane possibly through PlsY. {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "plsX b1090 JW5156"
---

# plsX

`protein.P27247`

## Static

- Type: `protein`
- Source: `UniProt:P27247`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm. Note=Associated with the membrane possibly through PlsY. {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the reversible formation of acyl-phosphate (acyl-PO(4)) from acyl-[acyl-carrier-protein] (acyl-ACP). This enzyme utilizes acyl-ACP as fatty acyl donor, but not acyl-CoA. {ECO:0000255|HAMAP-Rule:MF_00019, ECO:0000269|PubMed:17645809}. PlsX, together with EG11674-MONOMER PlsY, can substitute for GLYCEROL-3-P-ACYLTRANSFER-MONOMER (PlsB) in synthesis of 2-Acyl-sn-glycerol-3-phosphates required for initiation of phospholipid synthesis and fine-tune the levels of other lipids involved in the structure of the cell envelope . Most Gram-negative proteobacteria have both the PlsX/PlsY and PlsB systems . The transcript levels and operon structure of plsX have been analyzed . A mutation in plsX is required for the sn-glycerol-3-phosphate auxotrophic phenotype of a plsB mutant strain . A plsX plsY double deletion is lethal . Yoshimura et al. hypothesize that PlsX and PlsY play a role in regulating the intracellular concentration of acyl-ACP . Using a suppressor screen approach, the plsX plsY double deletion synthetic lethality was confirmed, and rescue of this phenotype required increased levels of G3P that could be obtained through secondary mutations, such as in EG10400...

## Biological Role

Catalyzes RXN-9590 (reaction.ecocyc.RXN-9590).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible formation of acyl-phosphate (acyl-PO(4)) from acyl-[acyl-carrier-protein] (acyl-ACP). This enzyme utilizes acyl-ACP as fatty acyl donor, but not acyl-CoA. {ECO:0000255|HAMAP-Rule:MF_00019, ECO:0000269|PubMed:17645809}.

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-9590|reaction.ecocyc.RXN-9590]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1090|gene.b1090]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27247`
- `KEGG:ecj:JW5156;eco:b1090;`
- `GeneID:946165;`
- `GO:GO:0005737; GO:0006633; GO:0008654; GO:0042304; GO:0043811; GO:0055088`
- `EC:2.3.1.274`

## Notes

Phosphate acyltransferase (EC 2.3.1.274) (Acyl-ACP phosphotransacylase) (Acyl-[acyl-carrier-protein]--phosphate acyltransferase) (Phosphate-acyl-ACP acyltransferase)
