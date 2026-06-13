---
entity_id: "protein.P37001"
entity_type: "protein"
name: "pagP"
source_database: "UniProt"
source_id: "P37001"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_00837, ECO:0000269|PubMed:11013210}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pagP crcA ybeG b0622 JW0617"
---

# pagP

`protein.P37001`

## Static

- Type: `protein`
- Source: `UniProt:P37001`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_00837, ECO:0000269|PubMed:11013210}.

## Enriched Summary

FUNCTION: Transfers a palmitate residue from the sn-1 position of a phospholipid to the N-linked hydroxymyristate on the proximal unit of lipid A or its precursors. Phosphatidylglycerol (PtdGro), phosphatidylethanolamine (PtdEtn), phosphatidylserine (PtdSer) and phosphatidic acid (Ptd-OH) are all effective acyl donors. {ECO:0000269|PubMed:11013210, ECO:0000269|PubMed:20826347, ECO:0000269|PubMed:20853818}. The outer membrane protein PagP catalyses the transfer of a palmitate chain from phospholipid donor to the lipid A moiety of lipopolysaccharide (LPS), a modification that is important for virulence in many gram-negative bacteria. Purified PagP transfers a palmitate chain from the sn-1 position of a phospholipid substrate (phosphatidylcholine substrates and common E. coli phospholipids) to the amide-linked hydroxymyristate chain of the proximal glucosamine unit (GlcN I) of disaccharide lipid A precursors (lipid IVA and Kdo2-lipid IVA) in vitro; the expected physiological substrate of PagP is the lipid A moiety of fully assembled CPD0-939 "LPS" in the outer membrane; PagP is highly selective for a saturated palmitate chain . PagP is an integral outer membrane enzyme...

## Biological Role

Catalyzes RXN-20913 (reaction.ecocyc.RXN-20913), RXN-20914 (reaction.ecocyc.RXN-20914), RXN-20915 (reaction.ecocyc.RXN-20915), RXN-20916 (reaction.ecocyc.RXN-20916), RXN-20918 (reaction.ecocyc.RXN-20918), RXN-20919 (reaction.ecocyc.RXN-20919).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Transfers a palmitate residue from the sn-1 position of a phospholipid to the N-linked hydroxymyristate on the proximal unit of lipid A or its precursors. Phosphatidylglycerol (PtdGro), phosphatidylethanolamine (PtdEtn), phosphatidylserine (PtdSer) and phosphatidic acid (Ptd-OH) are all effective acyl donors. {ECO:0000269|PubMed:11013210, ECO:0000269|PubMed:20826347, ECO:0000269|PubMed:20853818}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.RXN-20913|reaction.ecocyc.RXN-20913]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20914|reaction.ecocyc.RXN-20914]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20915|reaction.ecocyc.RXN-20915]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20916|reaction.ecocyc.RXN-20916]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20918|reaction.ecocyc.RXN-20918]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-20919|reaction.ecocyc.RXN-20919]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0622|gene.b0622]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37001`
- `KEGG:ecj:JW0617;eco:b0622;ecoc:C3026_03110;`
- `GeneID:75205016;946360;`
- `GO:GO:0009245; GO:0009279; GO:0016416`
- `EC:2.3.1.251`

## Notes

Lipid A palmitoyltransferase PagP (EC 2.3.1.251) (Lipid A acylation protein)
