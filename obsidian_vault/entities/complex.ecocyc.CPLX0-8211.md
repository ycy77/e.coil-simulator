---
entity_id: "complex.ecocyc.CPLX0-8211"
entity_type: "complex"
name: "hydroxyethylthiazole kinase"
source_database: "EcoCyc"
source_id: "CPLX0-8211"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# hydroxyethylthiazole kinase

`complex.ecocyc.CPLX0-8211`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8211`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P76423|protein.P76423]]

## Enriched Summary

Hydroxyethylthiazole kinase (ThiM) catalyzes the ATP-dependent phosphorylation of 4-methyl-5-(β-hydroxyethyl)thiazole to generate 4-methyl-5-(β-hydroxyethyl)thiazole phosphate, a reaction in the PWY-6897 pathway . The E. coli enzyme has only recently been purified . ThiM was also shown to have isopentenol kinase activity; the product DMAP is used by UBIX-MONOMER UbiX-like proteins to generate the prenylated FMN cofactor . Both the marine organism Ostreococcus tauri and E. coli can utilize 5-(2-hydroxyethyl)-4-methyl-1,3-thiazole-2-carboxylic acid (cHET) as a precursor for thiamine biosynthesis. In O. tauri, utilization was dependent on thiM . thiM mRNA contains a riboswitch that binds to the thiamine biosynthesis pathway product thiamine pyrophosphate (TPP) . This interaction has been examined via NMR and crystal structures . The secondary structure of the thiM riboswitch in its TPP-free and -bound form has been reported , and TPP-induced folding has been investigated . Mutations of conserved bases in the riboswitch domain enabled confirmation of nucleotides involved in TPP recognition . A method to screen for compounds that bind the riboswitch region has been developed and used to study the riboswitch ligand interactions . TPP-dependent conformational changes elucidated the relationship between ligand recognition and aptamer folding...

## Biological Role

Catalyzes RXN-23965 (reaction.ecocyc.RXN-23965), RXN0-7298 (reaction.ecocyc.RXN0-7298), THIAZOLSYN3-RXN (reaction.ecocyc.THIAZOLSYN3-RXN). Bound by Cobalt ion (molecule.C00175), Magnesium cation (molecule.C00305).

## Annotation

Hydroxyethylthiazole kinase (ThiM) catalyzes the ATP-dependent phosphorylation of 4-methyl-5-(β-hydroxyethyl)thiazole to generate 4-methyl-5-(β-hydroxyethyl)thiazole phosphate, a reaction in the PWY-6897 pathway . The E. coli enzyme has only recently been purified . ThiM was also shown to have isopentenol kinase activity; the product DMAP is used by UBIX-MONOMER UbiX-like proteins to generate the prenylated FMN cofactor . Both the marine organism Ostreococcus tauri and E. coli can utilize 5-(2-hydroxyethyl)-4-methyl-1,3-thiazole-2-carboxylic acid (cHET) as a precursor for thiamine biosynthesis. In O. tauri, utilization was dependent on thiM . thiM mRNA contains a riboswitch that binds to the thiamine biosynthesis pathway product thiamine pyrophosphate (TPP) . This interaction has been examined via NMR and crystal structures . The secondary structure of the thiM riboswitch in its TPP-free and -bound form has been reported , and TPP-induced folding has been investigated . Mutations of conserved bases in the riboswitch domain enabled confirmation of nucleotides involved in TPP recognition . A method to screen for compounds that bind the riboswitch region has been developed and used to study the riboswitch ligand interactions . TPP-dependent conformational changes elucidated the relationship between ligand recognition and aptamer folding . Real-time monitoring of riboswitch folding by single-molecule FRET showed that the aptamer initially folds in the "off" conformation even in the absence of TPP; a transcriptional pause site near the initiation codon enhances the transition to the "on" conformation during transcription of the 5' UTR to the ribosome binding site. TPP binding inhibits this transition to the "on" conformation . The thiM riboswitch was shown to be kinetically

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-23965|reaction.ecocyc.RXN-23965]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7298|reaction.ecocyc.RXN0-7298]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THIAZOLSYN3-RXN|reaction.ecocyc.THIAZOLSYN3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76423|protein.P76423]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8211`
- `QSPROTEOME:QS00196507`

## Notes

2*protein.P76423
