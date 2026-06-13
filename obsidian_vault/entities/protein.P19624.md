---
entity_id: "protein.P19624"
entity_type: "protein"
name: "pdxA"
source_database: "UniProt"
source_id: "P19624"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00536}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdxA b0052 JW0051"
---

# pdxA

`protein.P19624`

## Static

- Type: `protein`
- Source: `UniProt:P19624`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00536}.

## Enriched Summary

FUNCTION: Catalyzes the NAD(P)-dependent oxidation of 4-(phosphooxy)-L-threonine (HTP) into 2-amino-3-oxo-4-(phosphooxy)butyric acid which spontaneously decarboxylates to form 3-amino-2-oxopropyl phosphate (AHAP). {ECO:0000255|HAMAP-Rule:MF_00536, ECO:0000269|PubMed:15026039, ECO:0000269|Ref.5}.

## Biological Role

Catalyzes 4-(phosphonooxy)threonine:NAD oxidoreductase (reaction.R05837). Component of 4-hydroxythreonine-4-phosphate dehydrogenase (complex.ecocyc.CPLX0-7847).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the NAD(P)-dependent oxidation of 4-(phosphooxy)-L-threonine (HTP) into 2-amino-3-oxo-4-(phosphooxy)butyric acid which spontaneously decarboxylates to form 3-amino-2-oxopropyl phosphate (AHAP). {ECO:0000255|HAMAP-Rule:MF_00536, ECO:0000269|PubMed:15026039, ECO:0000269|Ref.5}.

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05837|reaction.R05837]] `KEGG` `database` - via EC:1.1.1.262
- `is_component_of` --> [[complex.ecocyc.CPLX0-7847|complex.ecocyc.CPLX0-7847]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0052|gene.b0052]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P19624`
- `KEGG:ecj:JW0051;eco:b0052;ecoc:C3026_00270;`
- `GeneID:944919;`
- `GO:GO:0000287; GO:0005737; GO:0008270; GO:0008615; GO:0042802; GO:0042803; GO:0042823; GO:0050570; GO:0050897; GO:0051287`
- `EC:1.1.1.262`

## Notes

4-hydroxythreonine-4-phosphate dehydrogenase (EC 1.1.1.262) (4-(phosphohydroxy)-L-threonine dehydrogenase)
