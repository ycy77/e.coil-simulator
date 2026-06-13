---
entity_id: "protein.P24230"
entity_type: "protein"
name: "recG"
source_database: "UniProt"
source_id: "P24230"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "recG radC spoV b3652 JW3627"
---

# recG

`protein.P24230`

## Static

- Type: `protein`
- Source: `UniProt:P24230`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Genetic interactions indicate that RecG or RadD are required for DNA repair in every replication cycle; they function in different pathways, each is essential in the absence of the other (PubMed:32644157). Plays a critical role in recombination and DNA repair (PubMed:8428576, PubMed:7957087, PubMed:8127666, PubMed:9265736, PubMed:10871364, PubMed:32644157). RecG or RadD are required for DNA maintenance in every replication cycle (PubMed:32644157). Helps process Holliday junction (HJ) intermediates to mature products by catalyzing branch migration (PubMed:8428576, PubMed:7957087, PubMed:8127666, PubMed:10871364). Has replication fork regression activity, unwinds stalled or blocked replication forks to make a HJ that can be resolved by RuvC or RusA (PubMed:10778854, PubMed:11459957). Also rewinds unwound dsDNA in an ATP-dependent manner (PubMed:24013402). Has double-stranded (ds)DNA unwinding activity characteristic of a DNA helicase with 3'-5' polarity in vitro on linear dsDNA; branched duplex DNA (Y-DNA) substrates adopt different conformations that influence which of the two arms are unwound (PubMed:7957087). Binds and unwinds HJ and Y-DNA but not linear duplex DNA; binds no more than 10 nucleotides of ssDNA at a fork (PubMed:8428576, PubMed:7957087, PubMed:8127666, PubMed:10871364, PubMed:11459957, PubMed:15533834)...

## Biological Role

Catalyzes RXN-11135 (reaction.ecocyc.RXN-11135).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: Genetic interactions indicate that RecG or RadD are required for DNA repair in every replication cycle; they function in different pathways, each is essential in the absence of the other (PubMed:32644157). Plays a critical role in recombination and DNA repair (PubMed:8428576, PubMed:7957087, PubMed:8127666, PubMed:9265736, PubMed:10871364, PubMed:32644157). RecG or RadD are required for DNA maintenance in every replication cycle (PubMed:32644157). Helps process Holliday junction (HJ) intermediates to mature products by catalyzing branch migration (PubMed:8428576, PubMed:7957087, PubMed:8127666, PubMed:10871364). Has replication fork regression activity, unwinds stalled or blocked replication forks to make a HJ that can be resolved by RuvC or RusA (PubMed:10778854, PubMed:11459957). Also rewinds unwound dsDNA in an ATP-dependent manner (PubMed:24013402). Has double-stranded (ds)DNA unwinding activity characteristic of a DNA helicase with 3'-5' polarity in vitro on linear dsDNA; branched duplex DNA (Y-DNA) substrates adopt different conformations that influence which of the two arms are unwound (PubMed:7957087). Binds and unwinds HJ and Y-DNA but not linear duplex DNA; binds no more than 10 nucleotides of ssDNA at a fork (PubMed:8428576, PubMed:7957087, PubMed:8127666, PubMed:10871364, PubMed:11459957, PubMed:15533834). Has a role in constitutive stable DNA replication (cSDR, DNA replication in the absence of protein synthesis) and R-loop (RNA annealed with dsDNA) formation (PubMed:7774596). Unwinds R-loops but not RNA:DNA hybrids (PubMed:8980680, PubMed:15533834). Is genetically synergistic to RadA and RuvABC (PubMed:12446634, PubMed:25484163). {ECO:0000269|PubMed:10778854, ECO:0000269|PubMed:10871364, ECO:0000269|PubMed:11459957, ECO:0000269|PubMed:12446634, ECO:0000269|PubMed:15533834, ECO:0000269|PubMed:24013402, ECO:0000269|PubMed:25484163, ECO:0000269|PubMed:32644157, ECO:0000269|PubMed:7774596, ECO:0000269|PubMed:7957087, ECO:0000269|PubMed:8127666, ECO:0000269|PubMed:8428576, ECO:0000269|PubMed:9265736}.; FUNCTION: Uup probably acts upstream of RecG; they are important in repair of stalled replication forks and postreplication gaps (PubMed:32644157). Lethal double radD-recG deletions are suppressed by a reduction in recA expression, by point mutations in priA helicase, by deletions in recF, recO or uup, suggesting all these proteins create branched DNA intermediates requiring RadD or RecG for resolution (PubMed:32644157). {ECO:0000269|PubMed:32644157}.

## Pathways

- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11135|reaction.ecocyc.RXN-11135]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3652|gene.b3652]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24230`
- `KEGG:ecj:JW3627;eco:b3652;ecoc:C3026_19785;`
- `GeneID:948162;`
- `GO:GO:0003677; GO:0003678; GO:0005524; GO:0005829; GO:0006281; GO:0006310; GO:0009314; GO:0009379; GO:0016887; GO:0043138; GO:0071932`
- `EC:5.6.2.4`

## Notes

ATP-dependent DNA helicase RecG (EC 5.6.2.4) (DNA branch migration protein RecG) (Probable DNA 3'-5' helicase RecG)
