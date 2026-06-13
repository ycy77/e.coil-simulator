---
entity_id: "protein.P43341"
entity_type: "protein"
name: "lpxH"
source_database: "UniProt"
source_id: "P43341"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:12000770}; Peripheral membrane protein {ECO:0000269|PubMed:12000770}; Cytoplasmic side {ECO:0000305|PubMed:12000770}. Cytoplasm {ECO:0000269|PubMed:12000770}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpxH ybbF b0524 JW0513"
---

# lpxH

`protein.P43341`

## Static

- Type: `protein`
- Source: `UniProt:P43341`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:12000770}; Peripheral membrane protein {ECO:0000269|PubMed:12000770}; Cytoplasmic side {ECO:0000305|PubMed:12000770}. Cytoplasm {ECO:0000269|PubMed:12000770}.

## Enriched Summary

FUNCTION: Hydrolyzes the pyrophosphate bond of UDP-2,3-diacylglucosamine to yield 2,3-diacylglucosamine 1-phosphate (lipid X) and UMP by catalyzing the attack of water at the alpha-P atom (PubMed:12000770). Involved in the biosynthesis of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell (PubMed:12000770, PubMed:12000771). Is essential for E.coli growth (PubMed:12000771). Does not cleave the unacylated UDP-GlcNAc, the mono-acylated UDP-3-O-(R)-3-hydroxymyristoyl-GlcNAc, and CDP-diacylglycerol (PubMed:12000770). {ECO:0000269|PubMed:12000770, ECO:0000269|PubMed:12000771}. UDP-2,3-diacylglucosamine hydrolase (LpxH) catalyzes the fourth step in lipid A synthesis, hydrolyzing UDP-2,3-bis(3-hydroxymyristoyl)glucosamine to yield 2,3-bis(3-hydroxymyristoyl)-β-D-glucosaminyl 1-phosphate (lipid X) . LpxH is a peripheral membrane protein whose activity appears to be stimulated by Mn2+ in vitro. LpxH catalyzes the attack of water on the α-P atom of the UDP moiety to form lipid X and UMP . Although LpxH and CDPDIGLYPYPHOSPHA-MONOMER (Cdh) are both able to catalyze the hydrolysis of UDP-2,3-diacylglucosamine in vitro, Cdh can not substitute for LpxH in vivo . The Cdh substrate CDP-diacylglycerol is not a substrate for LpxH . A crystal structure of a solubilized, catalytically active mutant of LpxH has been solved at 2 Å resolution...

## Biological Role

Catalyzes LIPIDXSYNTHESIS-RXN (reaction.ecocyc.LIPIDXSYNTHESIS-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Hydrolyzes the pyrophosphate bond of UDP-2,3-diacylglucosamine to yield 2,3-diacylglucosamine 1-phosphate (lipid X) and UMP by catalyzing the attack of water at the alpha-P atom (PubMed:12000770). Involved in the biosynthesis of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell (PubMed:12000770, PubMed:12000771). Is essential for E.coli growth (PubMed:12000771). Does not cleave the unacylated UDP-GlcNAc, the mono-acylated UDP-3-O-(R)-3-hydroxymyristoyl-GlcNAc, and CDP-diacylglycerol (PubMed:12000770). {ECO:0000269|PubMed:12000770, ECO:0000269|PubMed:12000771}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.LIPIDXSYNTHESIS-RXN|reaction.ecocyc.LIPIDXSYNTHESIS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0524|gene.b0524]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P43341`
- `KEGG:ecj:JW0513;eco:b0524;ecoc:C3026_02570;`
- `GeneID:949053;`
- `GO:GO:0005737; GO:0008758; GO:0009245; GO:0019897; GO:0030145`
- `EC:3.6.1.54`

## Notes

UDP-2,3-diacylglucosamine hydrolase (EC 3.6.1.54) (UDP-2,3-diacylglucosamine diphosphatase) (UDP-2,3-diacylglucosamine pyrophosphatase)
