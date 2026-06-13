---
entity_id: "protein.P52086"
entity_type: "protein"
name: "cobC"
source_database: "UniProt"
source_id: "P52086"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cobC phpB b0638 JW0633"
---

# cobC

`protein.P52086`

## Static

- Type: `protein`
- Source: `UniProt:P52086`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of adenosylcobalamin 5'-phosphate to adenosylcobalamin (vitamin B12); involved in the assembly of the nucleotide loop of cobalamin. Also catalyzes the hydrolysis of the phospho group from alpha-ribazole 5'-phosphate to form alpha-ribazole. {ECO:0000250|UniProtKB:P39701}. The CobC protein has not been characterised in E. coli K-12 but is predicted to be an adenosylcobalamin 5'-phosphate phosphatase by homology with cobC from Salmonella typhimurium. Early studies in S. typhimurium suggested that CobC was an α-ribazole phosphatase but more recently it was shown that adenosylcobalamin 5'-phosphate was the preferred substrate and that CobC catalyses the last step of adenosylcobalamin (coenzyme B12) biosynthesis .

## Biological Role

Catalyzes RXN-16788 (reaction.ecocyc.RXN-16788), RXN-8770 (reaction.ecocyc.RXN-8770).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of adenosylcobalamin 5'-phosphate to adenosylcobalamin (vitamin B12); involved in the assembly of the nucleotide loop of cobalamin. Also catalyzes the hydrolysis of the phospho group from alpha-ribazole 5'-phosphate to form alpha-ribazole. {ECO:0000250|UniProtKB:P39701}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-16788|reaction.ecocyc.RXN-16788]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-8770|reaction.ecocyc.RXN-8770]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0638|gene.b0638]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52086`
- `KEGG:ecj:JW0633;eco:b0638;ecoc:C3026_03190;`
- `GeneID:945246;`
- `GO:GO:0005737; GO:0009236; GO:0016791; GO:0043755`
- `EC:3.1.3.73`

## Notes

Adenosylcobalamin/alpha-ribazole phosphatase (EC 3.1.3.73) (Adenosylcobalamin phosphatase) (Alpha-ribazole-5'-phosphate phosphatase)
