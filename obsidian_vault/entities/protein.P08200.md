---
entity_id: "protein.P08200"
entity_type: "protein"
name: "icd"
source_database: "UniProt"
source_id: "P08200"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "icd icdA icdE b1136 JW1122"
---

# icd

`protein.P08200`

## Static

- Type: `protein`
- Source: `UniProt:P08200`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidative decarboxylation of isocitrate to 2-oxoglutarate and carbon dioxide with the concomitant reduction of NADP(+). {ECO:0000269|PubMed:21151122, ECO:0000269|PubMed:3112144, ECO:0000269|PubMed:4400493, ECO:0000269|PubMed:7761851, ECO:0000269|PubMed:7819221}.

## Biological Role

Catalyzes isocitrate:NADP+ oxidoreductase (decarboxylating) (reaction.R00267), oxalosuccinate carboxy-lyase (2-oxoglutarate-forming) (reaction.R00268), isocitrate:NADP+ oxidoreductase (reaction.R01899). Component of isocitrate dehydrogenase (complex.ecocyc.ISOCITHASE-CPLX), isocitrate dehydrogenase-P (protein.ecocyc.ISOCITHASE-P).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco04146` Peroxisome (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidative decarboxylation of isocitrate to 2-oxoglutarate and carbon dioxide with the concomitant reduction of NADP(+). {ECO:0000269|PubMed:21151122, ECO:0000269|PubMed:3112144, ECO:0000269|PubMed:4400493, ECO:0000269|PubMed:7761851, ECO:0000269|PubMed:7819221}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco04146` Peroxisome (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00267|reaction.R00267]] `KEGG` `database` - via EC:1.1.1.42
- `catalyzes` --> [[reaction.R00268|reaction.R00268]] `KEGG` `database` - via EC:1.1.1.42
- `catalyzes` --> [[reaction.R01899|reaction.R01899]] `KEGG` `database` - via EC:1.1.1.42
- `is_component_of` --> [[complex.ecocyc.ISOCITHASE-CPLX|complex.ecocyc.ISOCITHASE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[protein.ecocyc.ISOCITHASE-P|protein.ecocyc.ISOCITHASE-P]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1136|gene.b1136]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08200`
- `KEGG:ecj:JW1122;eco:b1136;`
- `GeneID:945702;`
- `GO:GO:0000287; GO:0004450; GO:0005737; GO:0005829; GO:0006097; GO:0006099; GO:0006979; GO:0022900; GO:0051287; GO:0097216`
- `EC:1.1.1.42`

## Notes

Isocitrate dehydrogenase [NADP] (IDH) (EC 1.1.1.42) (IDP) (NADP(+)-dependent isocitric dehydrogenase) (NADP(+)-specific ICDH) (Oxalosuccinate decarboxylase)
