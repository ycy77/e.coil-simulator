---
entity_id: "molecule.C00143"
entity_type: "small_molecule"
name: "5,10-Methylenetetrahydrofolate"
source_database: "KEGG"
source_id: "C00143"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5,10-Methylenetetrahydrofolate"
  - "(6R)-5,10-Methylenetetrahydrofolate"
  - "5,10-Methylene-THF"
---

# 5,10-Methylenetetrahydrofolate

`molecule.C00143`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00143`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5,10-Methylenetetrahydrofolate; (6R)-5,10-Methylenetetrahydrofolate; 5,10-Methylene-THF EcoCyc common name: 5,10-methylenetetrahydropteroyl mono-L-glutamate. THF-GLU-N Tetrahydrofolate (vitamin B9) and its derivatives, commonly termed folates, are required in a variety of reactions in both prokaryotes and eukaryotes, where they act as carriers of one-carbon units in various oxidation states. These one-carbon units are utilized in the biosynthesis of various cellular components, including glycine, methionine, formylmethionine, thymidylate, pantothenate and purine nucleotides. During folate biosynthesis (as described in FOLSYN-PWY) the enzyme EC-6.3.2.12, adds a glutamate residue to 7-8-DIHYDROPTEROATE, resulting in DIHYDROFOLATE, also known as H2PteGlu1. This molecule in turn is reduced by EC-1.5.1.3 (FolA) to THF (H4PteGlu1, or tetrahydrofolate), which can be converted to several other folate molecules . Most folate molecules are modified in cells by successive additions of glutamate residues, forming folate polyglutamates (or folylpoly-γ-glutamates). The glutamate residues are added by an amide linkage to the γ-carboxylate group of the folate or folate derivative. Since these isopeptide bonds are not the normal amide bonds they are not hydrolyzed by peptidases or proteases, which are specific for α-carboxyl-linked peptide bonds...

## Biological Role

Produced in 1 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: 5,10-Methylenetetrahydrofolate; (6R)-5,10-Methylenetetrahydrofolate; 5,10-Methylene-THF

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (1)

- `is_product_of` --> [[reaction.R04125|reaction.R04125]] `KEGG` `database` - C01242 + C00101 <=> C02972 + C00143 + C00014

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00143`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
