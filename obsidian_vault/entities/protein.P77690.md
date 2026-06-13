---
entity_id: "protein.P77690"
entity_type: "protein"
name: "arnB"
source_database: "UniProt"
source_id: "P77690"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arnB pmrH yfbE b2253 JW5372"
---

# arnB

`protein.P77690`

## Static

- Type: `protein`
- Source: `UniProt:P77690`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of UDP-4-keto-arabinose (UDP-Ara4O) to UDP-4-amino-4-deoxy-L-arabinose (UDP-L-Ara4N). The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:12704196}. ArnB is a UDP-L-Ara4O C-4" transaminase that acts in a pathway which modifies lipid A phosphates with 4-amino-4-deoxy-L-arabinose (L-Ara4N), causing increased resistance to polymyxin . Structural and biochemical characterization of Salmonella typhimurium ArnB has been performed; crystal structures of the enzyme are presented and discussed with respect to catalysis . Expression of arnB is induced by the presence of FeSO4 (which primarily yields oxidized ferric iron in solution); the effect is dependent on the presence of the BasS-BasR two-component system . Fe(III) promotes transcription of the BasR activated arn operon and polymyxin resistance in E. coli K-12 . Chromosomal expression of the Salmonella typhimurium pmrD gene enables E. coli K-12 to induce the BasR activated arn operon and promotes resistance to polymyxin B during growth in a low Mg2+ environment ArnB: "L-Ara4N (4-amino-4-deoxy-L-arabinose) biosynthesis" PmrH: "polymyxin resistance" Review:

## Biological Role

Catalyzes RXN0-1863 (reaction.ecocyc.RXN0-1863). Bound by Pyridoxal phosphate (molecule.C00018).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of UDP-4-keto-arabinose (UDP-Ara4O) to UDP-4-amino-4-deoxy-L-arabinose (UDP-L-Ara4N). The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:12704196}.

## Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1863|reaction.ecocyc.RXN0-1863]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2253|gene.b2253]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77690`
- `KEGG:ecj:JW5372;eco:b2253;`
- `GeneID:947375;`
- `GO:GO:0000271; GO:0005737; GO:0008483; GO:0009103; GO:0009245; GO:0016020; GO:0030170; GO:0046677; GO:0099620`
- `EC:2.6.1.87`

## Notes

UDP-4-amino-4-deoxy-L-arabinose--oxoglutarate aminotransferase (EC 2.6.1.87) (Polymyxin resistance protein PmrH) (UDP-(beta-L-threo-pentapyranosyl-4''-ulose diphosphate) aminotransferase) (UDP-Ara4O aminotransferase) (UDP-4-amino-4-deoxy-L-arabinose aminotransferase)
