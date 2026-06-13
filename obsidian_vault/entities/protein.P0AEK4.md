---
entity_id: "protein.P0AEK4"
entity_type: "protein"
name: "fabI"
source_database: "UniProt"
source_id: "P0AEK4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fabI envM b1288 JW1281"
---

# fabI

`protein.P0AEK4`

## Static

- Type: `protein`
- Source: `UniProt:P0AEK4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reduction of a carbon-carbon double bond in an enoyl moiety that is covalently linked to an acyl carrier protein (ACP). Involved in the elongation cycle of fatty acid which are used in the lipid metabolism and in the biotin biosynthesis. {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:20693992, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8119879, ECO:0000269|PubMed:8910376}.

## Biological Role

Catalyzes butyryl-[acp]:NAD+ trans-2-oxidoreductase (reaction.R04429), butyryl-[acp]:NADP+ trans-2-oxidoreductase (reaction.R04430), dodecanoyl-[acp]:NAD+ trans-2-oxidoreductase (reaction.R04724), dodecanoyl-[acp]:NADP+ trans-2-oxidoreductase (reaction.R04725), octanoyl-[acp]:NAD+ trans-2-oxidoreductase (reaction.R04958), octanoyl-[acp]:NADP+ trans-2-oxidoreductase (reaction.R04959), decanoyl-[acp]:NAD+ trans-2-oxidoreductase (reaction.R04961), decanoyl-[acp]:NADP+ trans-2-oxidoreductase (reaction.R04962), and 2 more. Component of enoyl-[acyl-carrier-protein] reductase (complex.ecocyc.CPLX0-8006).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of a carbon-carbon double bond in an enoyl moiety that is covalently linked to an acyl carrier protein (ACP). Involved in the elongation cycle of fatty acid which are used in the lipid metabolism and in the biotin biosynthesis. {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:20693992, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8119879, ECO:0000269|PubMed:8910376}.

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (11)

- `catalyzes` --> [[reaction.R04429|reaction.R04429]] `KEGG` `database` - via EC:1.3.1.9
- `catalyzes` --> [[reaction.R04430|reaction.R04430]] `KEGG` `database` - via EC:1.3.1.10
- `catalyzes` --> [[reaction.R04724|reaction.R04724]] `KEGG` `database` - via EC:1.3.1.9
- `catalyzes` --> [[reaction.R04725|reaction.R04725]] `KEGG` `database` - via EC:1.3.1.10
- `catalyzes` --> [[reaction.R04958|reaction.R04958]] `KEGG` `database` - via EC:1.3.1.9
- `catalyzes` --> [[reaction.R04959|reaction.R04959]] `KEGG` `database` - via EC:1.3.1.10
- `catalyzes` --> [[reaction.R04961|reaction.R04961]] `KEGG` `database` - via EC:1.3.1.9
- `catalyzes` --> [[reaction.R04962|reaction.R04962]] `KEGG` `database` - via EC:1.3.1.10
- `catalyzes` --> [[reaction.R04966|reaction.R04966]] `KEGG` `database` - via EC:1.3.1.9
- `catalyzes` --> [[reaction.R07765|reaction.R07765]] `KEGG` `database` - via EC:1.3.1.9
- `is_component_of` --> [[complex.ecocyc.CPLX0-8006|complex.ecocyc.CPLX0-8006]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1288|gene.b1288]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEK4`
- `KEGG:ecj:JW1281;eco:b1288;ecoc:C3026_07565;`
- `GeneID:86859893;93775413;945870;`
- `GO:GO:0004318; GO:0005829; GO:0008610; GO:0009102; GO:0016020; GO:0030497; GO:0032991; GO:0042802; GO:0046677; GO:0051289; GO:0070404; GO:1902494`
- `EC:1.3.1.9`

## Notes

Enoyl-[acyl-carrier-protein] reductase [NADH] FabI (ENR) (EC 1.3.1.9) (NADH-dependent enoyl-ACP reductase)
