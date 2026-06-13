---
entity_id: "protein.P75993"
entity_type: "protein"
name: "ariR"
source_database: "UniProt"
source_id: "P75993"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ariR ymgB b1166 JW1153"
---

# ariR

`protein.P75993`

## Static

- Type: `protein`
- Source: `UniProt:P75993`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably a connector protein for RcsB/C regulation of biofilm and acid-resistance, providing additional signal input into the two-component signaling pathway. May serve to stimulate biofilm maturation, via the Rcs phosphorelay. Regulates expression of genes involved in acid-resistance and biofilm formation, including the RcsB/C two-component system. May be a non-specific DNA-binding protein that binds genes and/or intergenic regions via a geometric recognition. Also confers resistance to H(2)O(2). Overexpression at 28 and 16 degrees Celsius increases the production of colanic acid, an exopolysaccharide and matrix component, and reduces adhesive curli fimbriae expression. Both of these effects require RcsB; AriR probably acts upstream of the RcsB/C system to stimulate the activity and not transcription of RcsB/C. 5-fluorouracil reduction in biofilm formation requires this protein. {ECO:0000269|PubMed:17765265}. AriR appears to be a regulator of acid resistance and biofilm formation. AriR binds DNA, and in vivo target sites were identified by nickel-enrichment DNA microarray studies. In vitro, AriR binds DNA non-specifically . Acting via AriR, 5-fluorouracil inhibits biofilm formation . The crystal structure of a C-terminal proteolytic fragment of AriR has been solved at 1...

## Biological Role

Component of putative two-component system connector protein AriR (complex.ecocyc.CPLX0-7623).

## Annotation

FUNCTION: Probably a connector protein for RcsB/C regulation of biofilm and acid-resistance, providing additional signal input into the two-component signaling pathway. May serve to stimulate biofilm maturation, via the Rcs phosphorelay. Regulates expression of genes involved in acid-resistance and biofilm formation, including the RcsB/C two-component system. May be a non-specific DNA-binding protein that binds genes and/or intergenic regions via a geometric recognition. Also confers resistance to H(2)O(2). Overexpression at 28 and 16 degrees Celsius increases the production of colanic acid, an exopolysaccharide and matrix component, and reduces adhesive curli fimbriae expression. Both of these effects require RcsB; AriR probably acts upstream of the RcsB/C system to stimulate the activity and not transcription of RcsB/C. 5-fluorouracil reduction in biofilm formation requires this protein. {ECO:0000269|PubMed:17765265}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7623|complex.ecocyc.CPLX0-7623]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1166|gene.b1166]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75993`
- `KEGG:ecj:JW1153;eco:b1166;ecoc:C3026_06870;`
- `GeneID:75171267;75203729;945340;`
- `GO:GO:0003677; GO:0042542; GO:0042803; GO:0044010; GO:0071468`

## Notes

Probable two-component-system connector protein AriR
