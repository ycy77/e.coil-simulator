---
entity_id: "protein.P0A6F3"
entity_type: "protein"
name: "glpK"
source_database: "UniProt"
source_id: "P0A6F3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpK b3926 JW3897"
---

# glpK

`protein.P0A6F3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6F3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Key enzyme in the regulation of glycerol uptake and metabolism. Catalyzes the phosphorylation of glycerol to yield sn-glycerol 3-phosphate. It also catalyzes the phosphorylation of dihydroxyacetone, L-glyceraldehyde and D-glyceraldehyde. It uses only ATP. {ECO:0000255|HAMAP-Rule:MF_00186, ECO:0000269|PubMed:2826434, ECO:0000269|PubMed:4575199, ECO:0000269|PubMed:5335908}. Glycerol kinase (GlpK) is involved in the utilization of the glycerol moiety of phospholipids and triglycerides after their breakdown into usable forms such as glycerophosphodiesters, sn-glycerol-3-phosphate (G3P) or glycerol. GlpK catalyzes the MgATP-dependent phosphorylation of glycerol to yield sn-glycerol 3-phosphate . This reaction is the rate-limiting step in glycerol utilization . GlpK is a member of a superfamily of proteins that share a common ATPase domain . Inhibition studies suggested an ordered catalytic mechanism, with glycerol binding first , but later experiments support a random catalytic mechanism . The crystal structure of a putative productive conformation of the enzyme is consistent with "half-of-the-sites" reactivity and the importance of domain motion for catalytic activity . A nucleophilic in-line transfer mechanism for the kinase reaction has been proposed...

## Biological Role

Catalyzes ATP:glycerol 3-phosphotransferase (reaction.R00847). Component of glycerol kinase (complex.ecocyc.GLYCEROL-KIN-CPLX).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Key enzyme in the regulation of glycerol uptake and metabolism. Catalyzes the phosphorylation of glycerol to yield sn-glycerol 3-phosphate. It also catalyzes the phosphorylation of dihydroxyacetone, L-glyceraldehyde and D-glyceraldehyde. It uses only ATP. {ECO:0000255|HAMAP-Rule:MF_00186, ECO:0000269|PubMed:2826434, ECO:0000269|PubMed:4575199, ECO:0000269|PubMed:5335908}.

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00847|reaction.R00847]] `KEGG` `database` - via EC:2.7.1.30
- `is_component_of` --> [[complex.ecocyc.GLYCEROL-KIN-CPLX|complex.ecocyc.GLYCEROL-KIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3926|gene.b3926]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6F3`
- `KEGG:ecj:JW3897;eco:b3926;ecoc:C3026_21220;`
- `GeneID:75169366;948423;`
- `GO:GO:0004370; GO:0005524; GO:0005829; GO:0006071; GO:0006072; GO:0006974; GO:0008270; GO:0019563; GO:0042802; GO:0046872`
- `EC:2.7.1.30`

## Notes

Glycerol kinase (EC 2.7.1.30) (ATP:glycerol 3-phosphotransferase) (Glycerokinase) (GK)
