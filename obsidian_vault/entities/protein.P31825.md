---
entity_id: "protein.P31825"
entity_type: "protein"
name: "yfiC"
source_database: "UniProt"
source_id: "P31825"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfiC b2575 JW2559"
---

# yfiC

`protein.P31825`

## Static

- Type: `protein`
- Source: `UniProt:P31825`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the adenine in position 37 of tRNA(1)(Val) (anticodon cmo5UAC). {ECO:0000269|PubMed:19383770}. The 37th position of tRNA, located in the anticodon stem-loop 3'-adjacent to the third nucleotide of the anticodon, is generally occupied by a purine and is often modified. The YfiC protein, also known as TrmM, is responsible for methylation of the A37 nucleotide of tRNAVal1 at the N6 position . The m6A modification is relatively rare in tRNA and mostly observed in bacteria. Under standard growth conditions, a yfiC null mutant has no significant growth defect. However, under osmotic or oxidative stress conditions, the yfiC mutant shows decreased survival . X-ray crystal structures of the protein with and without ADENOSYL-HOMO-CYS were published for the orthologous protein from TAX-2095, which can substitute for YfiC. That protein was shown to require a divalent metal ion for activity .

## Biological Role

Catalyzes S-adenosyl-L-methionine:tRNA1Val (adenine37-N6)-methyltransferase (reaction.ecocyc.RXN-12480).

## Annotation

FUNCTION: Specifically methylates the adenine in position 37 of tRNA(1)(Val) (anticodon cmo5UAC). {ECO:0000269|PubMed:19383770}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-12480|reaction.ecocyc.RXN-12480]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2575|gene.b2575]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31825`
- `KEGG:ecj:JW2559;eco:b2575;ecoc:C3026_14265;`
- `GeneID:947047;`
- `GO:GO:0003676; GO:0005737; GO:0016430; GO:0030488`
- `EC:2.1.1.223`

## Notes

tRNA1(Val) (adenine(37)-N6)-methyltransferase (EC 2.1.1.223) (tRNA m6A37 methyltransferase)
