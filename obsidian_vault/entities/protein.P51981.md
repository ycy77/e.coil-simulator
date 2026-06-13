---
entity_id: "protein.P51981"
entity_type: "protein"
name: "ycjG"
source_database: "UniProt"
source_id: "P51981"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycjG ycjH b1325 JW1318"
---

# ycjG

`protein.P51981`

## Static

- Type: `protein`
- Source: `UniProt:P51981`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the epimerization of L-Ala-D-Glu to L-Ala-L-Glu and has a role in the recycling of the murein peptide, of which L-Ala-D-Glu is a component. Is also able to catalyze the reverse reaction and the epimerization of all the L-Ala-X dipeptides, except L-Ala-L-Arg, L-Ala-L-Lys and L-Ala-L-Pro. Is also active with L-Gly-L-Glu, L-Phe-L-Glu, and L-Ser-L-Glu, but not with L-Glu-L-Glu, L-Lys-L-Glu, L-Pro-L-Glu, L-Lys-L-Ala, or D-Ala-D-Ala. {ECO:0000269|PubMed:11747447, ECO:0000269|PubMed:18535144}. YcjG is an L-Ala-D/L-Glu epimerase that may play a role in the metabolism of murein peptide. The substrate specificity of the enzyme is not strict. YcjG belongs to the MLE subfamily of the enolase family of enzymes . The crystal structure of YcjG has been solved at 2.6 Å resolution. Although YcjG behaves like a monomer in solution, the crystal structure shows extensive surface contacts between two monomers . A D297G mutant can catalyze both the wild-type reaction as well as the o-succinylbenzoate synthase reaction; thus this substitution relaxes the substrate specificity of the enzyme. O-succinylbenzoate synthase activity of the mutant is sufficient to partially rescue the growth defect of the o-succinylbenzoate synthase-deficient menC mutant under anaerobic growth conditions...

## Biological Role

Catalyzes L-alanyl-D-glutamate epimerase (reaction.R10938), N-acetyl-glutamate racemase (reaction.R13097), RXN0-5228 (reaction.ecocyc.RXN0-5228).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the epimerization of L-Ala-D-Glu to L-Ala-L-Glu and has a role in the recycling of the murein peptide, of which L-Ala-D-Glu is a component. Is also able to catalyze the reverse reaction and the epimerization of all the L-Ala-X dipeptides, except L-Ala-L-Arg, L-Ala-L-Lys and L-Ala-L-Pro. Is also active with L-Gly-L-Glu, L-Phe-L-Glu, and L-Ser-L-Glu, but not with L-Glu-L-Glu, L-Lys-L-Glu, L-Pro-L-Glu, L-Lys-L-Ala, or D-Ala-D-Ala. {ECO:0000269|PubMed:11747447, ECO:0000269|PubMed:18535144}.

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R10938|reaction.R10938]] `KEGG` `database` - via EC:5.1.1.20
- `catalyzes` --> [[reaction.R13097|reaction.R13097]] `KEGG` `database` - via EC:5.1.1.25
- `catalyzes` --> [[reaction.ecocyc.RXN0-5228|reaction.ecocyc.RXN0-5228]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1325|gene.b1325]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P51981`
- `KEGG:ecj:JW1318;eco:b1325;ecoc:C3026_07755;`
- `GeneID:946013;`
- `GO:GO:0006518; GO:0009063; GO:0009254; GO:0016854; GO:0016855; GO:0046872; GO:0071555; GO:0103031`
- `EC:5.1.1.20`

## Notes

L-Ala-D/L-Glu epimerase (AE epimerase) (AEE) (EC 5.1.1.20)
