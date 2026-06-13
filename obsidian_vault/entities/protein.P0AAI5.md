---
entity_id: "protein.P0AAI5"
entity_type: "protein"
name: "fabF"
source_database: "UniProt"
source_id: "P0AAI5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fabF fabJ b1095 JW1081"
---

# fabF

`protein.P0AAI5`

## Static

- Type: `protein`
- Source: `UniProt:P0AAI5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the type II fatty acid elongation cycle (PubMed:6988423, PubMed:9013860). Catalyzes the elongation of a wide range of acyl-ACP by the addition of two carbons from malonyl-ACP to an acyl acceptor (PubMed:22017312, PubMed:9013860). Can efficiently catalyze the conversion of palmitoleoyl-ACP (cis-hexadec-9-enoyl-ACP) to cis-vaccenoyl-ACP (cis-octadec-11-enoyl-ACP), an essential step in the thermal regulation of fatty acid composition (PubMed:6988423, PubMed:9013860). Can use acyl chains from C-6 to C-16 (PubMed:22017312, PubMed:9013860). Is able to catalyze the condensation reaction when CoA is the carrier for both substrates (PubMed:22017312). {ECO:0000269|PubMed:22017312, ECO:0000269|PubMed:6988423, ECO:0000269|PubMed:9013860}.

## Biological Role

Catalyzes dodecanoyl-[acyl-carrier-protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating) (reaction.R04726), hexanoyl-[acyl-carrier protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating) (reaction.R04957), octanoyl-[acyl-carrier protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating) (reaction.R04960), decanoyl-[acyl-carrier protein]:malonyl-[acyl-carrier-protein] C-acyltransferase (decarboxylating) (reaction.R04963). Component of 3-oxoacyl-[acyl carrier protein] synthase 2 (complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Involved in the type II fatty acid elongation cycle (PubMed:6988423, PubMed:9013860). Catalyzes the elongation of a wide range of acyl-ACP by the addition of two carbons from malonyl-ACP to an acyl acceptor (PubMed:22017312, PubMed:9013860). Can efficiently catalyze the conversion of palmitoleoyl-ACP (cis-hexadec-9-enoyl-ACP) to cis-vaccenoyl-ACP (cis-octadec-11-enoyl-ACP), an essential step in the thermal regulation of fatty acid composition (PubMed:6988423, PubMed:9013860). Can use acyl chains from C-6 to C-16 (PubMed:22017312, PubMed:9013860). Is able to catalyze the condensation reaction when CoA is the carrier for both substrates (PubMed:22017312). {ECO:0000269|PubMed:22017312, ECO:0000269|PubMed:6988423, ECO:0000269|PubMed:9013860}.

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R04726|reaction.R04726]] `KEGG` `database` - via EC:2.3.1.179
- `catalyzes` --> [[reaction.R04957|reaction.R04957]] `KEGG` `database` - via EC:2.3.1.179
- `catalyzes` --> [[reaction.R04960|reaction.R04960]] `KEGG` `database` - via EC:2.3.1.179
- `catalyzes` --> [[reaction.R04963|reaction.R04963]] `KEGG` `database` - via EC:2.3.1.179
- `is_component_of` --> [[complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX|complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1095|gene.b1095]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAI5`
- `KEGG:ecj:JW1081;eco:b1095;ecoc:C3026_06620;`
- `GeneID:86945966;946665;`
- `GO:GO:0004315; GO:0005829; GO:0006633; GO:0009409; GO:0019367; GO:0042803; GO:1903966`
- `EC:2.3.1.179`

## Notes

3-oxoacyl-[acyl-carrier-protein] synthase 2 (EC 2.3.1.179) (3-oxoacyl-[acyl-carrier-protein] synthase II) (Beta-ketoacyl-ACP synthase II) (KAS II)
