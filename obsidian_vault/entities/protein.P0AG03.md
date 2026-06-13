---
entity_id: "protein.P0AG03"
entity_type: "protein"
name: "ubiX"
source_database: "UniProt"
source_id: "P0AG03"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiX dedF b2311 JW2308"
---

# ubiX

`protein.P0AG03`

## Static

- Type: `protein`
- Source: `UniProt:P0AG03`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Flavin prenyltransferase that catalyzes the synthesis of the prenylated FMN cofactor (prenyl-FMN) for 4-hydroxy-3-polyprenylbenzoic acid decarboxylase UbiD. The prenyltransferase is metal-independent and links a dimethylallyl moiety from dimethylallyl monophosphate (DMAP) to the flavin N5 and C6 atoms of FMN (By similarity). Acts in concert with UbiD to perform the decarboxylation of 4-hydroxy-3-octaprenyl-benzoate, a step in the biosynthesis of coenzyme Q (PubMed:16923914, PubMed:17889824). {ECO:0000255|HAMAP-Rule:MF_01984, ECO:0000269|PubMed:16923914, ECO:0000269|PubMed:17889824}. Evidence gathered for orthologous enzymes and genetic interactions indicate that UbiX is a flavin prenyltransferase that produces a novel cofactor for CPLX0-301 UbiD, CPD-18260 . ubiX was first thought to encode a second 3-octaprenyl-4-hydroxybenzoate decarboxylase in E. coli ; however, no biochemical evidence for the enzymatic function of UbiX was available at that time. The fungal genes pad1 and fdc1 are homologs of E. coli ubiX and ubiD, respectively. Coexpression of Fdc1 from both Saccharomyces cerevisiae and Aspergillus niger with either the respective Pad1 enzymes or E. coli UbiX allows isolation of active Fdc1, suggesting that UbiX is isofunctional with Pad1. The enzymatic function of Pseudomonas aeruginosa UbiX and the structure of its product, CPD-18260, were fully characterized...

## Biological Role

Catalyzes RXN-16937 (reaction.ecocyc.RXN-16937).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Flavin prenyltransferase that catalyzes the synthesis of the prenylated FMN cofactor (prenyl-FMN) for 4-hydroxy-3-polyprenylbenzoic acid decarboxylase UbiD. The prenyltransferase is metal-independent and links a dimethylallyl moiety from dimethylallyl monophosphate (DMAP) to the flavin N5 and C6 atoms of FMN (By similarity). Acts in concert with UbiD to perform the decarboxylation of 4-hydroxy-3-octaprenyl-benzoate, a step in the biosynthesis of coenzyme Q (PubMed:16923914, PubMed:17889824). {ECO:0000255|HAMAP-Rule:MF_01984, ECO:0000269|PubMed:16923914, ECO:0000269|PubMed:17889824}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-16937|reaction.ecocyc.RXN-16937]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2311|gene.b2311]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG03`
- `KEGG:ecj:JW2308;eco:b2311;ecoc:C3026_12885;`
- `GeneID:949033;`
- `GO:GO:0006744; GO:0016831; GO:0106141; GO:0120232`
- `EC:2.5.1.129`

## Notes

Flavin prenyltransferase UbiX (EC 2.5.1.129)
