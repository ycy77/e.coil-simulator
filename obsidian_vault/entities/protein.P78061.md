---
entity_id: "protein.P78061"
entity_type: "protein"
name: "puuA"
source_database: "UniProt"
source_id: "P78061"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "puuA ycjK b1297 JW5201"
---

# puuA

`protein.P78061`

## Static

- Type: `protein`
- Source: `UniProt:P78061`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the breakdown of putrescine. Catalyzes the ATP-dependent gamma-glutamylation of putrescine, producing gamma-L-glutamylputrescine. Absolutely essential to utilize putrescine as both nitrogen and carbon sources and to decrease the toxicity of putrescine, which can lead to inhibition of cell growth and protein synthesis. In vitro is also able to use several diamines, and spermidine and spermine, instead of putrescine, but with a much lower activity, and cannot catalyze the gamma-glutamylation of ornithine or GABA (PubMed:18495664). {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:18495664}. Glutamate-putrescine ligase is the first enzyme in the primary putrescine utilization pathway of E. coli . It catalyzes the ATP-dependent γ-glutamylation of putrescine. The function of genes in the puu gene cluster was initially inferred by similarity with the ipuABCDEGFH operon in Pseudomonas sp. . PuuA has similarity to glutamine synthetase; based on this similarity, predicted active site residues were mutagenized, and the resulting enzymes show little activity . A puuA deletion mutant can not grow on putrescine as the sole source of carbon or nitrogen . Expression of puuA is induced during the transition of anaerobic to aerobic cultures and by putrescine . PuuA: "putrescine utilization pathway"

## Biological Role

Component of glutamate-putrescine ligase (complex.ecocyc.CPLX0-7709).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in the breakdown of putrescine. Catalyzes the ATP-dependent gamma-glutamylation of putrescine, producing gamma-L-glutamylputrescine. Absolutely essential to utilize putrescine as both nitrogen and carbon sources and to decrease the toxicity of putrescine, which can lead to inhibition of cell growth and protein synthesis. In vitro is also able to use several diamines, and spermidine and spermine, instead of putrescine, but with a much lower activity, and cannot catalyze the gamma-glutamylation of ornithine or GABA (PubMed:18495664). {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:18495664}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7709|complex.ecocyc.CPLX0-7709]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b1297|gene.b1297]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P78061`
- `KEGG:ecj:JW5201;eco:b1297;`
- `GeneID:946202;`
- `GO:GO:0004356; GO:0005524; GO:0006542; GO:0006598; GO:0009447; GO:0034024`
- `EC:6.3.1.11`

## Notes

Gamma-glutamylputrescine synthetase PuuA (Gamma-Glu-Put synthetase) (EC 6.3.1.11) (Glutamate--putrescine ligase)
