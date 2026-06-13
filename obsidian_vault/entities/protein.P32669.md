---
entity_id: "protein.P32669"
entity_type: "protein"
name: "fsaB"
source_database: "UniProt"
source_id: "P32669"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fsaB talC yijG b3946 JW3918"
---

# fsaB

`protein.P32669`

## Static

- Type: `protein`
- Source: `UniProt:P32669`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Catalyzes the reversible formation of fructose 6-phosphate from dihydroxyacetone and D-glyceraldehyde 3-phosphate via an aldolization reaction. Can utilize hydroxyacetone as an alternative donor substrate. Is also able to catalyze the direct self-aldol addition of glycolaldehyde. Is less catalytically efficient than the isozyme FsaA. Does not display transaldolase activity. {ECO:0000269|PubMed:11120740, ECO:0000269|Ref.6}.

## Biological Role

Component of fructose-6-phosphate aldolase 2 (complex.ecocyc.CPLX0-8584).

## Annotation

FUNCTION: Catalyzes the reversible formation of fructose 6-phosphate from dihydroxyacetone and D-glyceraldehyde 3-phosphate via an aldolization reaction. Can utilize hydroxyacetone as an alternative donor substrate. Is also able to catalyze the direct self-aldol addition of glycolaldehyde. Is less catalytically efficient than the isozyme FsaA. Does not display transaldolase activity. {ECO:0000269|PubMed:11120740, ECO:0000269|Ref.6}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8584|complex.ecocyc.CPLX0-8584]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b3946|gene.b3946]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32669`
- `KEGG:ecj:JW3918;eco:b3946;ecoc:C3026_21330;`
- `GeneID:948439;`
- `GO:GO:0005737; GO:0006000; GO:0042182; GO:0097023`
- `EC:4.1.2.-`

## Notes

Fructose-6-phosphate aldolase 2 (EC 4.1.2.-) (Fructose-6-phosphate aldolase B) (FSAB)
