---
entity_id: "protein.P69451"
entity_type: "protein"
name: "fadD"
source_database: "UniProt"
source_id: "P69451"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}. Note=Partially membrane-associated. {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadD oldD b1805 JW1794"
---

# fadD

`protein.P69451`

## Static

- Type: `protein`
- Source: `UniProt:P69451`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}. Note=Partially membrane-associated. {ECO:0000250}.

## Enriched Summary

FUNCTION: Catalyzes the esterification, concomitant with transport, of exogenous long-chain fatty acids into metabolically active CoA thioesters for subsequent degradation or incorporation into phospholipids. Activity is the highest with fatty acid substrates of > 10 carbon atoms (PubMed:15213221). Is involved in the aerobic beta-oxidative degradation of fatty acids, which allows aerobic growth of E.coli on fatty acids as a sole carbon and energy source (PubMed:12535077). {ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:15213221}.

## Biological Role

Catalyzes long-chain-fatty-acid:CoA ligase (AMP-forming) (reaction.R00390). Component of long-chain-fatty-acid—CoA ligase (complex.ecocyc.ACYLCOASYN-CPLX).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco04146` Peroxisome (KEGG)

## Annotation

FUNCTION: Catalyzes the esterification, concomitant with transport, of exogenous long-chain fatty acids into metabolically active CoA thioesters for subsequent degradation or incorporation into phospholipids. Activity is the highest with fatty acid substrates of > 10 carbon atoms (PubMed:15213221). Is involved in the aerobic beta-oxidative degradation of fatty acids, which allows aerobic growth of E.coli on fatty acids as a sole carbon and energy source (PubMed:12535077). {ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:15213221}.

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco04146` Peroxisome (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00390|reaction.R00390]] `KEGG` `database` - via EC:6.2.1.3
- `is_component_of` --> [[complex.ecocyc.ACYLCOASYN-CPLX|complex.ecocyc.ACYLCOASYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1805|gene.b1805]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69451`
- `KEGG:ecj:JW1794;eco:b1805;`
- `GeneID:75171874;75202631;946327;`
- `GO:GO:0004467; GO:0005504; GO:0005524; GO:0005737; GO:0005829; GO:0006629; GO:0006631; GO:0006635; GO:0006637; GO:0008654; GO:0009411; GO:0009898; GO:0015908; GO:0016405; GO:0042803; GO:0070538; GO:0102391`
- `EC:6.2.1.3`

## Notes

Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) (Acyl-CoA synthetase)
