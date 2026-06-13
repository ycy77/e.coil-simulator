---
entity_id: "gene.b0144"
entity_type: "gene"
name: "gluQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0144"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0144"
  - "gluQ"
---

# gluQ

`gene.b0144`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0144`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gluQ (gene.b0144) is a gene entity. It encodes gluQ (protein.P27305). Encoded protein function: FUNCTION: Catalyzes the tRNA-independent activation of glutamate in presence of ATP and the subsequent transfer of glutamate onto tRNA(Asp). Glutamate is transferred on the 2-amino-5-(4,5-dihydroxy-2-cyclopenten-1-yl) moiety of the queuosine in position 34 of the tRNA(Asp), the wobble position of the QUC anticodon. Does not transfer glutamate to either tRNA(Glu) or tRNA(Gln). The incapacity of the glutamylated tRNA(Asp) to bind elongation factor Tu suggests that it is not involved in ribosomal protein biosynthesis. {ECO:0000269|PubMed:15096594, ECO:0000269|PubMed:15096612, ECO:0000269|PubMed:15150343}. EcoCyc product frame: EG11362-MONOMER. EcoCyc synonyms: yadB. Genomic coordinates: 159186-160112. EcoCyc protein note: Glutamyl-Q tRNAAsp synthetase (Glu-Q-RS, GluQ) catalyzes the addition of a glutamate residue to the queosine-modified wobble base of tRNAAsp. The GluQ protein shows similarity to the amino terminal part of bacterial glutamyl-tRNA synthetases, although it lacks the tRNA anticodon interaction domain . The protein is not capable of using tRNAGlu or tRNAGln as a substrate in vitro or in vivo, but can modify tRNAAsp with glutamate...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27305|protein.P27305]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gluQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000497,ECOCYC:EG11362,GeneID:944846`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:159186-160112:-; feature_type=gene
