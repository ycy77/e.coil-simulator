---
entity_id: "protein.P76106"
entity_type: "protein"
name: "hicA"
source_database: "UniProt"
source_id: "P76106"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hicA yncN b4532 JW5230"
---

# hicA

`protein.P76106`

## Static

- Type: `protein`
- Source: `UniProt:P76106`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. A probable translation-independent mRNA interferase. Overexpression causes cessation of cell growth and inhibits cell proliferation via inhibition of translation; this blockage is overcome (after 90 minutes) by subsequent expression of antitoxin HicB. Overexpression causes cleavage of a number of mRNAs and tmRNA, in a translation-independent fashion, suggesting this is an mRNA interferase (PubMed:19060138). {ECO:0000269|PubMed:19060138}. HicA is an mRNA interferase acting as the toxin of the HicA-HicB toxin-antitoxin system. Overexpression of HicA induces mRNA cleavage and growth inhibition, but not cell death. Expression of HicB neutralizes the effect of HicA . HicA contributes to autoregulation of HicAB expression , likely by affecting the kinetics of DNA binding by HicB . An analysis of the targets and site specificity of HicA showed some cleavage site specificity, favoring an A immediately downstream of the cleavage site. Similar to ribosome-dependent endonuclease toxins, HicA shows a bias towards cleaving before the first position in a codon. Like other E. coli endoribonuclease toxins, HicA activity does not affect mature ribosomes, but inhibits ribosome biogenesis, likely by affecting the translation of a specific set of ribosomal proteins...

## Biological Role

Catalyzes RXN0-5509 (reaction.ecocyc.RXN0-5509).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. A probable translation-independent mRNA interferase. Overexpression causes cessation of cell growth and inhibits cell proliferation via inhibition of translation; this blockage is overcome (after 90 minutes) by subsequent expression of antitoxin HicB. Overexpression causes cleavage of a number of mRNAs and tmRNA, in a translation-independent fashion, suggesting this is an mRNA interferase (PubMed:19060138). {ECO:0000269|PubMed:19060138}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5509|reaction.ecocyc.RXN0-5509]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4532|gene.b4532]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76106`
- `KEGG:ecj:JW5230;eco:b4532;ecoc:C3026_08365;`
- `GeneID:75171518;75202358;945989;`
- `GO:GO:0003729; GO:0004521; GO:0006355; GO:0006402; GO:0016787; GO:0040008; GO:0110001`
- `EC:3.1.-.-`

## Notes

Probable mRNA interferase toxin HicA (EC 3.1.-.-) (Endoribonuclease HicA) (Toxin HicA)
