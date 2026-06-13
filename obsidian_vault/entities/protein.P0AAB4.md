---
entity_id: "protein.P0AAB4"
entity_type: "protein"
name: "ubiD"
source_database: "UniProt"
source_id: "P0AAB4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000255|HAMAP-Rule:MF_01636, ECO:0000305|PubMed:782527}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01636, ECO:0000305|PubMed:782527}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiD yigC yigY b3843 JW3819"
---

# ubiD

`protein.P0AAB4`

## Static

- Type: `protein`
- Source: `UniProt:P0AAB4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000255|HAMAP-Rule:MF_01636, ECO:0000305|PubMed:782527}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01636, ECO:0000305|PubMed:782527}.

## Enriched Summary

FUNCTION: Catalyzes the decarboxylation of 3-octaprenyl-4-hydroxy benzoate to 2-octaprenylphenol, an intermediate step in ubiquinone biosynthesis. {ECO:0000255|HAMAP-Rule:MF_01636, ECO:0000269|PubMed:782527}.

## Biological Role

Component of 3-octaprenyl-4-hydroxybenzoate decarboxylase (complex.ecocyc.CPLX0-301).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the decarboxylation of 3-octaprenyl-4-hydroxy benzoate to 2-octaprenylphenol, an intermediate step in ubiquinone biosynthesis. {ECO:0000255|HAMAP-Rule:MF_01636, ECO:0000269|PubMed:782527}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-301|complex.ecocyc.CPLX0-301]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3843|gene.b3843]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAB4`
- `KEGG:ecj:JW3819;eco:b3843;ecoc:C3026_20780;`
- `GeneID:93778094;948326;`
- `GO:GO:0005737; GO:0005829; GO:0005886; GO:0006744; GO:0008694; GO:0030145; GO:0034214; GO:0042802; GO:0120233`
- `EC:4.1.1.98`

## Notes

3-octaprenyl-4-hydroxybenzoate carboxy-lyase (EC 4.1.1.98) (Polyprenyl p-hydroxybenzoate decarboxylase)
