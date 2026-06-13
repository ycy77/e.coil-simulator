---
entity_id: "protein.P39401"
entity_type: "protein"
name: "mdoB"
source_database: "UniProt"
source_id: "P39401"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdoB opgB yjjO b4359 JW5794"
---

# mdoB

`protein.P39401`

## Static

- Type: `protein`
- Source: `UniProt:P39401`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Transfers a phosphoglycerol residue from phosphatidylglycerol to the membrane-bound nascent glucan backbones. {ECO:0000269|PubMed:2985566, ECO:0000269|PubMed:6094515}. E. coli opgB encodes two phosphoglycerol transferases. Phosphoglycerol transferase I is a membrane bound enzyme which catalyzes the transfer of phosphoglycerol residues from phosphatidylglycerol to membrane derived oligosaccharides (MDOs), now known as osmoregulated periplasmic glucans (OPGs). Phosphoglycerol transferase II is a soluble periplasmic enzyme which catalyzes the transfer of phosphoglycerol residues between species of MDO leading to the formation of multiply substituted oligosaccharides. In addition, at low concentrations of acceptor, phosphoglycerol transferase II can act as a cyclase liberating free cyclic phosphoglycerol . Phosphoglycerol transferase II is the proteolytically processed form of PGLYCEROLTRANSI-MONOMER . Phosphoglycerol transferase II does not utilize phosphatidylglycerol, but catalyzes the transfer of phosphoglycerol residues between species of osmoregulated periplasmic glucans (OPGs) leading to the formation of multiply substituted oligosaccharides. In addition, at low concentrations of acceptor, phosphoglycerol transferase II can act as a cyclase liberating free cyclic phosphoglycerol .

## Biological Role

Catalyzes PGLYCEROLTRANSI-RXN (reaction.ecocyc.PGLYCEROLTRANSI-RXN), PGLYCEROLTRANSII-RXN (reaction.ecocyc.PGLYCEROLTRANSII-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: Transfers a phosphoglycerol residue from phosphatidylglycerol to the membrane-bound nascent glucan backbones. {ECO:0000269|PubMed:2985566, ECO:0000269|PubMed:6094515}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.PGLYCEROLTRANSI-RXN|reaction.ecocyc.PGLYCEROLTRANSI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PGLYCEROLTRANSII-RXN|reaction.ecocyc.PGLYCEROLTRANSII-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4359|gene.b4359]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39401`
- `KEGG:ecj:JW5794;eco:b4359;ecoc:C3026_23550;`
- `GeneID:948888;`
- `GO:GO:0005886; GO:0008960; GO:0009250; GO:0016020; GO:0016740`
- `EC:2.7.8.20`

## Notes

Phosphoglycerol transferase I (EC 2.7.8.20) (Phosphatidylglycerol--membrane-oligosaccharide glycerophosphotransferase)
