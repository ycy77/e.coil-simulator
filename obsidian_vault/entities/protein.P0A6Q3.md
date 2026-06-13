---
entity_id: "protein.P0A6Q3"
entity_type: "protein"
name: "fabA"
source_database: "UniProt"
source_id: "P0A6Q3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fabA b0954 JW0937"
---

# fabA

`protein.P0A6Q3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6Q3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Necessary for the introduction of cis unsaturation into fatty acids (PubMed:8910376). Catalyzes the dehydration of (3R)-3-hydroxydecanoyl-ACP to (2E)-decenoyl-ACP and then its isomerization to (3Z)-decenoyl-ACP (PubMed:8910376). Can catalyze the dehydratase reaction for beta-hydroxyacyl-ACPs with saturated chain lengths up to 16:0, being most active on intermediate chain length (PubMed:10629181, PubMed:7592873, PubMed:8910376). Is inactive in the dehydration of long chain unsaturated beta-hydroxyacyl-ACP (PubMed:8910376). {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8910376}.

## Biological Role

Catalyzes (3R)-3-hydroxybutanoyl-[acyl-carrier-protein] hydro-lyase (reaction.R04428), (3R)-3-hydroxydodecanoyl-[acyl-carrier-protein] hydro-lyase (reaction.R04965). Component of β-hydroxyacyl-acyl carrier protein dehydratase/isomerase (complex.ecocyc.FABA-CPLX).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

FUNCTION: Necessary for the introduction of cis unsaturation into fatty acids (PubMed:8910376). Catalyzes the dehydration of (3R)-3-hydroxydecanoyl-ACP to (2E)-decenoyl-ACP and then its isomerization to (3Z)-decenoyl-ACP (PubMed:8910376). Can catalyze the dehydratase reaction for beta-hydroxyacyl-ACPs with saturated chain lengths up to 16:0, being most active on intermediate chain length (PubMed:10629181, PubMed:7592873, PubMed:8910376). Is inactive in the dehydration of long chain unsaturated beta-hydroxyacyl-ACP (PubMed:8910376). {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8910376}.

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R04428|reaction.R04428]] `KEGG` `database` - via EC:4.2.1.59
- `catalyzes` --> [[reaction.R04965|reaction.R04965]] `KEGG` `database` - via EC:4.2.1.59
- `is_component_of` --> [[complex.ecocyc.FABA-CPLX|complex.ecocyc.FABA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0954|gene.b0954]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6Q3`
- `KEGG:ecj:JW0937;eco:b0954;ecoc:C3026_05835;`
- `GeneID:86863472;93776460;945568;`
- `GO:GO:0005829; GO:0006633; GO:0006636; GO:0019171; GO:0034017; GO:0042803`
- `EC:4.2.1.59; 5.3.3.14`

## Notes

3-hydroxydecanoyl-[acyl-carrier-protein] dehydratase (EC 4.2.1.59) (3-hydroxyacyl-[acyl-carrier-protein] dehydratase FabA) (Beta-hydroxydecanoyl thioester dehydrase) (Trans-2-decenoyl-[acyl-carrier-protein] isomerase) (EC 5.3.3.14)
