---
entity_id: "protein.P0A763"
entity_type: "protein"
name: "ndk"
source_database: "UniProt"
source_id: "P0A763"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00451, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ndk b2518 JW2502"
---

# ndk

`protein.P0A763`

## Static

- Type: `protein`
- Source: `UniProt:P0A763`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00451, ECO:0000305}.

## Enriched Summary

FUNCTION: Major role in the synthesis of nucleoside triphosphates other than ATP. The ATP gamma phosphate is transferred to the NDP beta phosphate via a ping-pong mechanism, using a phosphorylated active-site intermediate. {ECO:0000255|HAMAP-Rule:MF_00451, ECO:0000269|PubMed:7730286}.

## Biological Role

Catalyzes ATP:ADP phosphatransferase (reaction.R00124), ATP:2'-deoxy-5-hydroxymethylcytidine-5'-diphosphate phosphotransferase (reaction.R00139), ATP:UDP phosphotransferase (reaction.R00156), ATP:GDP phosphotransferase (reaction.R00330), ATP:nucleoside-diphosphate phosphotransferase (reaction.R00331), ATP:CDP phosphotransferase (reaction.R00570), ATP:IDP phosphotransferase (reaction.R00722), ATP:dADP phosphotransferase (reaction.R01137), and 1 more. Component of nucleoside diphosphate kinase (complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Major role in the synthesis of nucleoside triphosphates other than ATP. The ATP gamma phosphate is transferred to the NDP beta phosphate via a ping-pong mechanism, using a phosphorylated active-site intermediate. {ECO:0000255|HAMAP-Rule:MF_00451, ECO:0000269|PubMed:7730286}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (10)

- `catalyzes` --> [[reaction.R00124|reaction.R00124]] `KEGG` `database` - via EC:2.7.4.6
- `catalyzes` --> [[reaction.R00139|reaction.R00139]] `KEGG` `database` - via EC:2.7.4.6
- `catalyzes` --> [[reaction.R00156|reaction.R00156]] `KEGG` `database` - via EC:2.7.4.6
- `catalyzes` --> [[reaction.R00330|reaction.R00330]] `KEGG` `database` - via EC:2.7.4.6
- `catalyzes` --> [[reaction.R00331|reaction.R00331]] `KEGG` `database` - via EC:2.7.4.6
- `catalyzes` --> [[reaction.R00570|reaction.R00570]] `KEGG` `database` - via EC:2.7.4.6
- `catalyzes` --> [[reaction.R00722|reaction.R00722]] `KEGG` `database` - via EC:2.7.4.6
- `catalyzes` --> [[reaction.R01137|reaction.R01137]] `KEGG` `database` - via EC:2.7.4.6
- `catalyzes` --> [[reaction.R02331|reaction.R02331]] `KEGG` `database` - via EC:2.7.4.6
- `is_component_of` --> [[complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX|complex.ecocyc.NUCLEOSIDE-DIP-KIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2518|gene.b2518]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A763`
- `KEGG:ecj:JW2502;eco:b2518;ecoc:C3026_13960;`
- `GeneID:86860643;93774618;945611;`
- `GO:GO:0004550; GO:0005524; GO:0005829; GO:0006163; GO:0006183; GO:0006220; GO:0006228; GO:0006241; GO:0046872`
- `EC:2.7.4.6`

## Notes

Nucleoside diphosphate kinase (NDK) (NDP kinase) (EC 2.7.4.6) (Nucleoside-2-P kinase)
