---
entity_id: "protein.P17109"
entity_type: "protein"
name: "menD"
source_database: "UniProt"
source_id: "P17109"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "menD b2264 JW5374"
---

# menD

`protein.P17109`

## Static

- Type: `protein`
- Source: `UniProt:P17109`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the thiamine diphosphate-dependent decarboxylation of 2-oxoglutarate and the subsequent addition of the resulting succinic semialdehyde-thiamine pyrophosphate anion to isochorismate to yield 2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate (SEPHCHC). {ECO:0000255|HAMAP-Rule:MF_01659, ECO:0000269|PubMed:17760421}.

## Biological Role

Component of 2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate synthase (complex.ecocyc.CPLX0-7525).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the thiamine diphosphate-dependent decarboxylation of 2-oxoglutarate and the subsequent addition of the resulting succinic semialdehyde-thiamine pyrophosphate anion to isochorismate to yield 2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate (SEPHCHC). {ECO:0000255|HAMAP-Rule:MF_01659, ECO:0000269|PubMed:17760421}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7525|complex.ecocyc.CPLX0-7525]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2264|gene.b2264]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17109`
- `KEGG:ecj:JW5374;eco:b2264;ecoc:C3026_12645;`
- `GeneID:946720;`
- `GO:GO:0000287; GO:0009234; GO:0030145; GO:0030976; GO:0042803; GO:0070204`
- `EC:2.2.1.9`

## Notes

2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate synthase (SEPHCHC synthase) (EC 2.2.1.9) (Menaquinone biosynthesis protein MenD)
