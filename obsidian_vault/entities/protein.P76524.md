---
entity_id: "protein.P76524"
entity_type: "protein"
name: "ypdF"
source_database: "UniProt"
source_id: "P76524"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ypdF b2385 JW2382"
---

# ypdF

`protein.P76524`

## Static

- Type: `protein`
- Source: `UniProt:P76524`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes the N-terminal methionine when the next amino acid is alanine, proline or serine. The substrate preference for methionyl aminopeptidase activity is Pro > Ala > Ser. Also able to hydrolyze the Xaa-Pro peptide bond when the first amino acid is alanine, asparagine or methionine. {ECO:0000269|PubMed:15901689}.

## Biological Role

Component of aminopeptidase YpdF (complex.ecocyc.CPLX0-8290).

## Annotation

FUNCTION: Hydrolyzes the N-terminal methionine when the next amino acid is alanine, proline or serine. The substrate preference for methionyl aminopeptidase activity is Pro > Ala > Ser. Also able to hydrolyze the Xaa-Pro peptide bond when the first amino acid is alanine, asparagine or methionine. {ECO:0000269|PubMed:15901689}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8290|complex.ecocyc.CPLX0-8290]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2385|gene.b2385]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76524`
- `KEGG:ecj:JW2382;eco:b2385;ecoc:C3026_13260;`
- `GeneID:946853;`
- `GO:GO:0004177; GO:0006508; GO:0042803; GO:0046914; GO:0070006`
- `EC:3.4.11.-`

## Notes

Aminopeptidase YpdF (EC 3.4.11.-)
