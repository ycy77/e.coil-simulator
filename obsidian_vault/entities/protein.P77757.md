---
entity_id: "protein.P77757"
entity_type: "protein"
name: "arnC"
source_database: "UniProt"
source_id: "P77757"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arnC pmrF yfbF b2254 JW2248"
---

# arnC

`protein.P77757`

## Static

- Type: `protein`
- Source: `UniProt:P77757`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Catalyzes the transfer of 4-deoxy-4-formamido-L-arabinose from UDP to undecaprenyl phosphate. The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:11706007}. ArnC is an undecaprenyl transferase that acts in a pathway which modifies lipid A phosphates with 4-amino-4-deoxy-L-arabinose (L-Ara4N), causing increased resistance to polymyxin . ArnC is an inner membrane protein with two predicted transmembrane domains; the C terminus is located in the cytoplasm . ArnC selectively converts uridine 5'-diphospho-β-(4-deoxy-4-formamido-L-arabinose) (UDP-L-Ara4FN), but not uridine 5'-diphospho-β-(4-amino-4-deoxy-L-arabinose) (UDP-L-Ara4N), to lipid product . ArnC: "L-Ara4N (4-amino-4-deoxy-L-arabinose) biosynthesis" PmrF: "polymyxin resistance" Review:

## Biological Role

Catalyzes RXN0-3521 (reaction.ecocyc.RXN0-3521).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of 4-deoxy-4-formamido-L-arabinose from UDP to undecaprenyl phosphate. The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:11706007}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3521|reaction.ecocyc.RXN0-3521]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2254|gene.b2254]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77757`
- `KEGG:ecj:JW2248;eco:b2254;ecoc:C3026_12590;`
- `GeneID:93774920;945275;`
- `GO:GO:0005886; GO:0009103; GO:0009245; GO:0016020; GO:0016780; GO:0036108; GO:0046677; GO:0099621`
- `EC:2.4.2.53`

## Notes

Undecaprenyl-phosphate 4-deoxy-4-formamido-L-arabinose transferase (EC 2.4.2.53) (Polymyxin resistance protein PmrF) (Undecaprenyl-phosphate Ara4FN transferase) (Ara4FN transferase)
