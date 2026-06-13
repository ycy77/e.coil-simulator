---
entity_id: "protein.P0A953"
entity_type: "protein"
name: "fabB"
source_database: "UniProt"
source_id: "P0A953"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fabB fabC b2323 JW2320"
---

# fabB

`protein.P0A953`

## Static

- Type: `protein`
- Source: `UniProt:P0A953`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Involved in the type II fatty acid elongation cycle. Catalyzes the elongation of a wide range of acyl-ACP by the addition of two carbons from malonyl-ACP to an acyl acceptor (PubMed:19679654, PubMed:22017312, PubMed:8910376, PubMed:9013860). Can also use unsaturated fatty acids (PubMed:19679654, PubMed:3076377, PubMed:8910376). Catalyzes a key reaction in unsaturated fatty acid (UFA) synthesis, the elongation of the cis-3-decenoyl-ACP produced by FabA (PubMed:19679654). Can use acyl chains from C-6 to C-14 (PubMed:19679654, PubMed:22017312, PubMed:8910376, PubMed:9013860). Has an absolute requirement for an ACP substrate as the acyl donor, and no activity is detected when both substrates are based on CoA (PubMed:22017312). {ECO:0000269|PubMed:19679654, ECO:0000269|PubMed:22017312, ECO:0000269|PubMed:3076377, ECO:0000269|PubMed:8910376, ECO:0000269|PubMed:9013860}.

## Biological Role

Catalyzes dodecanoyl-[acyl-carrier-protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating) (reaction.R04726), hexanoyl-[acyl-carrier protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating) (reaction.R04957), octanoyl-[acyl-carrier protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating) (reaction.R04960), decanoyl-[acyl-carrier protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating) (reaction.R04963). Component of 3-oxoacyl-[acyl carrier protein] synthase 1 (complex.ecocyc.FABB-CPLX).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Involved in the type II fatty acid elongation cycle. Catalyzes the elongation of a wide range of acyl-ACP by the addition of two carbons from malonyl-ACP to an acyl acceptor (PubMed:19679654, PubMed:22017312, PubMed:8910376, PubMed:9013860). Can also use unsaturated fatty acids (PubMed:19679654, PubMed:3076377, PubMed:8910376). Catalyzes a key reaction in unsaturated fatty acid (UFA) synthesis, the elongation of the cis-3-decenoyl-ACP produced by FabA (PubMed:19679654). Can use acyl chains from C-6 to C-14 (PubMed:19679654, PubMed:22017312, PubMed:8910376, PubMed:9013860). Has an absolute requirement for an ACP substrate as the acyl donor, and no activity is detected when both substrates are based on CoA (PubMed:22017312). {ECO:0000269|PubMed:19679654, ECO:0000269|PubMed:22017312, ECO:0000269|PubMed:3076377, ECO:0000269|PubMed:8910376, ECO:0000269|PubMed:9013860}.

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R04726|reaction.R04726]] `KEGG` `database` - via EC:2.3.1.41
- `catalyzes` --> [[reaction.R04957|reaction.R04957]] `KEGG` `database` - via EC:2.3.1.41
- `catalyzes` --> [[reaction.R04960|reaction.R04960]] `KEGG` `database` - via EC:2.3.1.41
- `catalyzes` --> [[reaction.R04963|reaction.R04963]] `KEGG` `database` - via EC:2.3.1.41
- `is_component_of` --> [[complex.ecocyc.FABB-CPLX|complex.ecocyc.FABB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2323|gene.b2323]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A953`
- `KEGG:ecj:JW2320;eco:b2323;ecoc:C3026_12945;`
- `GeneID:75202594;946799;`
- `GO:GO:0004315; GO:0005829; GO:0006633; GO:1903966`
- `EC:2.3.1.41`

## Notes

3-oxoacyl-[acyl-carrier-protein] synthase 1 (EC 2.3.1.41) (3-oxoacyl-[acyl-carrier-protein] synthase I) (Beta-ketoacyl-ACP synthase I) (KAS I)
