---
entity_id: "molecule.C03541"
entity_type: "small_molecule"
name: "THF-polyglutamate"
source_database: "KEGG"
source_id: "C03541"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "THF-polyglutamate"
  - "Tetrahydropteroyl-[gamma-Glu]n"
  - "Tetrahydrofolyl-[Glu](n-1)"
  - "(6S)-H4PteGlu(n)"
  - "Tetrahydropteroyl-[gamma-Glu]n+1"
  - "Tetrahydrofolyl-[Glu](n)"
---

# THF-polyglutamate

`molecule.C03541`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03541`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: THF-polyglutamate; Tetrahydropteroyl-[gamma-Glu]n; Tetrahydrofolyl-[Glu](n-1); (6S)-H4PteGlu(n); Tetrahydropteroyl-[gamma-Glu]n+1; Tetrahydrofolyl-[Glu](n) EcoCyc common name: a tetrahydrofolate. THF-GLU-N Tetrahydrofolate (vitamin B9) and its derivatives, commonly termed folates, are required in a variety of reactions in both prokaryotes and eukaryotes, where they act as carriers of one-carbon units in various oxidation states. These one-carbon units are utilized in the biosynthesis of various cellular components, including glycine, methionine, formylmethionine, thymidylate, pantothenate and purine nucleotides. During folate biosynthesis (as described in FOLSYN-PWY) the enzyme EC-6.3.2.12, adds a glutamate residue to 7-8-DIHYDROPTEROATE, resulting in DIHYDROFOLATE, also known as H2PteGlu1. This molecule in turn is reduced by EC-1.5.1.3 (FolA) to THF (H4PteGlu1, or tetrahydrofolate), which can be converted to several other folate molecules . Most folate molecules are modified in cells by successive additions of glutamate residues, forming folate polyglutamates (or folylpoly-γ-glutamates). The glutamate residues are added by an amide linkage to the γ-carboxylate group of the folate or folate derivative...

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 10 reaction(s).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Annotation

KEGG compound: THF-polyglutamate; Tetrahydropteroyl-[gamma-Glu]n; Tetrahydrofolyl-[Glu](n-1); (6S)-H4PteGlu(n); Tetrahydropteroyl-[gamma-Glu]n+1; Tetrahydrofolyl-[Glu](n)

## Pathways

- `eco00790` Folate biosynthesis (KEGG)

## Outgoing Edges (15)

- `is_product_of` --> [[reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN|reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.AICARTRANSFORM-RXN|reaction.ecocyc.AICARTRANSFORM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN|reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.FORMYLTHFDEFORMYL-RXN|reaction.ecocyc.FORMYLTHFDEFORMYL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GART-RXN|reaction.ecocyc.GART-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYOHMETRANS-RXN|reaction.ecocyc.GLYOHMETRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.HOMOCYSMETB12-RXN|reaction.ecocyc.HOMOCYSMETB12-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.METHIONYL-TRNA-FORMYLTRANSFERASE-RXN|reaction.ecocyc.METHIONYL-TRNA-FORMYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21539|reaction.ecocyc.RXN-21539]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1862|reaction.ecocyc.RXN0-1862]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN|reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN|reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GCVMULTI-RXN|reaction.ecocyc.GCVMULTI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GCVT-RXN|reaction.ecocyc.GCVT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-2881|reaction.ecocyc.RXN-2881]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03541`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
