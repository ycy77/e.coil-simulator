---
entity_id: "protein.P00904"
entity_type: "protein"
name: "trpGD"
source_database: "UniProt"
source_id: "P00904"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trpGD trpD b1263 JW1255"
---

# trpGD

`protein.P00904`

## Static

- Type: `protein`
- Source: `UniProt:P00904`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of a heterotetrameric complex that catalyzes the two-step biosynthesis of anthranilate, an intermediate in the biosynthesis of L-tryptophan. In the first step, the glutamine-binding beta subunit (TrpG) of anthranilate synthase (AS) provides the glutamine amidotransferase activity which generates ammonia as a substrate that, along with chorismate, is used in the second step, catalyzed by the large alpha subunit of AS (TrpE) to produce anthranilate. In the absence of TrpG, TrpE can synthesize anthranilate directly from chorismate and high concentrations of ammonia. In addition to synthesizing anthranilate, it also catalyzes the second step of the pathway, the transfer of the phosphoribosyl group of 5-phosphorylribose-1-pyrophosphate (PRPP) to anthranilate. {ECO:0000269|PubMed:2428387, ECO:0000269|PubMed:4567790, ECO:0000269|PubMed:5333199}. Anthranilate phosphoribosyl transferase (TrpD) catalyzes the second step in the pathway of tryptophan biosynthesis. TrpD catalyzes a phosphoribosyltransferase reaction that generates N-(5'-phosphoribosyl)-anthranilate . The phosphoribosyl transferase and anthranilate synthase contributing portions of TrpD are present in different portions of the protein. The anthranilate synthase reaction requires the amino-terminal portion of the protein, whereas the phosphoribosyltransferase reaction requires the carboxy-terminal region .

## Biological Role

Catalyzes chorismate pyruvate-lyase (amino-accepting; anthranilate-forming) (reaction.R00985), chorismate pyruvate-lyase (amino-accepting) (reaction.R00986), PRTRANS-RXN (reaction.ecocyc.PRTRANS-RXN). Component of anthranilate synthase (complex.ecocyc.ANTHRANSYN-CPLX).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Part of a heterotetrameric complex that catalyzes the two-step biosynthesis of anthranilate, an intermediate in the biosynthesis of L-tryptophan. In the first step, the glutamine-binding beta subunit (TrpG) of anthranilate synthase (AS) provides the glutamine amidotransferase activity which generates ammonia as a substrate that, along with chorismate, is used in the second step, catalyzed by the large alpha subunit of AS (TrpE) to produce anthranilate. In the absence of TrpG, TrpE can synthesize anthranilate directly from chorismate and high concentrations of ammonia. In addition to synthesizing anthranilate, it also catalyzes the second step of the pathway, the transfer of the phosphoribosyl group of 5-phosphorylribose-1-pyrophosphate (PRPP) to anthranilate. {ECO:0000269|PubMed:2428387, ECO:0000269|PubMed:4567790, ECO:0000269|PubMed:5333199}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00985|reaction.R00985]] `KEGG` `database` - via EC:4.1.3.27
- `catalyzes` --> [[reaction.R00986|reaction.R00986]] `KEGG` `database` - via EC:4.1.3.27
- `catalyzes` --> [[reaction.ecocyc.PRTRANS-RXN|reaction.ecocyc.PRTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.ANTHRANSYN-CPLX|complex.ecocyc.ANTHRANSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1263|gene.b1263]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00904`
- `KEGG:ecj:JW1255;eco:b1263;ecoc:C3026_07410;`
- `GeneID:75203375;945109;`
- `GO:GO:0000162; GO:0000287; GO:0002047; GO:0004048; GO:0004049; GO:0005950`
- `EC:2.4.2.18; 4.1.3.27`

## Notes

Bifunctional protein TrpGD [Includes: Anthranilate synthase component 2 (AS) (ASII) (EC 4.1.3.27) (Anthranilate synthase, glutamine amidotransferase component); Anthranilate phosphoribosyltransferase (EC 2.4.2.18)]
