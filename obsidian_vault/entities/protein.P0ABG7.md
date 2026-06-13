---
entity_id: "protein.P0ABG7"
entity_type: "protein"
name: "mrdB"
source_database: "UniProt"
source_id: "P0ABG7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02079, ECO:0000269|PubMed:6348029, ECO:0000305|PubMed:37620344}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02079, ECO:0000305|PubMed:37620344}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mrdB rodA b0634 JW0629"
---

# mrdB

`protein.P0ABG7`

## Static

- Type: `protein`
- Source: `UniProt:P0ABG7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02079, ECO:0000269|PubMed:6348029, ECO:0000305|PubMed:37620344}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02079, ECO:0000305|PubMed:37620344}.

## Enriched Summary

FUNCTION: Peptidoglycan polymerase that is essential for cell wall elongation (PubMed:27643381, PubMed:37620344). Also required for the maintenance of the rod cell shape (PubMed:2644207). Functions probably in conjunction with the penicillin-binding protein 2 (mrdA) (PubMed:2644207, PubMed:27643381, PubMed:37620344). {ECO:0000269|PubMed:2644207, ECO:0000269|PubMed:27643381, ECO:0000269|PubMed:37620344}. The SEDS family protein MrdB (also called RodA) is believed to be the primary peptidoglycan (PG) glycosyltransferase which functions together with its cognate transpeptidase EG10606-MONOMER "PBP2" (MrdA) to synthesize PG during cell elongation; MrdB-PBP2 are the SEDS-bPBP pair of the elongasome/Rod system. A model of SEDS-bPBP catalysed peptidoglycan synthesis has been generated based on the structural, biochemical, genetic, and computational analyses of a RodA-PBP2 fusion protein . MrdB displays EG10608-MONOMER "MreB"-like directional motion and has been implicated as the core glycosyltransferase of peptidoglycan synthesis during cell elongation . MrdB is a member of the shape, elongation, division and sporulation (SEDS) family of proteins; subcomplexes of SEDS family proteins with class 2 penicillin binding proteins are proposed to be the primary peptidoglycan synthases in cell elongation and division...

## Biological Role

Catalyzes R06177 (reaction.R06177), [poly-N-acetyl-D-glucosaminyl-(1->4)-(N-acetyl-D-muramoylpentapeptide)]-diphosphoundecaprenol:[N-acetyl-D-glucosaminyl-(1->4)-N-acetyl-D-muramoylpentapeptide]-diphosphoundecaprenol polysaccharidetransferase (reaction.R06178), R06179 (reaction.R06179), RXN-16650 (reaction.ecocyc.RXN-16650).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Annotation

FUNCTION: Peptidoglycan polymerase that is essential for cell wall elongation (PubMed:27643381, PubMed:37620344). Also required for the maintenance of the rod cell shape (PubMed:2644207). Functions probably in conjunction with the penicillin-binding protein 2 (mrdA) (PubMed:2644207, PubMed:27643381, PubMed:37620344). {ECO:0000269|PubMed:2644207, ECO:0000269|PubMed:27643381, ECO:0000269|PubMed:37620344}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R06177|reaction.R06177]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06178|reaction.R06178]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06179|reaction.R06179]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0634|gene.b0634]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABG7`
- `KEGG:ecj:JW0629;eco:b0634;ecoc:C3026_03170;`
- `GeneID:93776848;945238;`
- `GO:GO:0005886; GO:0008360; GO:0008955; GO:0009252; GO:0015648; GO:0031504; GO:0032153; GO:0051301`
- `EC:2.4.99.28`

## Notes

Peptidoglycan glycosyltransferase MrdB (PGT) (EC 2.4.99.28) (Cell elongation protein RodA) (Cell wall polymerase) (Peptidoglycan polymerase) (PG polymerase) (Rod shape-determining protein) (Shape, elongation, division and sporulation glycosyltransferase RodA) (SEDS GT RodA)
