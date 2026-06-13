---
entity_id: "protein.P37349"
entity_type: "protein"
name: "dhaM"
source_database: "UniProt"
source_id: "P37349"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dhaM ycgC b1198 JW5185"
---

# dhaM

`protein.P37349`

## Static

- Type: `protein`
- Source: `UniProt:P37349`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the dihydroxyacetone kinase complex, which is responsible for the phosphoenolpyruvate (PEP)-dependent phosphorylation of dihydroxyacetone. DhaM serves as the phosphoryl donor. Is phosphorylated by phosphoenolpyruvate in an EI- and HPr-dependent reaction, and a phosphorelay system on histidine residues finally leads to phosphoryl transfer to DhaL and dihydroxyacetone. {ECO:0000269|PubMed:11350937}.

## Biological Role

Catalyzes phosphoenolpyruvate:glycerone phosphotransferase (reaction.R01012). Component of dihydroxyacetone kinase (complex.ecocyc.CPLX0-2081), dihydroxyacetone kinase, phosphotransferase component (complex.ecocyc.CPLX0-8206).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Component of the dihydroxyacetone kinase complex, which is responsible for the phosphoenolpyruvate (PEP)-dependent phosphorylation of dihydroxyacetone. DhaM serves as the phosphoryl donor. Is phosphorylated by phosphoenolpyruvate in an EI- and HPr-dependent reaction, and a phosphorelay system on histidine residues finally leads to phosphoryl transfer to DhaL and dihydroxyacetone. {ECO:0000269|PubMed:11350937}.

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R01012|reaction.R01012]] `KEGG` `database` - via EC:2.7.1.121
- `is_component_of` --> [[complex.ecocyc.CPLX0-2081|complex.ecocyc.CPLX0-2081]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8206|complex.ecocyc.CPLX0-8206]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1198|gene.b1198]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37349`
- `KEGG:ecj:JW5185;eco:b1198;ecoc:C3026_07045;`
- `GeneID:945749;`
- `GO:GO:0005829; GO:0006974; GO:0009401; GO:0016020; GO:0019563; GO:0042803; GO:0046835; GO:0047324; GO:1990234`
- `EC:2.7.1.121`

## Notes

PEP-dependent dihydroxyacetone kinase, phosphoryl donor subunit DhaM (EC 2.7.1.121) (Dihydroxyacetone kinase subunit M)
