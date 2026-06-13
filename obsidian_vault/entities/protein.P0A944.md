---
entity_id: "protein.P0A944"
entity_type: "protein"
name: "rimI"
source_database: "UniProt"
source_id: "P0A944"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02210, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rimI b4373 JW4335"
---

# rimI

`protein.P0A944`

## Static

- Type: `protein`
- Source: `UniProt:P0A944`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02210, ECO:0000305}.

## Enriched Summary

FUNCTION: Acetylates the N-terminal alanine of ribosomal protein bS18 (PubMed:2828880, PubMed:6991870). Also acts as a N-epsilon-lysine acetyltransferase that catalyzes acetylation of several proteins (PubMed:30352934). {ECO:0000269|PubMed:2828880, ECO:0000269|PubMed:30352934, ECO:0000269|PubMed:6991870}. RimI is an alanine acetyltransferase that is specific for EG10917-MONOMER . It also functions as an Nε-lysine acetyltransferase that targets 14 unique lysine residues in 11 unique proteins . A rimI mutant exhibits a defect in acetylation of the N-terminal alanine of ribosomal protein S18, but shows no defect in acetylation of ribosomal proteins S5 or L12 . Overexpression of RimI in an acetylation-gutted strain (Δ pta patZ acs cobB) leads to the appearance of acetylated proteins in an anti-acetyllysine Western blot. Mutagenesis of a predicted catalytic residue in RimI, Y115A, eliminates the acetylation signal observed with the wild-type protein . RimI and RimJ share C-terminal similarity .

## Biological Role

Catalyzes 2.3.1.128-RXN (reaction.ecocyc.2.3.1.128-RXN), RXN0-7160 (reaction.ecocyc.RXN0-7160).

## Annotation

FUNCTION: Acetylates the N-terminal alanine of ribosomal protein bS18 (PubMed:2828880, PubMed:6991870). Also acts as a N-epsilon-lysine acetyltransferase that catalyzes acetylation of several proteins (PubMed:30352934). {ECO:0000269|PubMed:2828880, ECO:0000269|PubMed:30352934, ECO:0000269|PubMed:6991870}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.2.3.1.128-RXN|reaction.ecocyc.2.3.1.128-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7160|reaction.ecocyc.RXN0-7160]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4373|gene.b4373]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A944`
- `KEGG:ecj:JW4335;eco:b4373;ecoc:C3026_23625;`
- `GeneID:75169867;75202945;948894;`
- `GO:GO:0005737; GO:0008080; GO:0008999; GO:0061733`
- `EC:2.3.1.-; 2.3.1.266`

## Notes

[Ribosomal protein bS18]-alanine N-acetyltransferase (EC 2.3.1.266) (KAT) (Peptidyl-lysine N-acetyltransferase) (EC 2.3.1.-)
