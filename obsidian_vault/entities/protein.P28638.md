---
entity_id: "protein.P28638"
entity_type: "protein"
name: "yhdJ"
source_database: "UniProt"
source_id: "P28638"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhdJ b3262 JW5543"
---

# yhdJ

`protein.P28638`

## Static

- Type: `protein`
- Source: `UniProt:P28638`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A beta subtype methylase, recognizes the double-stranded sequence 5'-ATGCAT-3' and methylates A-5. {ECO:0000269|PubMed:17400740, ECO:0000303|PubMed:12654995}. Overexpression of YdhJ leads to methylation of genomic DNA at the NsiI recognition sequence (5'-ATGCAT-3'), and partially purified YdhJ is shown to methylate this sequence to produce N6-methyladenine in the 3' adenine position of ATGCAT in vitro . ydhJ is not an essential gene, and overexpression of ydhJ does not alter cell morphology . Overexpression of yhdJ from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid . A retracted publication claimed that the "CcrM" protein is a cell cycle-regulated DNA adenine methyltransferase that is essential for viability.

## Biological Role

Catalyzes 2.1.1.72-RXN (reaction.ecocyc.2.1.1.72-RXN).

## Annotation

FUNCTION: A beta subtype methylase, recognizes the double-stranded sequence 5'-ATGCAT-3' and methylates A-5. {ECO:0000269|PubMed:17400740, ECO:0000303|PubMed:12654995}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.1.1.72-RXN|reaction.ecocyc.2.1.1.72-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3262|gene.b3262]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28638`
- `KEGG:ecj:JW5543;eco:b3262;ecoc:C3026_17745;`
- `GeneID:947695;`
- `GO:GO:0003677; GO:0005737; GO:0008170; GO:0009007; GO:0032259`
- `EC:2.1.1.72`

## Notes

DNA adenine methyltransferase YhdJ (EC 2.1.1.72) (Type II methyltransferase M.EcoKII) (M.EcoKII)
