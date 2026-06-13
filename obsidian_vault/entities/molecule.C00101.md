---
entity_id: "molecule.C00101"
entity_type: "small_molecule"
name: "Tetrahydrofolate"
source_database: "KEGG"
source_id: "C00101"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Tetrahydrofolate"
  - "5,6,7,8-Tetrahydrofolate"
  - "Tetrahydrofolic acid"
  - "THF"
  - "(6S)-Tetrahydrofolate"
  - "(6S)-Tetrahydrofolic acid"
  - "(6S)-THFA"
---

# Tetrahydrofolate

`molecule.C00101`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00101`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Tetrahydrofolate; 5,6,7,8-Tetrahydrofolate; Tetrahydrofolic acid; THF; (6S)-Tetrahydrofolate; (6S)-Tetrahydrofolic acid; (6S)-THFA EcoCyc common name: 5,6,7,8-tetrahydrofolate. THF-GLU-N Tetrahydrofolate (vitamin B9) and its derivatives, commonly termed folates, are required in a variety of reactions in both prokaryotes and eukaryotes, where they act as carriers of one-carbon units in various oxidation states. These one-carbon units are utilized in the biosynthesis of various cellular components, including glycine, methionine, formylmethionine, thymidylate, pantothenate and purine nucleotides. During folate biosynthesis (as described in FOLSYN-PWY) the enzyme EC-6.3.2.12, adds a glutamate residue to 7-8-DIHYDROPTEROATE, resulting in DIHYDROFOLATE, also known as H2PteGlu1. This molecule in turn is reduced by EC-1.5.1.3 (FolA) to THF (H4PteGlu1, or tetrahydrofolate), which can be converted to several other folate molecules . Most folate molecules are modified in cells by successive additions of glutamate residues, forming folate polyglutamates (or folylpoly-γ-glutamates). The glutamate residues are added by an amide linkage to the γ-carboxylate group of the folate or folate derivative. Since these isopeptide bonds are not the normal amide bonds they are not hydrolyzed by peptidases or proteases, which are specific for α-carboxyl-linked peptide bonds...

## Biological Role

Consumed as substrate in 2 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: Tetrahydrofolate; 5,6,7,8-Tetrahydrofolate; Tetrahydrofolic acid; THF; (6S)-Tetrahydrofolate; (6S)-Tetrahydrofolic acid; (6S)-THFA

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (4)

- `activates` --> [[reaction.ecocyc.DSERDEAM-RXN|reaction.ecocyc.DSERDEAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_substrate_of` --> [[reaction.R04125|reaction.R04125]] `KEGG` `database` - C01242 + C00101 <=> C02972 + C00143 + C00014
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19329|reaction.ecocyc.RXN-19329]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN|reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00101`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
