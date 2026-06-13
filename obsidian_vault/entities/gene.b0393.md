---
entity_id: "gene.b0393"
entity_type: "gene"
name: "rdgC"
source_database: "NCBI RefSeq"
source_id: "gene-b0393"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0393"
  - "rdgC"
---

# rdgC

`gene.b0393`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0393`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rdgC (gene.b0393) is a gene entity. It encodes rdgC (protein.P36767). Encoded protein function: FUNCTION: May be involved in recombination (PubMed:8807285). Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000269|PubMed:36326440, ECO:0000269|PubMed:8807285}. EcoCyc product frame: EG12158-MONOMER. EcoCyc synonyms: yaiD. Genomic coordinates: 409108-410019. EcoCyc protein note: RdgC is a 34 kDa nucleoid-associated protein believed to function as a regulator of EG10823-MONOMER RecA activity. RdgC inhibits RecA-mediated strand exchange in vitro, probably by competing with RecA for DNA binding sites . RdgC binds non-specifically to both ssDNA and dsDNA and is expressed at high levels in the exponential growth phase . RdgC is essential for growth in recombination-deficient E. coli strains and in strains lacking the primosome factor EG10763-MONOMER PriA . Double-strand DNA breaks accumulate in an ΔrdgC strain; Tn-seq data indicates that rdgC has enhanced importance when priB is deleted . RdgC exists in solution as a mixture of monomers, dimers and tetramers . RdgC crystallises as a dimer and forms a toroidal ring structure proposed to encircle DNA . rdgC: recombination-dependent growth .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36767|protein.P36767]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001366,ECOCYC:EG12158,GeneID:948585`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:409108-410019:-; feature_type=gene
