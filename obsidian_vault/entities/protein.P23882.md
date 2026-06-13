---
entity_id: "protein.P23882"
entity_type: "protein"
name: "fmt"
source_database: "UniProt"
source_id: "P23882"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fmt yhdD b3288 JW3249"
---

# fmt

`protein.P23882`

## Static

- Type: `protein`
- Source: `UniProt:P23882`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Attaches a formyl group to the free amino group of methionyl-tRNA(fMet). The formyl group appears to play a dual role in the initiator identity of N-formylmethionyl-tRNA by promoting its recognition by IF2 and preventing the misappropriation of this tRNA by the elongation apparatus. {ECO:0000255|HAMAP-Rule:MF_00182, ECO:0000269|PubMed:6989606, ECO:0000269|PubMed:8331078, ECO:0000269|PubMed:9843487}. 10-formyltetrahydrofolate:L-methionyl-tRNAfMet N-formyltransferase (Fmt) attaches a formyl group to the free amino group of methionyl-tRNAfMet . There are two types of methionine-specific tRNAs in E. coli; the Initiation-tRNAmet is used in the initiation of translation, while Elongation-tRNAMet is used during peptide chain elongation. The timely formylation of the methionine-charged initiator tRNA that is catalyzed by Fmt is important in restricting the use of the methionylated initiator tRNA specifically for initiation, rather than chain elongation . While the specific biological function of the formylated N-terminal fMet residue in proteins is still being studied, it has been shown that N-terminal fMet can act as a co-translational degradation signal , and formylation has been shown to be important in the fidelity of translation initiation...

## Biological Role

Catalyzes METHIONYL-TRNA-FORMYLTRANSFERASE-RXN (reaction.ecocyc.METHIONYL-TRNA-FORMYLTRANSFERASE-RXN), RXN0-7422 (reaction.ecocyc.RXN0-7422). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Attaches a formyl group to the free amino group of methionyl-tRNA(fMet). The formyl group appears to play a dual role in the initiator identity of N-formylmethionyl-tRNA by promoting its recognition by IF2 and preventing the misappropriation of this tRNA by the elongation apparatus. {ECO:0000255|HAMAP-Rule:MF_00182, ECO:0000269|PubMed:6989606, ECO:0000269|PubMed:8331078, ECO:0000269|PubMed:9843487}.

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.METHIONYL-TRNA-FORMYLTRANSFERASE-RXN|reaction.ecocyc.METHIONYL-TRNA-FORMYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7422|reaction.ecocyc.RXN0-7422]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3288|gene.b3288]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23882`
- `KEGG:ecj:JW3249;eco:b3288;ecoc:C3026_17875;`
- `GeneID:947779;`
- `GO:GO:0004479; GO:0005829; GO:0019988; GO:0071951`
- `EC:2.1.2.9`

## Notes

Methionyl-tRNA formyltransferase (EC 2.1.2.9) (Met-tRNA(fMet) formyltransferase)
