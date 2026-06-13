---
entity_id: "gene.b2828"
entity_type: "gene"
name: "lgt"
source_database: "NCBI RefSeq"
source_id: "gene-b2828"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2828"
  - "lgt"
---

# lgt

`gene.b2828`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2828`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lgt (gene.b2828) is a gene entity. It encodes lgt (protein.P60955). Encoded protein function: FUNCTION: Catalyzes the transfer of the diacylglyceryl group from phosphatidylglycerol to the sulfhydryl group of the N-terminal cysteine of a prolipoprotein, the first step in the formation of mature lipoproteins. {ECO:0000255|HAMAP-Rule:MF_01147, ECO:0000269|PubMed:26729647, ECO:0000269|PubMed:7896715, ECO:0000269|PubMed:8051048}. EcoCyc product frame: EG12128-MONOMER. EcoCyc synonyms: umpA. Genomic coordinates: 2965162-2966037. EcoCyc protein note: Lgt catalyses the transfer of an sn-1,2-diacylglyceryl group from phosphatidylglycerol to the sulfhydryl group of the prospective N-terminal cysteine of a proliporotein . It is the first of 3 sequential reactions (catalysed by Lgt, EG10548-MONOMER and EG10168-MONOMER respectively) that result in the formation of mature triacylated lipoproteins, including EG10544-MONOMER. Lgt is an essential inner membrane protein . lgt (formerly umpA) mutants are defective in diacylglycerol modification of prolipoprotein in vitro and in vivo . Lgt contains 7 transmembrane segments; the N-terminus faces the periplasm and the C-terminus faces the cytoplasm . Lgt is a peripheral membrane protein associating loosely with the cytoplasmic face of the inner membrane...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60955|protein.P60955]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lgt; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009270,ECOCYC:EG12128,GeneID:947303`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2965162-2966037:-; feature_type=gene
