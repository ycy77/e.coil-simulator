---
entity_id: "protein.P0A725"
entity_type: "protein"
name: "lpxC"
source_database: "UniProt"
source_id: "P0A725"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpxC asmB envA b0096 JW0094"
---

# lpxC

`protein.P0A725`

## Static

- Type: `protein`
- Source: `UniProt:P0A725`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of UDP-3-O-myristoyl-N-acetylglucosamine to form UDP-3-O-myristoylglucosamine and acetate, the committed step in lipid A biosynthesis. {ECO:0000255|HAMAP-Rule:MF_00388, ECO:0000269|PubMed:10026271, ECO:0000269|PubMed:8530464, ECO:0000269|PubMed:8824222, ECO:0000269|Ref.7}. EC-3.5.1.108 (LpxC) catalyzes the second reaction and the first committed step in lipid A biosynthesis. LpxC hydrolyzes UDP-3-O-(3-hydroxymyristoyl)-N-acetlyglucosamine to UDP-3-O-(3-hydroxymyristoyl)glucosamine and acetate . The mechanism of action of LpxC has been studied, and a high-throughput fluorescent screen as well as a mass-spectrometry based screen have been developed to evaluate LpxC activity . LpxC is a metalloenzyme that was reported to require bound zinc for activity . Site-directed mutagenesis has identified zinc binding sites . More recently, LpxC with bound iron was shown to have higher activity than zinc-bound enzyme . While LpxC has significantly higher affinity for zinc, in vivo concentrations of readily available iron are higher that those of zinc. It has been proposed that LpxC is able to switch between metal ions in response to their availability . LpxC abundance is regulated in response to the cells need for lipid A...

## Biological Role

Catalyzes UDPACYLGLCNACDEACETYL-RXN (reaction.ecocyc.UDPACYLGLCNACDEACETYL-RXN).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of UDP-3-O-myristoyl-N-acetylglucosamine to form UDP-3-O-myristoylglucosamine and acetate, the committed step in lipid A biosynthesis. {ECO:0000255|HAMAP-Rule:MF_00388, ECO:0000269|PubMed:10026271, ECO:0000269|PubMed:8530464, ECO:0000269|PubMed:8824222, ECO:0000269|Ref.7}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UDPACYLGLCNACDEACETYL-RXN|reaction.ecocyc.UDPACYLGLCNACDEACETYL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0096|gene.b0096]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A725`
- `KEGG:ecj:JW0094;eco:b0096;ecoc:C3026_00385;`
- `GeneID:86862606;93777338;944816;`
- `GO:GO:0005506; GO:0005737; GO:0008270; GO:0009245; GO:0016020; GO:0019213; GO:0103117`
- `EC:3.5.1.108`

## Notes

UDP-3-O-acyl-N-acetylglucosamine deacetylase (UDP-3-O-acyl-GlcNAc deacetylase) (EC 3.5.1.108) (Protein EnvA) (UDP-3-O-[R-3-hydroxymyristoyl]-N-acetylglucosamine deacetylase)
