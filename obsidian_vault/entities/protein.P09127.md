---
entity_id: "protein.P09127"
entity_type: "protein"
name: "hemX"
source_database: "UniProt"
source_id: "P09127"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Single-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemX b3803 JW3775"
---

# hemX

`protein.P09127`

## Static

- Type: `protein`
- Source: `UniProt:P09127`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Single-pass membrane protein {ECO:0000255}.

## Enriched Summary

Protein HemX (ORF X) The HemX protein was suggested to be a uroporphyrinogen III methylase . However, the function of the protein has not been experimentally determined. HemX exists as a homooligomer in the inner membrane . HemX is predicted to be a bitopic inner membrane protein .

## Biological Role

Catalyzes S-adenosyl-L-methionine:uroporphyrinogen-III C-methyltransferase (reaction.R03194).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

Protein HemX (ORF X)

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R03194|reaction.R03194]] `KEGG` `database` - via EC:2.1.1.107

## Incoming Edges (1)

- `encodes` <-- [[gene.b3803|gene.b3803]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09127`
- `KEGG:ecj:JW3775;eco:b3803;`
- `GeneID:948446;`
- `GO:GO:0005886`

## Notes

Protein HemX (ORF X)
