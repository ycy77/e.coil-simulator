---
entity_id: "protein.P0AE22"
entity_type: "protein"
name: "aphA"
source_database: "UniProt"
source_id: "P0AE22"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:9011040}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aphA napA yjbP b4055 JW4015"
---

# aphA

`protein.P0AE22`

## Static

- Type: `protein`
- Source: `UniProt:P0AE22`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:9011040}.

## Enriched Summary

FUNCTION: Dephosphorylates several organic phosphate monoesters including 3'- and 5'-nucleotides, 2'-deoxy-5'-nucleotides, pNPP, phenyl phosphate, glycerol 2-phosphate, ribose 5-phosphate, O-phospho-L-amino acids and phytic acid, showing the highest activity with aryl phosphoesters (pNPP, phenyl phosphate and O-phospho-L-tyrosine), and to a lesser extent with 3'- and 5'-nucleotides. No activity toward ATP, phosphodiesters, glycerol-1-phosphate, glucose 1-phosphate, glucose 6-phosphate, NADP, GTP or 3',5'-cAMP, ADP or ATP. Also has a phosphotransferase activity catalyzing the transfer of low-energy phosphate groups from organic phosphate monoesters to free hydroxyl groups of various organic compounds. Capable of transferring phosphate from either pNPP or UMP to adenosine or uridine. Does not exhibit nucleotide phosphomutase activity. {ECO:0000269|PubMed:16297670, ECO:0000269|PubMed:9011040}. aphA encodes a periplasmic phosphatase/phosphotransferase that has optimal activity at acidic pH. The purified enzyme is able to dephosphorylate 5' and 3' mononucleotides, 2-deoxy 5' nucleotides, phenylphosphate, glycerol-2-phosphate, ribose-5-phosphate, O-phospho-L-amino acids (O-phospho-L-serine, O-phospho-L-threonine and O-phospho-L-tyrosine) and phytic acid. No activity was observed on ATP, phosphodiesters, glycerol-1-phosphate, glucose-1-phosphate or glucose-6-phosphate...

## Biological Role

Catalyzes riboflavin-5-phosphate phosphohydrolase (reaction.R00548), phosphate-monoester phosphohydrolase (reaction.R00626), glycerone phosphate phosphohydrolase (reaction.R01010), thiamin monophosphate phosphohydrolase (reaction.R02135), 1-acyl-sn-glycerol 3-phosphate phosphohydrolase (reaction.R11527). Component of acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Dephosphorylates several organic phosphate monoesters including 3'- and 5'-nucleotides, 2'-deoxy-5'-nucleotides, pNPP, phenyl phosphate, glycerol 2-phosphate, ribose 5-phosphate, O-phospho-L-amino acids and phytic acid, showing the highest activity with aryl phosphoesters (pNPP, phenyl phosphate and O-phospho-L-tyrosine), and to a lesser extent with 3'- and 5'-nucleotides. No activity toward ATP, phosphodiesters, glycerol-1-phosphate, glucose 1-phosphate, glucose 6-phosphate, NADP, GTP or 3',5'-cAMP, ADP or ATP. Also has a phosphotransferase activity catalyzing the transfer of low-energy phosphate groups from organic phosphate monoesters to free hydroxyl groups of various organic compounds. Capable of transferring phosphate from either pNPP or UMP to adenosine or uridine. Does not exhibit nucleotide phosphomutase activity. {ECO:0000269|PubMed:16297670, ECO:0000269|PubMed:9011040}.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R00548|reaction.R00548]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` --> [[reaction.R00626|reaction.R00626]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` --> [[reaction.R01010|reaction.R01010]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` --> [[reaction.R02135|reaction.R02135]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` --> [[reaction.R11527|reaction.R11527]] `KEGG` `database` - via EC:3.1.3.2
- `is_component_of` --> [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b4055|gene.b4055]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE22`
- `KEGG:ecj:JW4015;eco:b4055;ecoc:C3026_21915;`
- `GeneID:948562;`
- `GO:GO:0000287; GO:0003993; GO:0030288; GO:0036424; GO:0042802`
- `EC:3.1.3.2`

## Notes

Class B acid phosphatase (CBAP) (EC 3.1.3.2)
