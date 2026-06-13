---
entity_id: "protein.P36999"
entity_type: "protein"
name: "rlmA"
source_database: "UniProt"
source_id: "P36999"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmA rrmA yebH b1822 JW1811"
---

# rlmA

`protein.P36999`

## Static

- Type: `protein`
- Source: `UniProt:P36999`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Specifically methylates the guanosine in position 745 of 23S rRNA. {ECO:0000269|PubMed:9440525}. RlmA is the methyltransferase responsible for methylation of 23S rRNA at the N1 position of the G745 nucleotide. RlmA activity is required for wild-type translation and cell growth . The methylated base is expected to reside near the peptide exit channel in the context of the ribosome . In vitro, RlmA is able to methylate free 23S rRNA, but not assembled 50S ribosomal subunits or 70S ribosomes. A 92 nt fragment of 23S rRNA consisting of stem-loops 33, 34 and 35 is efficiently methylated . Specificity for the target nucleotide is determined by the methyltransferase rather than the rRNA substrate . The location of the SAM-binding region and catalytic site have been predicted . RlmA is predicted to have an N-terminal zinc finger and a C-terminal substrate recognition region . The crystal structure of RlmA has been determined at 2.8 Å resolution, and RlmA appears to be an asymmetric dimer. The Zn2+-binding domains may be responsible for RNA recognition and binding . An rlmA mutant lacks 1-methylguanine in its rRNA . rlmA mutants exhibit defects in translation, a decreased growth rate even in rich medium, and increased resistance to the antibiotic viomycin...

## Biological Role

Catalyzes RXN-11573 (reaction.ecocyc.RXN-11573). Bound by Zinc cation (molecule.C00038).

## Annotation

FUNCTION: Specifically methylates the guanosine in position 745 of 23S rRNA. {ECO:0000269|PubMed:9440525}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11573|reaction.ecocyc.RXN-11573]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1822|gene.b1822]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36999`
- `KEGG:ecj:JW1811;eco:b1822;ecoc:C3026_10380;`
- `GeneID:946340;`
- `GO:GO:0008168; GO:0008270; GO:0008989; GO:0052911; GO:0070475`
- `EC:2.1.1.187`

## Notes

23S rRNA (guanine(745)-N(1))-methyltransferase (EC 2.1.1.187) (23S rRNA m1G745 methyltransferase) (Ribosomal RNA large subunit methyltransferase A)
