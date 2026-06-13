---
entity_id: "protein.P07014"
entity_type: "protein"
name: "sdhB"
source_database: "UniProt"
source_id: "P07014"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sdhB b0724 JW0714"
---

# sdhB

`protein.P07014`

## Static

- Type: `protein`
- Source: `UniProt:P07014`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; the fumarate reductase is used in anaerobic growth, and the succinate dehydrogenase is used in aerobic growth. This is one of two catalytic subunits of the four-subunit succinate dehydrogenase (SQR) enzyme. This subunit contains three iron-sulfur clusters: a 2Fe-2S, a 4Fe-4S and a 3Fe-4S. This subunit has 38% identity to the fumarate reductase iron-sulfur cluster subunit, FrdB . The iron-sulfur clusters of this subunit act as electron transfer redox centers, delivering electrons from the FAD cofactor in SdhA to the ubiquinone binding site within the membrane domain . sdhB belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . ArcA appears to repress sdhB gene expression under anaerobiosis. Two putative ArcA binding sites were identified 69, 267 and 330 bp upstream of this gene , but no promoter upstream of it has been identified. Instead, sdhB is transcribed from two promoters: one of them is located usptream of sdhD gene and the other one upstream of sdhC gene. The sdhCp promoter is repressed by ArcA. A ΔsdhB mutation suppresses the succinate-dependent growth phenotype of a ΔlipB mutant .

## Biological Role

Component of succinate:quinone oxidoreductase (complex.ecocyc.CPLX0-8160), succinate:quinone oxidoreductase subcomplex (complex.ecocyc.SUCC-DEHASE).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; the fumarate reductase is used in anaerobic growth, and the succinate dehydrogenase is used in aerobic growth.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8160|complex.ecocyc.CPLX0-8160]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.SUCC-DEHASE|complex.ecocyc.SUCC-DEHASE]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0724|gene.b0724]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07014`
- `KEGG:ecj:JW0714;eco:b0724;ecoc:C3026_03625;`
- `GeneID:945300;`
- `GO:GO:0005886; GO:0006099; GO:0008177; GO:0009055; GO:0009060; GO:0016020; GO:0019646; GO:0022904; GO:0045273; GO:0046872; GO:0051536; GO:0051537; GO:0051538; GO:0051539`
- `EC:1.3.5.1`

## Notes

Succinate dehydrogenase iron-sulfur subunit (EC 1.3.5.1)
