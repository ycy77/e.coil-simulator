---
entity_id: "protein.P27129"
entity_type: "protein"
name: "waaJ"
source_database: "UniProt"
source_id: "P27129"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}. Note=Membrane associated. {ECO:0000250|UniProtKB:Q9ZIT6}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaJ rfaJ waaR b3626 JW3601"
---

# waaJ

`protein.P27129`

## Static

- Type: `protein`
- Source: `UniProt:P27129`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}. Note=Membrane associated. {ECO:0000250|UniProtKB:Q9ZIT6}.

## Enriched Summary

FUNCTION: Glucosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:10234827). Catalyzes the addition of a glucose (glucose III) to the outer-core glucose II (PubMed:10234827). {ECO:0000269|PubMed:10234827}. WaaJ (also known as WaaR and formerly RfaJ) is a UDP-glucose:(glucosyl)LPS α-1,2-glucosyltransferase which adds the third glucose (GlcIII) to the second glucose (GlcII) in the outer core of E. coli K-12 LPS . waaJ in E. coli K-12 is also referred to in the literature by the synonym WaaR. Early studies characterized the waa (rfa) locus and identified waaJ in both E. coli and Salmonella typhimurium . Later work renamed waaJ to waaR in E. coli K-12 to differentiate its activity (formation of α-D-Glcp-(1→2)-α-D-Glcp in the LPS outer core) from that of WaaJ in S. typhimurium (formation of α-D-Glcp-(1→2)-α-D-Galp) (see ). waaJ is predicted to encode a soluble or peripheral membrane protein; WaaJ activity requires functional waaB; WaaJ function is essential for Mu phage sensitivity . The substrate donor and acceptor specificities of several recombinantly produced outer core glycosyltransferases from different E. coli strains have been studied, including the WaaR UDP-glucose:(glucosyl) LPS alpha-1,2-glucosyltransferase of the non K-12 E. coli strain F632 (CPD-21354 "R2 core type")...

## Biological Role

Catalyzes RXN0-5126 (reaction.ecocyc.RXN0-5126).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Glucosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:10234827). Catalyzes the addition of a glucose (glucose III) to the outer-core glucose II (PubMed:10234827). {ECO:0000269|PubMed:10234827}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5126|reaction.ecocyc.RXN0-5126]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3626|gene.b3626]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27129`
- `KEGG:ecj:JW3601;eco:b3626;ecoc:C3026_19655;`
- `GeneID:948142;`
- `GO:GO:0005886; GO:0008918; GO:0008919; GO:0009244; GO:0046872`
- `EC:2.4.1.58`

## Notes

Lipopolysaccharide 1,2-glucosyltransferase (EC 2.4.1.58) (UDP-glucose:(glucosyl) LPS alpha 1,2-glucosyltransferase)
