---
entity_id: "protein.P09835"
entity_type: "protein"
name: "uhpB"
source_database: "UniProt"
source_id: "P09835"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uhpB b3668 JW3643"
---

# uhpB

`protein.P09835`

## Static

- Type: `protein`
- Source: `UniProt:P09835`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the UhpABC signaling cascade that controls the expression of the hexose phosphate transporter UhpT. UhpB functions as a membrane-associated protein kinase that autophosphorylates in response to interaction with UhpC, and subsequently transfers its phosphate group to the response regulator UhpA (PubMed:11053370, PubMed:11739766, PubMed:3038843, PubMed:8349544). Can also dephosphorylate UhpA (PubMed:11053370, PubMed:11739766). {ECO:0000269|PubMed:11053370, ECO:0000269|PubMed:11739766, ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:8349544}. This is the phosphorylated form of UHPB-MONOMER UhpB - the sensor histidine kinase of the UhpBA two-component signal transduction system. UhpB belongs to the phosphorelay system UhpB-UhpC-UhpA which is involved in the regulation of the uptake of hexose phosphates. UhpB is a membrane bound histidine kinase with eight predicted transmembrane helices and a C-terminal cytoplasmic domain containing the characteristic histidine kinase sequence motifs . UhpB autophosphorylates on a conserved histidine residue (His313) and transfers the phosphoryl group its cognate response regulator, UhpA . The Uhp signal transduction system is responsible for sensing and transport of the metabolic intermediate, glucose-6-phosphate...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the UhpABC signaling cascade that controls the expression of the hexose phosphate transporter UhpT. UhpB functions as a membrane-associated protein kinase that autophosphorylates in response to interaction with UhpC, and subsequently transfers its phosphate group to the response regulator UhpA (PubMed:11053370, PubMed:11739766, PubMed:3038843, PubMed:8349544). Can also dephosphorylate UhpA (PubMed:11053370, PubMed:11739766). {ECO:0000269|PubMed:11053370, ECO:0000269|PubMed:11739766, ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:8349544}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3668|gene.b3668]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09835`
- `KEGG:ecj:JW3643;eco:b3668;ecoc:C3026_19880;`
- `GeneID:75205382;948195;`
- `GO:GO:0000155; GO:0004721; GO:0005524; GO:0005886; GO:0007165; GO:0046983`
- `EC:2.7.13.3; 3.1.3.-`

## Notes

Signal transduction histidine-protein kinase/phosphatase UhpB (EC 2.7.13.3) (EC 3.1.3.-)
