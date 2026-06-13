---
entity_id: "gene.b4532"
entity_type: "gene"
name: "hicA"
source_database: "NCBI RefSeq"
source_id: "gene-b4532"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4532"
  - "hicA"
---

# hicA

`gene.b4532`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4532`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hicA (gene.b4532) is a gene entity. It encodes hicA (protein.P76106). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. A probable translation-independent mRNA interferase. Overexpression causes cessation of cell growth and inhibits cell proliferation via inhibition of translation; this blockage is overcome (after 90 minutes) by subsequent expression of antitoxin HicB. Overexpression causes cleavage of a number of mRNAs and tmRNA, in a translation-independent fashion, suggesting this is an mRNA interferase (PubMed:19060138). {ECO:0000269|PubMed:19060138}. EcoCyc product frame: MONOMER0-2673. EcoCyc synonyms: yncN. Genomic coordinates: 1509286-1509462. EcoCyc protein note: HicA is an mRNA interferase acting as the toxin of the HicA-HicB toxin-antitoxin system. Overexpression of HicA induces mRNA cleavage and growth inhibition, but not cell death. Expression of HicB neutralizes the effect of HicA . HicA contributes to autoregulation of HicAB expression , likely by affecting the kinetics of DNA binding by HicB . An analysis of the targets and site specificity of HicA showed some cleavage site specificity, favoring an A immediately downstream of the cleavage site. Similar to ribosome-dependent endonuclease toxins, HicA shows a bias towards cleaving before the first position in a codon. Like other E...

## Biological Role

Repressed by hicB (protein.P67697). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76106|protein.P76106]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hicA; function=+
- `represses` <-- [[protein.P67697|protein.P67697]] `RegulonDB` `C` - regulator=HicB; target=hicA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285053,ECOCYC:G0-10451,GeneID:945989`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1509286-1509462:+; feature_type=gene
