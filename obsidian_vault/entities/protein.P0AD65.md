---
entity_id: "protein.P0AD65"
entity_type: "protein"
name: "mrdA"
source_database: "UniProt"
source_id: "P0AD65"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02081, ECO:0000269|PubMed:1103132, ECO:0000269|PubMed:3009484, ECO:0000305|PubMed:37620344}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02081, ECO:0000305|PubMed:37620344}. Note=Localizes preferentially in the lateral wall and at mid-cell in comparison with the old cell pole. Localization at mid-cell is dependent on active FtsI. {ECO:0000269|PubMed:12519203}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mrdA pbpA b0635 JW0630"
---

# mrdA

`protein.P0AD65`

## Static

- Type: `protein`
- Source: `UniProt:P0AD65`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02081, ECO:0000269|PubMed:1103132, ECO:0000269|PubMed:3009484, ECO:0000305|PubMed:37620344}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02081, ECO:0000305|PubMed:37620344}. Note=Localizes preferentially in the lateral wall and at mid-cell in comparison with the old cell pole. Localization at mid-cell is dependent on active FtsI. {ECO:0000269|PubMed:12519203}.

## Enriched Summary

FUNCTION: Catalyzes cross-linking of the peptidoglycan cell wall (PubMed:3009484). Responsible for the determination of the rod shape of the cell (PubMed:1103132). Is probably required for lateral peptidoglycan synthesis and maintenance of the correct diameter during lateral and centripetal growth (PubMed:12519203). {ECO:0000269|PubMed:1103132, ECO:0000269|PubMed:12519203, ECO:0000269|PubMed:3009484}. Penicillin binding protein 2 (PBP2), the product of the mrdA gene is believed to be the primary peptidoglycan (PG) transpeptidase which functions together with the SEDS family protein EG10607-MONOMER MrdB (RodA) to synthesize PG during cell elongation; MrdB-PBP2 are the SEDS-bPBP pair of the elongasome/Rod system. A model of SEDS-bPBP catalysed peptidoglycan synthesis has been generated based on the structural, biochemical, genetic, and computational analyses of a RodA-PBP2 fusion protein . PBP2 displays EG10608-MONOMER "MreB"-like directional motion and has been implicated as the core transpeptidase of peptidoglycan synthesis during cell elongation . Subcomplexes of class 2 penicillin binding proteins with SEDS (shape, elongation, division and sporulation) family proteins are proposed to be the primary peptidoglycan synthases in cell elongation and division...

## Biological Role

Catalyzes peptidoglycan transpeptidase (Gram-negative bacteria) (reaction.ecocyc.RXN-16659).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Annotation

FUNCTION: Catalyzes cross-linking of the peptidoglycan cell wall (PubMed:3009484). Responsible for the determination of the rod shape of the cell (PubMed:1103132). Is probably required for lateral peptidoglycan synthesis and maintenance of the correct diameter during lateral and centripetal growth (PubMed:12519203). {ECO:0000269|PubMed:1103132, ECO:0000269|PubMed:12519203, ECO:0000269|PubMed:3009484}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-16659|reaction.ecocyc.RXN-16659]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0635|gene.b0635]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD65`
- `KEGG:ecj:JW0630;eco:b0635;ecoc:C3026_03175;`
- `GeneID:75170638;75205004;945240;`
- `GO:GO:0005886; GO:0006508; GO:0008360; GO:0008658; GO:0009002; GO:0009252; GO:0030288; GO:0046677; GO:0071555; GO:0071972`
- `EC:3.4.16.4`

## Notes

Peptidoglycan D,D-transpeptidase MrdA (EC 3.4.16.4) (Class B penicillin-binding protein 2) (Penicillin-binding protein 2) (PBP-2) (PBP2) (Transpeptidase PBP2) (TP PBP2)
