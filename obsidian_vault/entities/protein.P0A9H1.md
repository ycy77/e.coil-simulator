---
entity_id: "protein.P0A9H1"
entity_type: "protein"
name: "mug"
source_database: "UniProt"
source_id: "P0A9H1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mug ygjF b3068 JW3040"
---

# mug

`protein.P0A9H1`

## Static

- Type: `protein`
- Source: `UniProt:P0A9H1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Excises ethenocytosine and uracil, which can arise by alkylation or deamination of cytosine, respectively, from the corresponding mispairs with guanine in ds-DNA. It is capable of hydrolyzing the carbon-nitrogen bond between the sugar-phosphate backbone of the DNA and the mispaired base. The complementary strand guanine functions in substrate recognition. Required for DNA damage lesion repair in stationary-phase cells. {ECO:0000269|PubMed:12668677, ECO:0000269|PubMed:8878487}. Mug is a glycosylase that acts in DNA repair . Mug shows activity toward G:U and G:T base mismatches . Mug also shows activity toward epsilonC (3,N4-ethenocytosine) , 8-HM-epsilondC (8-(hydroxymethyl)-3,N4-etheno-2'-deoxycytidine) , 1,N(2)-epsilonG (1,N(2)-ethenoguanine) lesions , and 5-formyluracil lesions. Structural models for the specificity of the enzyme for G:U and G:T base mispairings and for the G:U preference of the enzyme are presented. The substrate specificity of the enzyme is discussed in detail . Mug activity reduces mutation during stationary phase , whereas it does not play a large role in DNA repair during cell growth . A mug mutant exhibits increased mutagenesis during stationary phase, compared to wild type and to an ung mutant . Crystal structures of Mug are presented . Regulation has been described . Mug production is upregulated upon stationary phase entry...

## Biological Role

Catalyzes RXN0-1922 (reaction.ecocyc.RXN0-1922).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

FUNCTION: Excises ethenocytosine and uracil, which can arise by alkylation or deamination of cytosine, respectively, from the corresponding mispairs with guanine in ds-DNA. It is capable of hydrolyzing the carbon-nitrogen bond between the sugar-phosphate backbone of the DNA and the mispaired base. The complementary strand guanine functions in substrate recognition. Required for DNA damage lesion repair in stationary-phase cells. {ECO:0000269|PubMed:12668677, ECO:0000269|PubMed:8878487}.

## Pathways

- `eco03410` Base excision repair (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1922|reaction.ecocyc.RXN0-1922]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3068|gene.b3068]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9H1`
- `KEGG:ecj:JW3040;eco:b3068;ecoc:C3026_16760;`
- `GeneID:93778924;947560;`
- `GO:GO:0003677; GO:0004844; GO:0005737; GO:0006285; GO:0008263`
- `EC:3.2.2.28`

## Notes

G/U mismatch-specific DNA glycosylase (EC 3.2.2.28) (Double-strand-specific uracil glycosylase) (Mismatch-specific uracil DNA-glycosylase) (MUG)
