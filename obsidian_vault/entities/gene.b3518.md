---
entity_id: "gene.b3518"
entity_type: "gene"
name: "ccp"
source_database: "NCBI RefSeq"
source_id: "gene-b3518"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3518"
  - "ccp"
---

# ccp

`gene.b3518`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3518`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ccp (gene.b3518) is a gene entity. It encodes ccp (protein.P37197). Encoded protein function: FUNCTION: Cytochrome peroxidase that enables anaerobic respiration with H(2)O(2) as a terminal electron acceptor (PubMed:28696311). It receives electrons from the quinol pool (PubMed:28696311, PubMed:29550214). Menaquinol is probably the electron donor in vivo (PubMed:28696311, PubMed:29550214). It can use menadiol (a menaquinol analog), hydroquinone, duroquinol and the artificial electron donor ABTS(2-) in vitro, but only menadiol and hydroquinone can efficiently transfer electrons to Ccp, maintaining the catalytic activity of the enzyme (PubMed:29550214). It enables E.coli to grow on a nonfermentable carbon source when H(2)O(2) is supplied (PubMed:28696311). Plays a role in the peroxide stress response under anaerobic conditions (PubMed:17464064). However, it does not degrade H(2)O(2) quickly enough to lower the periplasmic H(2)O(2) level below that of the surrounding medium and protect the cell from its toxic effects (PubMed:28696311). {ECO:0000269|PubMed:17464064, ECO:0000269|PubMed:28696311, ECO:0000269|PubMed:29550214}. EcoCyc product frame: EG12244-MONOMER. EcoCyc synonyms: yhjA. Genomic coordinates: 3667791-3669188. EcoCyc protein note: ccp encodes a periplasmic cytochrome c peroxidase (CCP) that enables E...

## Biological Role

Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), oxyR (protein.P0ACQ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37197|protein.P37197]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ccp; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=ccp; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=ccp; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011493,ECOCYC:EG12244,GeneID:948038`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3667791-3669188:-; feature_type=gene
