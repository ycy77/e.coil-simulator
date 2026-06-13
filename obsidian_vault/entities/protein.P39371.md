---
entity_id: "protein.P39371"
entity_type: "protein"
name: "nanM"
source_database: "UniProt"
source_id: "P39371"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:18063573}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanM yjhT b4310 JW5777"
---

# nanM

`protein.P39371`

## Static

- Type: `protein`
- Source: `UniProt:P39371`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:18063573}.

## Enriched Summary

FUNCTION: Converts alpha-N-acetylneuranimic acid (Neu5Ac) to the beta-anomer, accelerating the equilibrium between the alpha- and beta-anomers. Probably facilitates sialidase-negative bacteria to compete successfully for limited amounts of extracellular Neu5Ac, which is likely taken up in the beta-anomer. In addition, the rapid removal of sialic acid from solution might be advantageous to the bacterium to damp down host responses (PubMed:18063573). Forms linear aceneuramate during interconversion of Neu5Ac anomers (PubMed:33895133). {ECO:0000269|PubMed:18063573, ECO:0000269|PubMed:33895133}. The periplasmic N-acetylneuraminate mutarotase supports the efficient use of α-N-acetylneuraminate (α-NeuNAc) as the sole source of carbon. Sialoglycoconjugates present in vertebrates are linked exclusively by α-linkages; once released by sialidases, spontaneous mutarotation converts the α anomer to β-NeuNAc, which constitutes more than 90% of NeuNAc at equilibrium. However, the spontaneous rate of mutarotation is relatively slow. Thus, loss of N-acetylneuraminate mutarotase confers a small growth delay to cells grown on α-NeuNAc . A crystal structure of NanM has been solved at 1.5 Å resolution, showing a homodimeric six-bladed β-propeller...

## Biological Role

Catalyzes N-acetyl-alpha-neuraminate 2-epimerase (reaction.R09797). Component of N-acetylneuraminate mutarotase (complex.ecocyc.CPLX0-7658).

## Annotation

FUNCTION: Converts alpha-N-acetylneuranimic acid (Neu5Ac) to the beta-anomer, accelerating the equilibrium between the alpha- and beta-anomers. Probably facilitates sialidase-negative bacteria to compete successfully for limited amounts of extracellular Neu5Ac, which is likely taken up in the beta-anomer. In addition, the rapid removal of sialic acid from solution might be advantageous to the bacterium to damp down host responses (PubMed:18063573). Forms linear aceneuramate during interconversion of Neu5Ac anomers (PubMed:33895133). {ECO:0000269|PubMed:18063573, ECO:0000269|PubMed:33895133}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R09797|reaction.R09797]] `KEGG` `database` - via EC:5.1.3.24
- `is_component_of` --> [[complex.ecocyc.CPLX0-7658|complex.ecocyc.CPLX0-7658]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4310|gene.b4310]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39371`
- `KEGG:ecj:JW5777;eco:b4310;ecoc:C3026_23270;`
- `GeneID:949106;`
- `GO:GO:0016857; GO:0019262; GO:0030288; GO:0042803`
- `EC:5.1.3.24`

## Notes

N-acetylneuraminate epimerase (EC 5.1.3.24) (N-acetylneuraminate anomerase NanM) (N-acetylneuraminate mutarotase) (Neu5Ac mutarotase) (Sialic acid epimerase)
