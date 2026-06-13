---
entity_id: "protein.P0A6L0"
entity_type: "protein"
name: "deoC"
source_database: "UniProt"
source_id: "P0A6L0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00592, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "deoC dra thyR b4381 JW4344"
---

# deoC

`protein.P0A6L0`

## Static

- Type: `protein`
- Source: `UniProt:P0A6L0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00592, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes a reversible aldol reaction between acetaldehyde and D-glyceraldehyde 3-phosphate to generate 2-deoxy-D-ribose 5-phosphate (PubMed:11598300, PubMed:17905878, PubMed:6749498). Can also catalyze the double aldol condensation of three acetaldehyde molecules, leading to the formation of 2,4,6-trideoxyhexose (Ref.5). {ECO:0000269|PubMed:11598300, ECO:0000269|PubMed:17905878, ECO:0000269|PubMed:6749498, ECO:0000269|Ref.5}. DeoC is a deoxyribose-phosphate aldolase which is part of the pathway that utilizes pyrimidine deoxyribonucleoside as a carbon and energy source. Deoxyribose-phosphate aldolase catalyzes the aldol reaction between the acetaldehyde donor and glyceraldehyde 3-phosphate acceptor to generate deoxyribose 5-phosphate. It belongs to the class I aldolases which form Schiff base intermediates. The purified enzyme may exist as both a monomer and a dimer. The enzyme exists as a monomer in Tris/HCl containing EDTA and as a dimer in phosphate buffer. The crystal structure of a covalent complex of deoxyribose phosphate aldolase with deoxyribose 5-phosphate was resolved to 1.05 Å. Site directed mutagenesis of the Schiff base Lys167 and Lys201 were found to be critical to catalysis. Mutations in deoC suppressed thymine requirement for growth in thymidylate synthase (thyA) mutants...

## Biological Role

Catalyzes DEOXYRIBOSE-P-ALD-RXN (reaction.ecocyc.DEOXYRIBOSE-P-ALD-RXN).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes a reversible aldol reaction between acetaldehyde and D-glyceraldehyde 3-phosphate to generate 2-deoxy-D-ribose 5-phosphate (PubMed:11598300, PubMed:17905878, PubMed:6749498). Can also catalyze the double aldol condensation of three acetaldehyde molecules, leading to the formation of 2,4,6-trideoxyhexose (Ref.5). {ECO:0000269|PubMed:11598300, ECO:0000269|PubMed:17905878, ECO:0000269|PubMed:6749498, ECO:0000269|Ref.5}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DEOXYRIBOSE-P-ALD-RXN|reaction.ecocyc.DEOXYRIBOSE-P-ALD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4381|gene.b4381]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6L0`
- `KEGG:ecj:JW4344;eco:b4381;ecoc:C3026_23675;`
- `GeneID:86862495;948902;`
- `GO:GO:0004139; GO:0005829; GO:0006018; GO:0006974; GO:0009264; GO:0015949; GO:0016020; GO:0016052; GO:0016829`
- `EC:4.1.2.4`

## Notes

Deoxyribose-phosphate aldolase (DERA) (EC 4.1.2.4) (2-deoxy-D-ribose 5-phosphate aldolase) (Phosphodeoxyriboaldolase) (Deoxyriboaldolase)
