---
entity_id: "protein.P0A7B1"
entity_type: "protein"
name: "ppk"
source_database: "UniProt"
source_id: "P0A7B1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:1331061}; Peripheral membrane protein {ECO:0000269|PubMed:1331061}. Note=Associated with the outer membrane in overproducing cells. {ECO:0000269|PubMed:1331061}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppk b2501 JW2486"
---

# ppk

`protein.P0A7B1`

## Static

- Type: `protein`
- Source: `UniProt:P0A7B1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:1331061}; Peripheral membrane protein {ECO:0000269|PubMed:1331061}. Note=Associated with the outer membrane in overproducing cells. {ECO:0000269|PubMed:1331061}.

## Enriched Summary

FUNCTION: Catalyzes the reversible transfer of the terminal phosphate of ATP to form a long-chain polyphosphate (polyP). Can form linear polymers of orthophosphate with chain lengths up to 1000 or more. Can use GTP instead of ATP, but the efficiency of GTP is 5% that of ATP. Also exhibits several other enzymatic activities, which include: ATP synthesis from polyP in the presence of excess ADP, general nucleoside-diphosphate kinase activity, linear guanosine 5'-tetraphosphate (ppppG) synthesis and autophosphorylation. {ECO:0000269|PubMed:10660553, ECO:0000269|PubMed:8962061}.

## Biological Role

Component of degradosome (complex.ecocyc.CPLX0-2381), polyphosphate kinase (complex.ecocyc.PPK-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible transfer of the terminal phosphate of ATP to form a long-chain polyphosphate (polyP). Can form linear polymers of orthophosphate with chain lengths up to 1000 or more. Can use GTP instead of ATP, but the efficiency of GTP is 5% that of ATP. Also exhibits several other enzymatic activities, which include: ATP synthesis from polyP in the presence of excess ADP, general nucleoside-diphosphate kinase activity, linear guanosine 5'-tetraphosphate (ppppG) synthesis and autophosphorylation. {ECO:0000269|PubMed:10660553, ECO:0000269|PubMed:8962061}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2381|complex.ecocyc.CPLX0-2381]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PPK-CPLX|complex.ecocyc.PPK-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2501|gene.b2501]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7B1`
- `KEGG:ecj:JW2486;eco:b2501;ecoc:C3026_13870;`
- `GeneID:93774635;946971;`
- `GO:GO:0005524; GO:0005829; GO:0005886; GO:0006799; GO:0008976; GO:0009358; GO:0016020; GO:0016776; GO:0016778; GO:0031241; GO:0042803; GO:0043751; GO:0046872; GO:0051302`
- `EC:2.7.4.1`

## Notes

Polyphosphate kinase (EC 2.7.4.1) (ATP-polyphosphate phosphotransferase) (Polyphosphoric acid kinase)
