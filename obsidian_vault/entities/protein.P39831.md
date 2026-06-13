---
entity_id: "protein.P39831"
entity_type: "protein"
name: "ydfG"
source_database: "UniProt"
source_id: "P39831"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydfG b1539 JW1532"
---

# ydfG

`protein.P39831`

## Static

- Type: `protein`
- Source: `UniProt:P39831`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: NADP-dependent dehydrogenase with broad substrate specificity acting on 3-hydroxy acids. Catalyzes the NADP-dependent oxidation of L-allo-threonine to L-2-amino-3-keto-butyrate, which is spontaneously decarboxylated into aminoacetone. Also acts on D-threonine, L-serine, D-serine, D-3-hydroxyisobutyrate, L-3-hydroxyisobutyrate, D-glycerate and L-glycerate (PubMed:12535615). Able to catalyze the reduction of the malonic semialdehyde to 3-hydroxypropionic acid. YdfG is apparently supplementing RutE, the presumed malonic semialdehyde reductase involved in pyrimidine degradation since both are able to detoxify malonic semialdehyde (PubMed:20400551). {ECO:0000269|PubMed:12535615, ECO:0000269|PubMed:20400551}. The ydfG gene belongs to the short-chain dehydrogenase/reductase (SDR) family and encodes a homotetrameric NADP+-dependent 3-hydroxy acid dehydrogenase, also called a serine dehydrogenase (SerDH). The high Km for NADP+ indicates that the enzyme acts in the reductive direction in vivo . A ydfG deletion mutant only grows poorly with uridine as the sole source of nitrogen, likely due to toxicity of the pathway intermediate, malonic semialdehyde . The crystal structure of the ligand-free homotetrameric SerDH complex and the NADP+-phosphate bound SerDH complex were solved to resolutions of 1.9 and 2.7 Å, respectively...

## Biological Role

Catalyzes R03758 (reaction.R03758), L-allo-threonine:NADP+ 3-oxidoreductase (decarboxylating) (reaction.R10852). Component of 3-hydroxy acid dehydrogenase YdfG (complex.ecocyc.CPLX0-1962).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: NADP-dependent dehydrogenase with broad substrate specificity acting on 3-hydroxy acids. Catalyzes the NADP-dependent oxidation of L-allo-threonine to L-2-amino-3-keto-butyrate, which is spontaneously decarboxylated into aminoacetone. Also acts on D-threonine, L-serine, D-serine, D-3-hydroxyisobutyrate, L-3-hydroxyisobutyrate, D-glycerate and L-glycerate (PubMed:12535615). Able to catalyze the reduction of the malonic semialdehyde to 3-hydroxypropionic acid. YdfG is apparently supplementing RutE, the presumed malonic semialdehyde reductase involved in pyrimidine degradation since both are able to detoxify malonic semialdehyde (PubMed:20400551). {ECO:0000269|PubMed:12535615, ECO:0000269|PubMed:20400551}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R03758|reaction.R03758]] `KEGG` `database` - via EC:1.1.1.381
- `catalyzes` --> [[reaction.R10852|reaction.R10852]] `KEGG` `database` - via EC:1.1.1.381
- `is_component_of` --> [[complex.ecocyc.CPLX0-1962|complex.ecocyc.CPLX0-1962]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1539|gene.b1539]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39831`
- `KEGG:ecj:JW1532;eco:b1539;ecoc:C3026_08890;`
- `GeneID:93775703;946085;`
- `GO:GO:0005829; GO:0006212; GO:0008442; GO:0031132; GO:0032991; GO:0035527; GO:0042802; GO:0051289`
- `EC:1.1.1.298; 1.1.1.381`

## Notes

NADP-dependent 3-hydroxy acid dehydrogenase YdfG (L-allo-threonine dehydrogenase) (EC 1.1.1.381) (Malonic semialdehyde reductase) (EC 1.1.1.298)
