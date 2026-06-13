---
entity_id: "protein.P0ADA1"
entity_type: "protein"
name: "tesA"
source_database: "UniProt"
source_id: "P0ADA1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8098033, ECO:0000269|PubMed:8432696}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tesA apeA pldC b0494 JW0483"
---

# tesA

`protein.P0ADA1`

## Static

- Type: `protein`
- Source: `UniProt:P0ADA1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8098033, ECO:0000269|PubMed:8432696}.

## Enriched Summary

FUNCTION: TesA is a multifunctional esterase that can act as a thioesterase, lysophospholipase and protease (PubMed:10423542, PubMed:1864840, PubMed:238979, PubMed:4554913, PubMed:4945109, PubMed:791643, PubMed:8098033, PubMed:8132479, PubMed:8432696, PubMed:9070299). TesA functions as a thioesterase specific for fatty acyl thioesters of greater than ten carbons, with highest activity on palmitoyl-CoA, cis-vaccenoyl-CoA and palmitoleoyl-CoA (PubMed:10423542, PubMed:4554913, PubMed:8098033, PubMed:8132479, PubMed:9070299). TesA also possesses an arylesterase activity towards short acyl-chain aromatic esters such as alpha-naphthyl acetate, alpha-naphthyl butyrate, benzyl acetate and phenyl acetate (PubMed:9070299). Also able to hydrolyze short acyl-chain triacylglycerols such as triacetin and tributyrin, and p-nitrophenyl esters such as p-nitrophenyl hexanoate and p-nitrophenyl butyrate (PubMed:9070299). The protease activity is mainly active on small peptides (PubMed:8432696, PubMed:9070299). TesA is also able to hydrolyze p-nitrophenyl esters of N-substituted amino acids such as N-benzyloxycarbonyl-L-Phe-p-nitrophenyl ester (Z-L-Phe-ONp) and N-benzyloxycarbonyl-L-Tyr-p-nitrophenyl ester (Z-L-Tyr-ONp), however it is unable to hydrolyze N-acetyl-L-Phe ethyl ester and its Tyr analog (PubMed:10423542, PubMed:791643, PubMed:8432696)...

## Biological Role

Catalyzes phosphatidylcholine acylhydrolase (reaction.R01309), 1-acyl-sn-glycero-3-phosphoethanolamine aldehydohydrolase (reaction.R03416), L-2-lysophosphatidylethanolamine aldehydohydrolase (reaction.R03417), aryl-ester hydrolase (reaction.R06893), 2-lysophosphatidylcholine acylhydrolase (reaction.R07291), R08183 (reaction.R08183). Component of multifunctional acyl-CoA thioesterase I and protease I and lysophospholipase L1 (complex.ecocyc.CPLX0-7630).

## Enriched Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

FUNCTION: TesA is a multifunctional esterase that can act as a thioesterase, lysophospholipase and protease (PubMed:10423542, PubMed:1864840, PubMed:238979, PubMed:4554913, PubMed:4945109, PubMed:791643, PubMed:8098033, PubMed:8132479, PubMed:8432696, PubMed:9070299). TesA functions as a thioesterase specific for fatty acyl thioesters of greater than ten carbons, with highest activity on palmitoyl-CoA, cis-vaccenoyl-CoA and palmitoleoyl-CoA (PubMed:10423542, PubMed:4554913, PubMed:8098033, PubMed:8132479, PubMed:9070299). TesA also possesses an arylesterase activity towards short acyl-chain aromatic esters such as alpha-naphthyl acetate, alpha-naphthyl butyrate, benzyl acetate and phenyl acetate (PubMed:9070299). Also able to hydrolyze short acyl-chain triacylglycerols such as triacetin and tributyrin, and p-nitrophenyl esters such as p-nitrophenyl hexanoate and p-nitrophenyl butyrate (PubMed:9070299). The protease activity is mainly active on small peptides (PubMed:8432696, PubMed:9070299). TesA is also able to hydrolyze p-nitrophenyl esters of N-substituted amino acids such as N-benzyloxycarbonyl-L-Phe-p-nitrophenyl ester (Z-L-Phe-ONp) and N-benzyloxycarbonyl-L-Tyr-p-nitrophenyl ester (Z-L-Tyr-ONp), however it is unable to hydrolyze N-acetyl-L-Phe ethyl ester and its Tyr analog (PubMed:10423542, PubMed:791643, PubMed:8432696). TesA also hydrolyzes N-benzyloxycarbonyl-L-Phe beta-nitrophenyl ester (Cbz-Phe-ONap) and N-acetyl-DL-Phe-2-naphthyl ester (chymotrypsin-like specificity) (PubMed:4945109, PubMed:8432696). Shows a slow proteolytic activity against denatured casein (PubMed:4945109). The lysophospholipase activity of TesA is able to hydrolyze 1-palmitoyl-sn-glycero-3-phosphocholine, 1-acyl-sn-glycero-3-phosphoglycerol, 1- and 2-acyl-sn-glycero-3-phosphoethanolamine (PubMed:10423542, PubMed:1864840, PubMed:238979). {ECO:0000269|PubMed:10423542, ECO:0000269|PubMed:1864840, ECO:0000269|PubMed:238979, ECO:0000269|PubMed:4554913, ECO:0000269|PubMed:4945109, ECO:0000269|PubMed:791643, ECO:0000269|PubMed:8098033, ECO:0000269|PubMed:8132479, ECO:0000269|PubMed:8432696, ECO:0000269|PubMed:9070299}.

## Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.R01309|reaction.R01309]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` --> [[reaction.R03416|reaction.R03416]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` --> [[reaction.R03417|reaction.R03417]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` --> [[reaction.R06893|reaction.R06893]] `KEGG` `database` - via EC:3.1.1.2
- `catalyzes` --> [[reaction.R07291|reaction.R07291]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` --> [[reaction.R08183|reaction.R08183]] `KEGG` `database` - via EC:3.1.2.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7630|complex.ecocyc.CPLX0-7630]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0494|gene.b0494]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADA1`
- `KEGG:ecj:JW0483;eco:b0494;`
- `GeneID:945127;`
- `GO:GO:0004064; GO:0004622; GO:0006508; GO:0006629; GO:0008233; GO:0016297; GO:0030288; GO:0042802; GO:0052816`
- `EC:3.1.1.2; 3.1.1.5; 3.1.2.14; 3.1.2.2; 3.4.21.-`

## Notes

Thioesterase 1/protease 1/lysophospholipase L1 (TAP) (Acyl-CoA thioesterase 1) (TESA) (EC 3.1.2.2) (Acyl-CoA thioesterase I) (Arylesterase) (EC 3.1.1.2) (Lysophospholipase L1) (EC 3.1.1.5) (Oleoyl-[acyl-carrier-protein] hydrolase) (EC 3.1.2.14) (Phospholipid degradation C) (Pldc) (Protease 1) (EC 3.4.21.-) (Protease I) (Thioesterase I/protease I) (TEP-I)
