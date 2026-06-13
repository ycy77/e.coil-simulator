---
entity_id: "molecule.ecocyc.METHYLENE-THF-GLU-N"
entity_type: "small_molecule"
name: "a 5,10-methylenetetrahydrofolate"
source_database: "EcoCyc"
source_id: "METHYLENE-THF-GLU-N"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "(-)CH2H4folate"
  - "(-)5,10-methylene-5,6,7,8-tetrahydrofolate"
  - "methylene-H4PteGlu(n)"
  - "methylene-THF(glu)n"
  - "methylene-H4PteGlun"
  - "methylene-tetrahydropteroylpolyglutamates"
---

# a 5,10-methylenetetrahydrofolate

`molecule.ecocyc.METHYLENE-THF-GLU-N`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:METHYLENE-THF-GLU-N`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

THF-GLU-N Tetrahydrofolate (vitamin B9) and its derivatives, commonly termed folates, are required in a variety of reactions in both prokaryotes and eukaryotes, where they act as carriers of one-carbon units in various oxidation states. These one-carbon units are utilized in the biosynthesis of various cellular components, including glycine, methionine, formylmethionine, thymidylate, pantothenate and purine nucleotides. During folate biosynthesis (as described in FOLSYN-PWY) the enzyme EC-6.3.2.12, adds a glutamate residue to 7-8-DIHYDROPTEROATE, resulting in DIHYDROFOLATE, also known as H2PteGlu1. This molecule in turn is reduced by EC-1.5.1.3 (FolA) to THF (H4PteGlu1, or tetrahydrofolate), which can be converted to several other folate molecules . Most folate molecules are modified in cells by successive additions of glutamate residues, forming folate polyglutamates (or folylpoly-γ-glutamates). The glutamate residues are added by an amide linkage to the γ-carboxylate group of the folate or folate derivative. Since these isopeptide bonds are not the normal amide bonds they are not hydrolyzed by peptidases or proteases, which are specific for α-carboxyl-linked peptide bonds. The addition of glutamyl residues probably occurs after the reduction of newly synthesized dihydrofolate to tetrahydrofolate and its conversion to other tetrahydrofolate derivatives...

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 6 reaction(s).

## Annotation

THF-GLU-N Tetrahydrofolate (vitamin B9) and its derivatives, commonly termed folates, are required in a variety of reactions in both prokaryotes and eukaryotes, where they act as carriers of one-carbon units in various oxidation states. These one-carbon units are utilized in the biosynthesis of various cellular components, including glycine, methionine, formylmethionine, thymidylate, pantothenate and purine nucleotides. During folate biosynthesis (as described in FOLSYN-PWY) the enzyme EC-6.3.2.12, adds a glutamate residue to 7-8-DIHYDROPTEROATE, resulting in DIHYDROFOLATE, also known as H2PteGlu1. This molecule in turn is reduced by EC-1.5.1.3 (FolA) to THF (H4PteGlu1, or tetrahydrofolate), which can be converted to several other folate molecules . Most folate molecules are modified in cells by successive additions of glutamate residues, forming folate polyglutamates (or folylpoly-γ-glutamates). The glutamate residues are added by an amide linkage to the γ-carboxylate group of the folate or folate derivative. Since these isopeptide bonds are not the normal amide bonds they are not hydrolyzed by peptidases or proteases, which are specific for α-carboxyl-linked peptide bonds. The addition of glutamyl residues probably occurs after the reduction of newly synthesized dihydrofolate to tetrahydrofolate and its conversion to other tetrahydrofolate derivatives. The glutamylation of folate residues serves several goals: it prevents the efflux of folates out of the cell, it increases the binding of folate cofactors to the enzymes of folate interconversion and biosynthesis, and in mammals, it allows the accumulation of folates in the mitochondria, which is required for glycine synthesis . This class stands for 5,10-methylene-tetrahydrofolates with an unspecified number of glutama

## Outgoing Edges (15)

- `is_product_of` --> [[reaction.ecocyc.1.5.1.20-RXN|reaction.ecocyc.1.5.1.20-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GCVMULTI-RXN|reaction.ecocyc.GCVMULTI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GCVT-RXN|reaction.ecocyc.GCVT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22438|reaction.ecocyc.RXN-22438]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-2881|reaction.ecocyc.RXN-2881]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2921|reaction.ecocyc.RXN0-2921]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN|reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GLYOHMETRANS-RXN|reaction.ecocyc.GLYOHMETRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN|reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18710|reaction.ecocyc.RXN-18710]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2921|reaction.ecocyc.RXN0-2921]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7068|reaction.ecocyc.RXN0-7068]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7083|reaction.ecocyc.RXN0-7083]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THYMIDYLATESYN-RXN|reaction.ecocyc.THYMIDYLATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.THYMIDYLATESYN-RXN|reaction.ecocyc.THYMIDYLATESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:METHYLENE-THF-GLU-N`
- `SEED:cpd27449`
- `METANETX:MNXM162297`
