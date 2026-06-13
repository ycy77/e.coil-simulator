---
entity_id: "protein.P25516"
entity_type: "protein"
name: "acnA"
source_database: "UniProt"
source_id: "P25516"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acnA acn b1276 JW1268"
---

# acnA

`protein.P25516`

## Static

- Type: `protein`
- Source: `UniProt:P25516`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible isomerization of citrate to isocitrate via cis-aconitate. The apo form of AcnA functions as a RNA-binding regulatory protein which plays a role as a maintenance or survival enzyme during nutritional or oxidative stress. During oxidative stress inactive AcnA apo-enzyme without iron sulfur clusters binds the acnA mRNA 3' UTRs (untranslated regions), stabilizes acnA mRNA and increases AcnA synthesis, thus mediating a post-transcriptional positive autoregulatory switch. AcnA also enhances the stability of the sodA transcript. {ECO:0000269|PubMed:10585860, ECO:0000269|PubMed:10589714, ECO:0000269|PubMed:11932448, ECO:0000269|PubMed:12486059, ECO:0000269|PubMed:1838390, ECO:0000269|PubMed:9421904}. There are two aconitases in E. coli, both of which catalyze the reversible isomerization of citrate and iso-citrate via cis-aconitate. The apo form of AcnA is able to bind mRNA and enhances translation of AcnA . The AcnA enzyme is more stable, has a higher affinity for citrate and is active over a wider pH range than the AcnB enzyme . Unlike AcnB, AcnA is resistant to oxidation in vivo . The main role of the AcnA enzyme appears to be as a maintenance or survival enzyme during nutritional or oxidative stress, while the AcnB enzyme appears to function as the main catabolic enzyme...

## Biological Role

Catalyzes citrate hydroxymutase (reaction.R01324), citrate hydro-lyase (cis-aconitate-forming) (reaction.R01325), isocitrate hydro-lyase (cis-aconitate-forming) (reaction.R01900), (2S,3R)-3-hydroxybutane-1,2,3-tricarboxylate hydro-lyase (reaction.R04425). Component of aconitate hydratase A (complex.ecocyc.CPLX0-7760).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible isomerization of citrate to isocitrate via cis-aconitate. The apo form of AcnA functions as a RNA-binding regulatory protein which plays a role as a maintenance or survival enzyme during nutritional or oxidative stress. During oxidative stress inactive AcnA apo-enzyme without iron sulfur clusters binds the acnA mRNA 3' UTRs (untranslated regions), stabilizes acnA mRNA and increases AcnA synthesis, thus mediating a post-transcriptional positive autoregulatory switch. AcnA also enhances the stability of the sodA transcript. {ECO:0000269|PubMed:10585860, ECO:0000269|PubMed:10589714, ECO:0000269|PubMed:11932448, ECO:0000269|PubMed:12486059, ECO:0000269|PubMed:1838390, ECO:0000269|PubMed:9421904}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R01324|reaction.R01324]] `KEGG` `database` - via EC:4.2.1.3
- `catalyzes` --> [[reaction.R01325|reaction.R01325]] `KEGG` `database` - via EC:4.2.1.3
- `catalyzes` --> [[reaction.R01900|reaction.R01900]] `KEGG` `database` - via EC:4.2.1.3
- `catalyzes` --> [[reaction.R04425|reaction.R04425]] `KEGG` `database` - via EC:4.2.1.99
- `is_component_of` --> [[complex.ecocyc.CPLX0-7760|complex.ecocyc.CPLX0-7760]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1276|gene.b1276]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25516`
- `KEGG:ecj:JW1268;eco:b1276;`
- `GeneID:946724;`
- `GO:GO:0003729; GO:0003730; GO:0003994; GO:0005506; GO:0005737; GO:0005829; GO:0006097; GO:0006099; GO:0006979; GO:0009061; GO:0030350; GO:0046872; GO:0051539`
- `EC:4.2.1.3`

## Notes

Aconitate hydratase A (ACN) (Aconitase) (EC 4.2.1.3) (Iron-responsive protein-like) (IRP-like) (RNA-binding protein) (Stationary phase enzyme)
