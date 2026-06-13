---
entity_id: "protein.P45470"
entity_type: "protein"
name: "yhbO"
source_database: "UniProt"
source_id: "P45470"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:16380269}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhbO b3153 JW5529"
---

# yhbO

`protein.P45470`

## Static

- Type: `protein`
- Source: `UniProt:P45470`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:16380269}.

## Enriched Summary

FUNCTION: Protein and nucleotide deglycase that catalyzes the deglycation of the Maillard adducts formed between amino groups of proteins or nucleotides and reactive carbonyl groups of glyoxals (PubMed:26774339, PubMed:28596309). Thus, functions as a protein deglycase that repairs methylglyoxal- and glyoxal-glycated proteins, and releases repaired proteins and lactate or glycolate, respectively. Deglycates cysteine, arginine and lysine residues in proteins, and thus reactivates these proteins by reversing glycation by glyoxals. Is able to repair glycated serum albumin, collagen, glyceraldehyde-3-phosphate dehydrogenase, and fructose biphosphate aldolase. Acts on early glycation intermediates (hemithioacetals and aminocarbinols), preventing the formation of advanced glycation endproducts (AGE) that cause irreversible damage (PubMed:26774339). Also functions as a nucleotide deglycase able to repair glycated guanine in the free nucleotide pool (GTP, GDP, GMP, dGTP) and in DNA and RNA. Is thus involved in a major nucleotide repair system named guanine glycation repair (GG repair), dedicated to reversing methylglyoxal and glyoxal damage via nucleotide sanitization and direct nucleic acid repair (PubMed:28596309)...

## Biological Role

Catalyzes GLYOXIII-RXN (reaction.ecocyc.GLYOXIII-RXN), RXN-17632 (reaction.ecocyc.RXN-17632).

## Annotation

FUNCTION: Protein and nucleotide deglycase that catalyzes the deglycation of the Maillard adducts formed between amino groups of proteins or nucleotides and reactive carbonyl groups of glyoxals (PubMed:26774339, PubMed:28596309). Thus, functions as a protein deglycase that repairs methylglyoxal- and glyoxal-glycated proteins, and releases repaired proteins and lactate or glycolate, respectively. Deglycates cysteine, arginine and lysine residues in proteins, and thus reactivates these proteins by reversing glycation by glyoxals. Is able to repair glycated serum albumin, collagen, glyceraldehyde-3-phosphate dehydrogenase, and fructose biphosphate aldolase. Acts on early glycation intermediates (hemithioacetals and aminocarbinols), preventing the formation of advanced glycation endproducts (AGE) that cause irreversible damage (PubMed:26774339). Also functions as a nucleotide deglycase able to repair glycated guanine in the free nucleotide pool (GTP, GDP, GMP, dGTP) and in DNA and RNA. Is thus involved in a major nucleotide repair system named guanine glycation repair (GG repair), dedicated to reversing methylglyoxal and glyoxal damage via nucleotide sanitization and direct nucleic acid repair (PubMed:28596309). In vitro, prevents acrylamide formation in asparagine/glyoxal and asparagine/sugar mixtures at 55 degrees Celsius, likely by degrading asparagine/glyoxal Maillard adducts formed at high temperatures (PubMed:27530919). Also displays an apparent glyoxalase activity that in fact reflects its deglycase activity (PubMed:26678554, PubMed:26774339). Is a general stress protein; is required for the protection of bacterial cells against many environmental stresses, including oxidative, thermal, osmotic, UV, and pH stresses (PubMed:17933887). And plays an important role in protection against electrophile/carbonyl stress (PubMed:26774339). {ECO:0000269|PubMed:17933887, ECO:0000269|PubMed:26678554, ECO:0000269|PubMed:26774339, ECO:0000269|PubMed:27530919, ECO:0000269|PubMed:28596309}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GLYOXIII-RXN|reaction.ecocyc.GLYOXIII-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17632|reaction.ecocyc.RXN-17632]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3153|gene.b3153]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45470`
- `KEGG:ecj:JW5529;eco:b3153;ecoc:C3026_17175;`
- `GeneID:75206008;947666;`
- `GO:GO:0005829; GO:0006281; GO:0006979; GO:0009268; GO:0009408; GO:0009411; GO:0019172; GO:0030091; GO:0036524; GO:0042802; GO:0106044`
- `EC:3.1.2.-; 3.5.1.-; 3.5.1.124`

## Notes

Protein/nucleic acid deglycase 2 (EC 3.1.2.-) (EC 3.5.1.-) (EC 3.5.1.124) (Maillard deglycase)
