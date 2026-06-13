---
entity_id: "protein.P0AFU8"
entity_type: "protein"
name: "ribC"
source_database: "UniProt"
source_id: "P0AFU8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ribC ribE b1662 JW1654"
---

# ribC

`protein.P0AFU8`

## Static

- Type: `protein`
- Source: `UniProt:P0AFU8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dismutation of two molecules of 6,7-dimethyl-8-ribityllumazine, resulting in the formation of riboflavin and 5-amino-6-(D-ribitylamino)uracil. {ECO:0000269|PubMed:9022701}. Riboflavin synthase catalyzes the final step in riboflavin biosynthesis, the formation of the carbocyclic ring of riboflavin by dismutation of 6,7-dimethyl-8-ribityllumazine. No homolog of this enzyme exists in humans, and it is therefore an attractive target for antimicrobial agents against microbes that are dependent on endogenous synthesis of riboflavin. Inhibitors of riboflavin synthase with antibiotic activity have been developed, e.g. . A recombinant N-terminal domain fragment dimerizes and is able to bind riboflavin . Catalytically relevant amino acid residues have been identified by mutagenesis . A kinetically competent reaction intermediate has been identified , and the enzyme kinetics have been studied under single turnover conditions . A new, simpler mechanism for formation of the pentacyclic reaction intermediate via hydryde transfer has been proposed . Riboflavin synthase is a homotrimer in solution . Solution and crystal structures of N-terminal riboflavin-binding domain fragments and the homotrimeric enzyme have been solved. Each subunit consists of two similarly-folding domains . ribC is an essential gene . Review:

## Biological Role

Catalyzes 6,7-dimethyl-8-(1-D-ribityl)lumazine:6,7-dimethyl-8-(1-D-ribityl)lumazine 2,3-butanediyltransferase (reaction.R00066). Component of riboflavin synthase (complex.ecocyc.CPLX0-3952).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the dismutation of two molecules of 6,7-dimethyl-8-ribityllumazine, resulting in the formation of riboflavin and 5-amino-6-(D-ribitylamino)uracil. {ECO:0000269|PubMed:9022701}.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00066|reaction.R00066]] `KEGG` `database` - via EC:2.5.1.9
- `is_component_of` --> [[complex.ecocyc.CPLX0-3952|complex.ecocyc.CPLX0-3952]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b1662|gene.b1662]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFU8`
- `KEGG:ecj:JW1654;eco:b1662;ecoc:C3026_09535;`
- `GeneID:93775817;945848;`
- `GO:GO:0004746; GO:0005829; GO:0009231`
- `EC:2.5.1.9`

## Notes

Riboflavin synthase (RS) (EC 2.5.1.9)
