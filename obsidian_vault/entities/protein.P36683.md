---
entity_id: "protein.P36683"
entity_type: "protein"
name: "acnB"
source_database: "UniProt"
source_id: "P36683"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acnB yacI yacJ b0118 JW0114"
---

# acnB

`protein.P36683`

## Static

- Type: `protein`
- Source: `UniProt:P36683`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the tricarboxylic acid (TCA)(acetyl degradation route) and the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the reversible isomerization of citrate to isocitrate via cis-aconitate. Also catalyzes the hydration of 2-methyl-cis-aconitate to yield (2R,3S)-2-methylisocitrate. The apo form of AcnB functions as a RNA-binding regulatory protein. During oxidative stress inactive AcnB apo-enzyme without iron sulfur clusters binds the acnB mRNA 3' UTRs (untranslated regions), stabilizes acnB mRNA and increases AcnB synthesis, thus mediating a post-transcriptional positive autoregulatory switch. AcnB also decreases the stability of the sodA transcript. {ECO:0000269|PubMed:10585860, ECO:0000269|PubMed:10589714, ECO:0000269|PubMed:11932448, ECO:0000269|PubMed:12473114, ECO:0000269|PubMed:15882410, ECO:0000269|PubMed:8000525, ECO:0000269|PubMed:8932712}. There are two aconitases in E. coli, both of which catalyze the reversible isomerization of citrate and iso-citrate via cis-aconitate. AcnB also plays a role in the methylcitrate cycle for degradation of propionate, where it is responsible for hydration of 2-methyl-cis-aconitate to (2R,3S)-2-methylisocitrate . The apo form of AcnB is able to bind mRNA and enhances translation of AcnB...

## Biological Role

Catalyzes citrate hydroxymutase (reaction.R01324), citrate hydro-lyase (cis-aconitate-forming) (reaction.R01325), isocitrate hydro-lyase (cis-aconitate-forming) (reaction.R01900), (2S,3R)-3-hydroxybutane-1,2,3-tricarboxylate hydro-lyase (reaction.R04425). Component of bifunctional aconitate hydratase B/2-methylisocitrate dehydratase (complex.ecocyc.CPLX0-7761).

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

FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the tricarboxylic acid (TCA)(acetyl degradation route) and the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the reversible isomerization of citrate to isocitrate via cis-aconitate. Also catalyzes the hydration of 2-methyl-cis-aconitate to yield (2R,3S)-2-methylisocitrate. The apo form of AcnB functions as a RNA-binding regulatory protein. During oxidative stress inactive AcnB apo-enzyme without iron sulfur clusters binds the acnB mRNA 3' UTRs (untranslated regions), stabilizes acnB mRNA and increases AcnB synthesis, thus mediating a post-transcriptional positive autoregulatory switch. AcnB also decreases the stability of the sodA transcript. {ECO:0000269|PubMed:10585860, ECO:0000269|PubMed:10589714, ECO:0000269|PubMed:11932448, ECO:0000269|PubMed:12473114, ECO:0000269|PubMed:15882410, ECO:0000269|PubMed:8000525, ECO:0000269|PubMed:8932712}.

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
- `is_component_of` --> [[complex.ecocyc.CPLX0-7761|complex.ecocyc.CPLX0-7761]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0118|gene.b0118]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36683`
- `KEGG:ecj:JW0114;eco:b0118;ecoc:C3026_00495;`
- `GeneID:93777318;944864;`
- `GO:GO:0003729; GO:0003730; GO:0003994; GO:0005829; GO:0006097; GO:0006099; GO:0006417; GO:0019629; GO:0046872; GO:0047456; GO:0051539`
- `EC:4.2.1.3; 4.2.1.99`

## Notes

Aconitate hydratase B (ACN) (Aconitase) (EC 4.2.1.3) ((2R,3S)-2-methylisocitrate dehydratase) ((2S,3R)-3-hydroxybutane-1,2,3-tricarboxylate dehydratase) (2-methyl-cis-aconitate hydratase) (EC 4.2.1.99) (Iron-responsive protein-like) (IRP-like) (RNA-binding protein)
