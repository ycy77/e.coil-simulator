---
entity_id: "protein.P0A873"
entity_type: "protein"
name: "trmD"
source_database: "UniProt"
source_id: "P0A873"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trmD b2607 JW2588"
---

# trmD

`protein.P0A873`

## Static

- Type: `protein`
- Source: `UniProt:P0A873`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates guanosine-37 in various tRNAs. {ECO:0000269|PubMed:14583191}. tRNA m1G37 methyltransferase (TrmD) catalyzes the addition of a methyl group to G37 of certain tRNAs . Specificity of this activity is controlled by tRNA structure, specifically including the V, T and D side loops and the presence of G36pG37 . TrmD can accomodate both A and G at position 36 in tRNAAsp and tRNAPhe . Analysis of enzyme activity with truncated tRNAs showed that TrmD minimally requires the anticodon loop and a 9 bp stem in vitro, distinguishing the prokaryotic enzymes from the archaeal and eukaryotic Trm5 . The catalytic mechanisms of TrmD- and Trm5-type enzymes differ, and kinetic assays that distinguish their activities have been described . The m1G37 modification of tRNAs contributes to the prevention of +1 frameshift errors during translation, particularly at the second codon of an open reading frame , and is required for translation of the proline-encoding CC[C/U] codons . CC[C/U] codons at codon 2 are overrepresented in ORFs encoding membrane proteins; accordingly, TrmD deficiency results in a variety of membrane-related phenotypes . Distinct from the frameshifting mechanism, lack of the m1G37 modification leads to ribosome stalling at codons that are normally translated by m1G37-containing tRNAs...

## Biological Role

Catalyzes S-adenosyl-L-methionine:tRNA guanine N1-methyltransferase; (reaction.R00597). Component of tRNA m1G37 methyltransferase (complex.ecocyc.CPLX0-3950).

## Annotation

FUNCTION: Specifically methylates guanosine-37 in various tRNAs. {ECO:0000269|PubMed:14583191}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00597|reaction.R00597]] `KEGG` `database` - via EC:2.1.1.228
- `is_component_of` --> [[complex.ecocyc.CPLX0-3950|complex.ecocyc.CPLX0-3950]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2607|gene.b2607]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A873`
- `KEGG:ecj:JW2588;eco:b2607;ecoc:C3026_14435;`
- `GeneID:93774457;947099;`
- `GO:GO:0000287; GO:0002939; GO:0005829; GO:0030488; GO:0042802; GO:0042803; GO:0052906`
- `EC:2.1.1.228`

## Notes

tRNA (guanine-N(1)-)-methyltransferase (EC 2.1.1.228) (M1G-methyltransferase) (tRNA [GM37] methyltransferase)
