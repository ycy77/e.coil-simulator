---
entity_id: "protein.P00895"
entity_type: "protein"
name: "trpE"
source_database: "UniProt"
source_id: "P00895"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trpE b1264 JW1256"
---

# trpE

`protein.P00895`

## Static

- Type: `protein`
- Source: `UniProt:P00895`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of a heterotetrameric complex that catalyzes the two-step biosynthesis of anthranilate, an intermediate in the biosynthesis of L-tryptophan. In the first step, the glutamine-binding beta subunit (TrpG) of anthranilate synthase (AS) provides the glutamine amidotransferase activity which generates ammonia as a substrate that, along with chorismate, is used in the second step, catalyzed by the large alpha subunit of AS (TrpE) to produce anthranilate. In the absence of TrpG, TrpE can synthesize anthranilate directly from chorismate and high concentrations of ammonia. {ECO:0000269|PubMed:4567790, ECO:0000269|PubMed:4886289, ECO:0000269|PubMed:5333199}.

## Biological Role

Catalyzes chorismate pyruvate-lyase (amino-accepting; anthranilate-forming) (reaction.R00985), chorismate pyruvate-lyase (amino-accepting) (reaction.R00986). Component of anthranilate synthase (complex.ecocyc.ANTHRANSYN-CPLX).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of a heterotetrameric complex that catalyzes the two-step biosynthesis of anthranilate, an intermediate in the biosynthesis of L-tryptophan. In the first step, the glutamine-binding beta subunit (TrpG) of anthranilate synthase (AS) provides the glutamine amidotransferase activity which generates ammonia as a substrate that, along with chorismate, is used in the second step, catalyzed by the large alpha subunit of AS (TrpE) to produce anthranilate. In the absence of TrpG, TrpE can synthesize anthranilate directly from chorismate and high concentrations of ammonia. {ECO:0000269|PubMed:4567790, ECO:0000269|PubMed:4886289, ECO:0000269|PubMed:5333199}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00985|reaction.R00985]] `KEGG` `database` - via EC:4.1.3.27
- `catalyzes` --> [[reaction.R00986|reaction.R00986]] `KEGG` `database` - via EC:4.1.3.27
- `is_component_of` --> [[complex.ecocyc.ANTHRANSYN-CPLX|complex.ecocyc.ANTHRANSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1264|gene.b1264]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00895`
- `KEGG:ecj:JW1256;eco:b1264;ecoc:C3026_07415;`
- `GeneID:945846;`
- `GO:GO:0000162; GO:0004049; GO:0005950; GO:0046872`
- `EC:4.1.3.27`

## Notes

Anthranilate synthase component 1 (AS) (ASI) (EC 4.1.3.27)
