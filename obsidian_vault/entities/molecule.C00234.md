---
entity_id: "molecule.C00234"
entity_type: "small_molecule"
name: "10-Formyltetrahydrofolate"
source_database: "KEGG"
source_id: "C00234"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "10-Formyltetrahydrofolate"
  - "10-Formyl-THF"
---

# 10-Formyltetrahydrofolate

`molecule.C00234`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00234`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 10-Formyltetrahydrofolate; 10-Formyl-THF EcoCyc common name: 10-formyl-tetrahydrofolate mono-L-glutamate. THF-GLU-N Tetrahydrofolate (vitamin B9) and its derivatives, commonly termed folates, are required in a variety of reactions in both prokaryotes and eukaryotes, where they act as carriers of one-carbon units in various oxidation states. These one-carbon units are utilized in the biosynthesis of various cellular components, including glycine, methionine, formylmethionine, thymidylate, pantothenate and purine nucleotides. During folate biosynthesis (as described in FOLSYN-PWY) the enzyme EC-6.3.2.12, adds a glutamate residue to 7-8-DIHYDROPTEROATE, resulting in DIHYDROFOLATE, also known as H2PteGlu1. This molecule in turn is reduced by EC-1.5.1.3 (FolA) to THF (H4PteGlu1, or tetrahydrofolate), which can be converted to several other folate molecules . Most folate molecules are modified in cells by successive additions of glutamate residues, forming folate polyglutamates (or folylpoly-γ-glutamates). The glutamate residues are added by an amide linkage to the γ-carboxylate group of the folate or folate derivative. Since these isopeptide bonds are not the normal amide bonds they are not hydrolyzed by peptidases or proteases, which are specific for α-carboxyl-linked peptide bonds...

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

KEGG compound: 10-Formyltetrahydrofolate; 10-Formyl-THF

## Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (2)

- `represses` --> [[reaction.ecocyc.METHENYLTHFCYCLOHYDRO-RXN|reaction.ecocyc.METHENYLTHFCYCLOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN|reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00234`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
