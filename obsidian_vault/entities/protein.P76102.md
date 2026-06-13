---
entity_id: "protein.P76102"
entity_type: "protein"
name: "insQ"
source_database: "UniProt"
source_id: "P76102"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "insQ tnpB ydcM b1432 JW5228"
---

# insQ

`protein.P76102`

## Static

- Type: `protein`
- Source: `UniProt:P76102`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: An RNA-guided dsDNA endonuclease. When guided by an RNA derived from the right-end element of its insertion sequence element (IS), cleaves DNA downstream of the transposon-associated motif (TAM). Cleaves supercoiled and linear DNA in a staggered manner 15-21 bases from the TAM yielding 5'-overhangs. Binds reRNA, an approximately 150 nucleotide base sRNA derived from the 3' end of its own gene, the right end (RE) of the insertion sequence (IS) plus sequence downstream of the IS. {ECO:0000250|UniProtKB:Q7DF80}.; FUNCTION: Not required for transposition of the insertion element. The corresponding transposase in strains MG1655 and W3110 is a truncated pseudogene (yncK). {ECO:0000305}. The insertion sequence in which this gene is found (group IS609) is identified in the ISfinder database () as falling within IS family IS200/IS605. The IS609 group is also found in some other E. coli, such as substrain W3110 and the pathogenic substrain O157:H7, and some Shigella species. The InsQ protein shares 34-36% amino acid identity with TnpA protein in TAX-243230, which is located adjacent to an IS200/IS605-like transposase and has been shown to function as a RNA-guided DNA endonuclease ; however, this has not been demonstrated in E. coli K-12 MG1655.

## Annotation

FUNCTION: An RNA-guided dsDNA endonuclease. When guided by an RNA derived from the right-end element of its insertion sequence element (IS), cleaves DNA downstream of the transposon-associated motif (TAM). Cleaves supercoiled and linear DNA in a staggered manner 15-21 bases from the TAM yielding 5'-overhangs. Binds reRNA, an approximately 150 nucleotide base sRNA derived from the 3' end of its own gene, the right end (RE) of the insertion sequence (IS) plus sequence downstream of the IS. {ECO:0000250|UniProtKB:Q7DF80}.; FUNCTION: Not required for transposition of the insertion element. The corresponding transposase in strains MG1655 and W3110 is a truncated pseudogene (yncK). {ECO:0000305}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1432|gene.b1432]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76102`
- `KEGG:ecj:JW5228;eco:b1432;`
- `GeneID:944942;`
- `GO:GO:0003677; GO:0004519; GO:0006310; GO:0016787; GO:0032196; GO:0046872`
- `EC:3.1.21.-`

## Notes

Putative RNA-guided DNA endonuclease InsQ (EC 3.1.21.-)
