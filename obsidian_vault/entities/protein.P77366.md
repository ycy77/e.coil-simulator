---
entity_id: "protein.P77366"
entity_type: "protein"
name: "ycjU"
source_database: "UniProt"
source_id: "P77366"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:20128927}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycjU pgmB b1317 JW1310"
---

# ycjU

`protein.P77366`

## Static

- Type: `protein`
- Source: `UniProt:P77366`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:20128927}.

## Enriched Summary

FUNCTION: Catalyzes the conversion of beta D-glucose 1-phosphate (G1P) to D-glucose 6-phosphate (G6P), forming beta-D-glucose 1,6-(bis)phosphate (beta-G16P) as an intermediate (Probable) (PubMed:16990279, PubMed:29684280). Phosphatase activity with the reaction intermediate beta-G16P has been measured (PubMed:25848029). In vitro interconverts beta D-glucose 1-phosphate, beta-D-allose 1-phosphate, beta-D-galactose 1-phosphate and beta-D-mannose 1-phosphate to their corresponding sugar 6-phosphate product. The beta-D-glucose 1-phosphate substrate may be furnished by YcjT (AC P77154), the apparent upstream enzyme in the putative biochemical pathway encoded in this locus (yjcM to ycjW) (PubMed:29684280). It may play a key role in the regulation of the flow of carbohydrate intermediates in glycolysis and the formation of the sugar nucleotide UDP-glucose. {ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:25848029, ECO:0000269|PubMed:29684280, ECO:0000305|PubMed:25848029}. YcjU is a β-phosphoglucomutase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases . Phosphatase activity of the enzyme with the reaction intermediate β-glucose-1,6-bisphosphate has been measured . ycjU was identified in a screen for genes that reduce the lethal effects of stress...

## Biological Role

Catalyzes BETA-PHOSPHOGLUCOMUTASE-RXN (reaction.ecocyc.BETA-PHOSPHOGLUCOMUTASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of beta D-glucose 1-phosphate (G1P) to D-glucose 6-phosphate (G6P), forming beta-D-glucose 1,6-(bis)phosphate (beta-G16P) as an intermediate (Probable) (PubMed:16990279, PubMed:29684280). Phosphatase activity with the reaction intermediate beta-G16P has been measured (PubMed:25848029). In vitro interconverts beta D-glucose 1-phosphate, beta-D-allose 1-phosphate, beta-D-galactose 1-phosphate and beta-D-mannose 1-phosphate to their corresponding sugar 6-phosphate product. The beta-D-glucose 1-phosphate substrate may be furnished by YcjT (AC P77154), the apparent upstream enzyme in the putative biochemical pathway encoded in this locus (yjcM to ycjW) (PubMed:29684280). It may play a key role in the regulation of the flow of carbohydrate intermediates in glycolysis and the formation of the sugar nucleotide UDP-glucose. {ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:25848029, ECO:0000269|PubMed:29684280, ECO:0000305|PubMed:25848029}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.BETA-PHOSPHOGLUCOMUTASE-RXN|reaction.ecocyc.BETA-PHOSPHOGLUCOMUTASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1317|gene.b1317]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77366`
- `KEGG:ecj:JW1310;eco:b1317;ecoc:C3026_07715;`
- `GeneID:945891;`
- `GO:GO:0000287; GO:0005737; GO:0005975; GO:0006974; GO:0008801; GO:0009294; GO:0046677`
- `EC:5.4.2.6`

## Notes

Beta-phosphoglucomutase (Beta-PGM) (EC 5.4.2.6)
