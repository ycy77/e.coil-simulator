---
entity_id: "protein.P76577"
entity_type: "protein"
name: "pbpC"
source_database: "UniProt"
source_id: "P76577"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10542235}; Single-pass type II membrane protein {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pbpC yfgN b2519 JW2503"
---

# pbpC

`protein.P76577`

## Static

- Type: `protein`
- Source: `UniProt:P76577`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10542235}; Single-pass type II membrane protein {ECO:0000250}.

## Enriched Summary

FUNCTION: Cell wall formation. The enzyme has a penicillin-insensitive transglycosylase N-terminal domain (formation of linear glycan strands) and a transpeptidase C-terminal domain which may not be functional. {ECO:0000269|PubMed:10542235}. pbpC encodes a HMW penicillin binding protein (PBP) known as PBP1C. PBP1C (like CPLX0-7717 PBP1A and CPLX0-3951 PBP1B) contains characteristic transglycosylase and transpeptidase amino acid motifs but only transglycosylase activity has been assayed . PBP1C does not bind most of the β-lactams known to bind other PBPs leading to speculation that PBP1C does not have transpeptidase activity (the transpeptidase region is also responsible for penicillin binding) . PPB1C is predicted to contain a single transmembrane domain which anchors the cell to the inner membrane with the remainder of the enzyme located in the periplasm . PBP1C is responsible for 75% of transglycosylase activity in ether pemeabilized cells, but only less than 3% in crude membranes; PBP1C-specific murein synthesizing activity is sensitive to moenomycin . PBP1C binds 35S-labeled penicillin; maximum binding occurs at pH 5 . PBP1C binds moxalactam poorly . PBP1C binds furazlocillin . PBP1C binds a 125I labelled derivative of ampicillin...

## Biological Role

Catalyzes R06177 (reaction.R06177), [poly-N-acetyl-D-glucosaminyl-(1->4)-(N-acetyl-D-muramoylpentapeptide)]-diphosphoundecaprenol:[N-acetyl-D-glucosaminyl-(1->4)-N-acetyl-D-muramoylpentapeptide]-diphosphoundecaprenol polysaccharidetransferase (reaction.R06178), R06179 (reaction.R06179), RXN-16650 (reaction.ecocyc.RXN-16650).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Cell wall formation. The enzyme has a penicillin-insensitive transglycosylase N-terminal domain (formation of linear glycan strands) and a transpeptidase C-terminal domain which may not be functional. {ECO:0000269|PubMed:10542235}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R06177|reaction.R06177]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06178|reaction.R06178]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06179|reaction.R06179]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2519|gene.b2519]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76577`
- `KEGG:ecj:JW2503;eco:b2519;ecoc:C3026_13965;`
- `GeneID:947152;`
- `GO:GO:0004180; GO:0005886; GO:0006508; GO:0008360; GO:0008658; GO:0008955; GO:0009252; GO:0016020; GO:0030288; GO:0051781; GO:0071555`
- `EC:2.4.99.28`

## Notes

Penicillin-binding protein 1C (PBP-1c) (PBP1c) [Includes: Penicillin-insensitive transglycosylase (EC 2.4.99.28) (Peptidoglycan TGase); Transpeptidase-like module]
