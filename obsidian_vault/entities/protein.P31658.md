---
entity_id: "protein.P31658"
entity_type: "protein"
name: "hchA"
source_database: "UniProt"
source_id: "P31658"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hchA yedU yzzC b1967 JW1950"
---

# hchA

`protein.P31658`

## Static

- Type: `protein`
- Source: `UniProt:P31658`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Protein and nucleotide deglycase that catalyzes the deglycation of the Maillard adducts formed between amino groups of proteins or nucleotides and reactive carbonyl groups of glyoxals (PubMed:26102038, PubMed:26774339, PubMed:28596309). Thus, functions as a protein deglycase that repairs methylglyoxal- and glyoxal-glycated proteins, and releases repaired proteins and lactate or glycolate, respectively. Deglycates cysteine, arginine and lysine residues in proteins, and thus reactivates these proteins by reversing glycation by glyoxals. Is able to repair glycated serum albumin, aspartate aminotransferase, glyceraldehyde-3-phosphate dehydrogenase, and fructose biphosphate aldolase. Acts on early glycation intermediates (hemithioacetals and aminocarbinols), preventing the formation of Schiff bases and advanced glycation endproducts (AGE) that cause irreversible damage (PubMed:26102038, PubMed:26774339). Also functions as a nucleotide deglycase able to repair glycated guanine in the free nucleotide pool (GTP, GDP, GMP, dGTP) and in DNA and RNA. Is thus involved in a major nucleotide repair system named guanine glycation repair (GG repair), dedicated to reversing methylglyoxal and glyoxal damage via nucleotide sanitization and direct nucleic acid repair (PubMed:28596309)...

## Biological Role

Catalyzes (R)-lactate hydro-lyase (reaction.R09796). Component of protein/nucleic acid deglycase 1 (complex.ecocyc.CPLX0-861).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Protein and nucleotide deglycase that catalyzes the deglycation of the Maillard adducts formed between amino groups of proteins or nucleotides and reactive carbonyl groups of glyoxals (PubMed:26102038, PubMed:26774339, PubMed:28596309). Thus, functions as a protein deglycase that repairs methylglyoxal- and glyoxal-glycated proteins, and releases repaired proteins and lactate or glycolate, respectively. Deglycates cysteine, arginine and lysine residues in proteins, and thus reactivates these proteins by reversing glycation by glyoxals. Is able to repair glycated serum albumin, aspartate aminotransferase, glyceraldehyde-3-phosphate dehydrogenase, and fructose biphosphate aldolase. Acts on early glycation intermediates (hemithioacetals and aminocarbinols), preventing the formation of Schiff bases and advanced glycation endproducts (AGE) that cause irreversible damage (PubMed:26102038, PubMed:26774339). Also functions as a nucleotide deglycase able to repair glycated guanine in the free nucleotide pool (GTP, GDP, GMP, dGTP) and in DNA and RNA. Is thus involved in a major nucleotide repair system named guanine glycation repair (GG repair), dedicated to reversing methylglyoxal and glyoxal damage via nucleotide sanitization and direct nucleic acid repair (PubMed:28596309). Has been reported to display chaperone, peptidase and glutathione-independent glyoxalase activities (PubMed:12235139, PubMed:12565879, PubMed:14731284, PubMed:15550391, PubMed:21696459, PubMed:7848303). However, these apparently disparate activities are all recruited to execute its protein deglycase primary function (PubMed:26102038, PubMed:26774339). Plays an important role in protecting cells from carbonyl stress, severe heat shock and starvation, as well as in acid resistance of stationary-phase cells (PubMed:12235139, PubMed:16796689, PubMed:17158627). {ECO:0000269|PubMed:12235139, ECO:0000269|PubMed:12565879, ECO:0000269|PubMed:14731284, ECO:0000269|PubMed:15550391, ECO:0000269|PubMed:16796689, ECO:0000269|PubMed:17158627, ECO:0000269|PubMed:21696459, ECO:0000269|PubMed:26102038, ECO:0000269|PubMed:26774339, ECO:0000269|PubMed:28596309, ECO:0000269|PubMed:7848303}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R09796|reaction.R09796]] `KEGG` `database` - via EC:4.2.1.130
- `is_component_of` --> [[complex.ecocyc.CPLX0-861|complex.ecocyc.CPLX0-861]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1967|gene.b1967]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31658`
- `KEGG:ecj:JW1950;eco:b1967;ecoc:C3026_11115;`
- `GeneID:86946880;946481;`
- `GO:GO:0005737; GO:0005829; GO:0006281; GO:0008270; GO:0010447; GO:0016790; GO:0019172; GO:0019243; GO:0030091; GO:0036524; GO:0042245; GO:0042803; GO:0051595; GO:0106044`
- `EC:3.1.2.-; 3.5.1.-; 3.5.1.124; 4.2.1.130`

## Notes

Protein/nucleic acid deglycase 1 (EC 3.1.2.-) (EC 3.5.1.-) (EC 3.5.1.124) (Glyoxalase III) (EC 4.2.1.130) (Holding molecular chaperone) (Hsp31) (Maillard deglycase)
