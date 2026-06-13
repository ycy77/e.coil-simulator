---
entity_id: "gene.b2782"
entity_type: "gene"
name: "mazF"
source_database: "NCBI RefSeq"
source_id: "gene-b2782"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2782"
  - "mazF"
---

# mazF

`gene.b2782`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2782`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mazF (gene.b2782) is a gene entity. It encodes mazF (protein.P0AE70). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. A sequence-specific endoribonuclease it inhibits protein synthesis by cleaving mRNA and inducing bacterial stasis. It is stable, single-strand specific with mRNA cleavage independent of the ribosome, although translation enhances cleavage for some mRNAs (PubMed:18854355). Cleavage occurs at the 5'-end of ACA sequences, yielding a 2',3'-cyclic phosphate and a free 5'-OH, although cleavage can also occur on the 3'-end of the first A (PubMed:15537630, PubMed:23280569). Digests 16S rRNA in vivo 43 nts upstream of the C-terminus; this removes the anti-Shine-Dalgarno sequence forming a mixed population of wild-type and 'stress ribosomes'. Stress ribosomes do not translate leader-containing mRNA but are proficient in translation of leaderless mRNA, which alters the protein expression profile of the cell; MazF produces some leaderless mRNA (PubMed:21944167). The toxic endoribonuclease activity is inhibited by its labile cognate antitoxin MazE. Toxicity results when the levels of MazE decrease in the cell, leading to mRNA degradation. This effect can be rescued by expression of MazE, but after 6 hours in rich medium overexpression of MazF leads to programmed cell death (PubMed:11222603, PubMed:8650219)...

## Biological Role

Repressed by mazE (protein.P0AE72), hipB (protein.P23873). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE70|protein.P0AE70]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=mazF; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=mazF; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=mazF; function=+
- `represses` <-- [[protein.P0AE72|protein.P0AE72]] `RegulonDB` `S` - regulator=MazE; target=mazF; function=-
- `represses` <-- [[protein.P23873|protein.P23873]] `RegulonDB` `S` - regulator=HipB; target=mazF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009119,ECOCYC:EG11249,GeneID:947252`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2910756-2911091:-; feature_type=gene
