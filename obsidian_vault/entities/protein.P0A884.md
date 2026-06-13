---
entity_id: "protein.P0A884"
entity_type: "protein"
name: "thyA"
source_database: "UniProt"
source_id: "P0A884"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00008}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thyA b2827 JW2795"
---

# thyA

`protein.P0A884`

## Static

- Type: `protein`
- Source: `UniProt:P0A884`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00008}.

## Enriched Summary

FUNCTION: Catalyzes the reductive methylation of 2'-deoxyuridine-5'-monophosphate (dUMP) to 2'-deoxythymidine-5'-monophosphate (dTMP) while utilizing 5,10-methylenetetrahydrofolate (mTHF) as the methyl donor and reductant in the reaction, yielding dihydrofolate (DHF) as a by-product (PubMed:2223754, PubMed:3286637, PubMed:9826509). This enzymatic reaction provides an intracellular de novo source of dTMP, an essential precursor for DNA biosynthesis. This protein also binds to its mRNA thus repressing its own translation (PubMed:7708505). {ECO:0000269|PubMed:2223754, ECO:0000269|PubMed:3286637, ECO:0000269|PubMed:7708505, ECO:0000269|PubMed:9826509}.

## Biological Role

Component of thymidylate synthase (complex.ecocyc.THYMIDYLATESYN-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the reductive methylation of 2'-deoxyuridine-5'-monophosphate (dUMP) to 2'-deoxythymidine-5'-monophosphate (dTMP) while utilizing 5,10-methylenetetrahydrofolate (mTHF) as the methyl donor and reductant in the reaction, yielding dihydrofolate (DHF) as a by-product (PubMed:2223754, PubMed:3286637, PubMed:9826509). This enzymatic reaction provides an intracellular de novo source of dTMP, an essential precursor for DNA biosynthesis. This protein also binds to its mRNA thus repressing its own translation (PubMed:7708505). {ECO:0000269|PubMed:2223754, ECO:0000269|PubMed:3286637, ECO:0000269|PubMed:7708505, ECO:0000269|PubMed:9826509}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.THYMIDYLATESYN-CPLX|complex.ecocyc.THYMIDYLATESYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2827|gene.b2827]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A884`
- `KEGG:ecj:JW2795;eco:b2827;ecoc:C3026_15520;`
- `GeneID:86860908;93779171;949035;`
- `GO:GO:0000287; GO:0003723; GO:0004799; GO:0005829; GO:0006231; GO:0006235; GO:0006417; GO:0009314; GO:0032259; GO:0042803`
- `EC:2.1.1.45`

## Notes

Thymidylate synthase (TS) (TSase) (EC 2.1.1.45)
