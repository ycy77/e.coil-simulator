---
entity_id: "protein.P0A784"
entity_type: "protein"
name: "orn"
source_database: "UniProt"
source_id: "P0A784"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "orn o204a yjeR b4162 JW5740"
---

# orn

`protein.P0A784`

## Static

- Type: `protein`
- Source: `UniProt:P0A784`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: 3'-to-5' exoribonuclease specific for small oligoribonucleotides 2 to 5 nucleotides in length, as well as small (2 to 5 nucleotides) ssDNA oligomers. Probably responsible for the final step in mRNA degradation. {ECO:0000269|PubMed:16682444, ECO:0000269|PubMed:7608090, ECO:0000269|PubMed:9573169}. Oligoribonuclease (Orn) is a processive 3'-to-5' exoribonuclease specific for short oligoribonucleotides . Short RNAs, from 2-7 nucleotides in length, accumulate in the cell during RNA degradation, because they are not good substrates for general exoribonucleases. Orn recycles these short RNA oligonucleotides into mononucleotides. The activity on very short oligoribonucleotides is not shared with other exoribonucleases in E. coli . Orn is the only known exoribonuclease enzyme that is essential for growth in E. coli, indicating the importance of its function . Orn from TAX-287 was shown to cleave the dinucleotide L-DI-GMP, which is formed from the second messanger C-DI-GMP by EC-3.1.4.52 . Orn binds adenosine-3',5'-bisphosphate (pAp), but does not hydrolyze it under the conditions tested . Crystal structures of Orn have been solved . A study of recombinant Orn from TAX-666 has found that the enzyme exhibits a strong substrate preference for diribonucleotides, and the crystal structure revealed an active site optimized for diribonucleotides...

## Biological Role

Component of oligoribonuclease (complex.ecocyc.CPLX0-1821).

## Enriched Pathways

- `eco03008` Ribosome biogenesis in eukaryotes (KEGG)

## Annotation

FUNCTION: 3'-to-5' exoribonuclease specific for small oligoribonucleotides 2 to 5 nucleotides in length, as well as small (2 to 5 nucleotides) ssDNA oligomers. Probably responsible for the final step in mRNA degradation. {ECO:0000269|PubMed:16682444, ECO:0000269|PubMed:7608090, ECO:0000269|PubMed:9573169}.

## Pathways

- `eco03008` Ribosome biogenesis in eukaryotes (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1821|complex.ecocyc.CPLX0-1821]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4162|gene.b4162]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A784`
- `KEGG:ecj:JW5740;eco:b4162;ecoc:C3026_22495;`
- `GeneID:93777660;948675;`
- `GO:GO:0000175; GO:0003676; GO:0005829; GO:0006401; GO:0008310; GO:0046872`
- `EC:3.1.15.-`

## Notes

Oligoribonuclease (EC 3.1.15.-)
