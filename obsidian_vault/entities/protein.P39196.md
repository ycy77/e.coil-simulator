---
entity_id: "protein.P39196"
entity_type: "protein"
name: "lplT"
source_database: "UniProt"
source_id: "P39196"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lplT ygeD b2835 JW2803"
---

# lplT

`protein.P39196`

## Static

- Type: `protein`
- Source: `UniProt:P39196`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Catalyzes the facilitated diffusion of 2-acyl-glycero-3-phosphoethanolamine (2-acyl-GPE) into the cell. {ECO:0000269|PubMed:15661733}. LplT is a phospholipid flippase that catalyses the facilitated diffusion of lysophospholipid across the inner membrane bilayer. LplT functions to reutilize 2-acylglycerophosphoethanolamine (2-acyl-GPE) that is generated in the periplasm during the maturation of the major outer membrane lipoprotein (Lpp); LplT import provides substrate for the AAS-MONOMER "Aas" catalysed 2-acyl-GPE acyltransferase reaction . lplT forms an operon with aas . LplT interacts directly with Aas; LplT and Aas form a functional complex in vivo which facilitates specific and efficient reacylation of lysophospholipids . LplT/Aas function plays a role in the resistance of gram-negative bacteria to mammalian secretory phospholipase A2 (sPLA2) . In a ΔfadD background, loss of lplT results in significant accumulation of acyl-GPE . E. coli ΔlplT and ΔlplTΔaas strains have perturbed phospholipid composition resulting in membrane destabilization; the strains show reduced PE and PG levels accompanied by an increase in lysophospholipids and in cardiolipin levels . E...

## Biological Role

Catalyzes TRANS-RXN-294 (reaction.ecocyc.TRANS-RXN-294), TRANS-RXN-295 (reaction.ecocyc.TRANS-RXN-295), TRANS-RXN-387 (reaction.ecocyc.TRANS-RXN-387).

## Annotation

FUNCTION: Catalyzes the facilitated diffusion of 2-acyl-glycero-3-phosphoethanolamine (2-acyl-GPE) into the cell. {ECO:0000269|PubMed:15661733}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-294|reaction.ecocyc.TRANS-RXN-294]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-295|reaction.ecocyc.TRANS-RXN-295]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-387|reaction.ecocyc.TRANS-RXN-387]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2835|gene.b2835]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39196`
- `KEGG:ecj:JW2803;eco:b2835;ecoc:C3026_15570;`
- `GeneID:947317;`
- `GO:GO:0005886; GO:0006650; GO:0019899; GO:0045332; GO:0051978; GO:0140329`

## Notes

Lysophospholipid transporter LplT
