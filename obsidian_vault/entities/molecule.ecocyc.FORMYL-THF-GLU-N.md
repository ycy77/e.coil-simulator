---
entity_id: "molecule.ecocyc.FORMYL-THF-GLU-N"
entity_type: "small_molecule"
name: "an N10-formyltetrahydrofolate"
source_database: "EcoCyc"
source_id: "FORMYL-THF-GLU-N"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "a 10-formyltetrahydrofolate"
---

# an N10-formyltetrahydrofolate

`molecule.ecocyc.FORMYL-THF-GLU-N`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:FORMYL-THF-GLU-N`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

THF-GLU-N Tetrahydrofolate (vitamin B9) and its derivatives, commonly termed folates, are required in a variety of reactions in both prokaryotes and eukaryotes, where they act as carriers of one-carbon units in various oxidation states. These one-carbon units are utilized in the biosynthesis of various cellular components, including glycine, methionine, formylmethionine, thymidylate, pantothenate and purine nucleotides. During folate biosynthesis (as described in FOLSYN-PWY) the enzyme EC-6.3.2.12, adds a glutamate residue to 7-8-DIHYDROPTEROATE, resulting in DIHYDROFOLATE, also known as H2PteGlu1. This molecule in turn is reduced by EC-1.5.1.3 (FolA) to THF (H4PteGlu1, or tetrahydrofolate), which can be converted to several other folate molecules . Most folate molecules are modified in cells by successive additions of glutamate residues, forming folate polyglutamates (or folylpoly-γ-glutamates). The glutamate residues are added by an amide linkage to the γ-carboxylate group of the folate or folate derivative. Since these isopeptide bonds are not the normal amide bonds they are not hydrolyzed by peptidases or proteases, which are specific for α-carboxyl-linked peptide bonds. The addition of glutamyl residues probably occurs after the reduction of newly synthesized dihydrofolate to tetrahydrofolate and its conversion to other tetrahydrofolate derivatives...

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 2 reaction(s).

## Annotation

THF-GLU-N Tetrahydrofolate (vitamin B9) and its derivatives, commonly termed folates, are required in a variety of reactions in both prokaryotes and eukaryotes, where they act as carriers of one-carbon units in various oxidation states. These one-carbon units are utilized in the biosynthesis of various cellular components, including glycine, methionine, formylmethionine, thymidylate, pantothenate and purine nucleotides. During folate biosynthesis (as described in FOLSYN-PWY) the enzyme EC-6.3.2.12, adds a glutamate residue to 7-8-DIHYDROPTEROATE, resulting in DIHYDROFOLATE, also known as H2PteGlu1. This molecule in turn is reduced by EC-1.5.1.3 (FolA) to THF (H4PteGlu1, or tetrahydrofolate), which can be converted to several other folate molecules . Most folate molecules are modified in cells by successive additions of glutamate residues, forming folate polyglutamates (or folylpoly-γ-glutamates). The glutamate residues are added by an amide linkage to the γ-carboxylate group of the folate or folate derivative. Since these isopeptide bonds are not the normal amide bonds they are not hydrolyzed by peptidases or proteases, which are specific for α-carboxyl-linked peptide bonds. The addition of glutamyl residues probably occurs after the reduction of newly synthesized dihydrofolate to tetrahydrofolate and its conversion to other tetrahydrofolate derivatives. The glutamylation of folate residues serves several goals: it prevents the efflux of folates out of the cell, it increases the binding of folate cofactors to the enzymes of folate interconversion and biosynthesis, and in mammals, it allows the accumulation of folates in the mitochondria, which is required for glycine synthesis . This class stands for 10-formyltetrahydrofolates with an unspecified number of glutamate res

## Outgoing Edges (8)

- `is_product_of` --> [[reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN|reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.METHENYLTHFCYCLOHYDRO-RXN|reaction.ecocyc.METHENYLTHFCYCLOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.AICARTRANSFORM-RXN|reaction.ecocyc.AICARTRANSFORM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FORMYLTHFDEFORMYL-RXN|reaction.ecocyc.FORMYLTHFDEFORMYL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN|reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GART-RXN|reaction.ecocyc.GART-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.METHIONYL-TRNA-FORMYLTRANSFERASE-RXN|reaction.ecocyc.METHIONYL-TRNA-FORMYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-1862|reaction.ecocyc.RXN0-1862]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:FORMYL-THF-GLU-N`
- `SEED:cpd27039`
- `METANETX:MNXM8615`
