---
entity_id: "protein.P77580"
entity_type: "protein"
name: "mhpF"
source_database: "UniProt"
source_id: "P77580"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mhpF mhpE b0351 JW0342"
---

# mhpF

`protein.P77580`

## Static

- Type: `protein`
- Source: `UniProt:P77580`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of acetaldehyde to acetyl-CoA, using NAD(+) and coenzyme A. Is the final enzyme in the meta-cleavage pathway for the degradation of 3-phenylpropanoate. Functions as a chaperone protein for folding of MhpE. {ECO:0000269|PubMed:16782065}. mhpF encodes an acetylating acetaldehyde dehydrogenase . MhpF is active as a monomer; the rate-limiting step of the reaction appears to be transthioesterification . MhpF is involved in synthesis of n-butanol in an engineered reversal of the β-oxidation pathway . The expression of MhpE is translationally coupled to MhpF, and interaction between the two proteins appears to be required for solubility of MhpE .

## Biological Role

Catalyzes acetaldehyde:NAD+ oxidoreductase (CoA-acetylating) (reaction.R00228), ACETALD-DEHYDROG-RXN (reaction.ecocyc.ACETALD-DEHYDROG-RXN).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of acetaldehyde to acetyl-CoA, using NAD(+) and coenzyme A. Is the final enzyme in the meta-cleavage pathway for the degradation of 3-phenylpropanoate. Functions as a chaperone protein for folding of MhpE. {ECO:0000269|PubMed:16782065}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00228|reaction.R00228]] `KEGG` `database` - via EC:1.2.1.10
- `catalyzes` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0351|gene.b0351]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77580`
- `KEGG:ecj:JW0342;eco:b0351;ecoc:C3026_24890;`
- `GeneID:93777104;945008;`
- `GO:GO:0008774; GO:0019380; GO:0051287`
- `EC:1.2.1.10`

## Notes

Acetaldehyde dehydrogenase (EC 1.2.1.10) (Acetaldehyde dehydrogenase [acetylating])
