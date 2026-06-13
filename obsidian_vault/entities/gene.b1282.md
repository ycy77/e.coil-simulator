---
entity_id: "gene.b1282"
entity_type: "gene"
name: "yciH"
source_database: "NCBI RefSeq"
source_id: "gene-b1282"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1282"
  - "yciH"
---

# yciH

`gene.b1282`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1282`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciH (gene.b1282) is a gene entity. It encodes yciH (protein.P08245). Encoded protein function: Uncharacterized protein YciH EcoCyc product frame: EG11128-MONOMER. Genomic coordinates: 1342658-1342984. EcoCyc protein note: YciH has similarity to eIF1, a eukaryotic translation initiation factor which is functionally equivalent to the eubacterial IF3, with the exception of the proofreading function of the IF3 C-terminal domain . YciH is able to perform some of the functions of IF3 in vitro . Purified YciH is able to interact with both the 30S subunit of eubacterial ribosomes and the 40S subunit of eukaryotic ribosomes. Like IF3, YciH reduces ribosomal complex formation at initiation sites with codon-anticodon mismatches and discriminates against initiation complexes formed with mutant tRNAs in vitro . However, a ΔyciH strain shows no difference in translation efficiency of several model mRNAs . A solution structure shows that YciH is a member of a new superfamily of α-β plait domain proteins . A ΔyciH strain displays a small growth defect compared to wild type when grown in minimal medium . The proteome of a ΔyciH strain shows decreased expression of a number of proteins involved in stress responses . In a large genetic interaction screen, yciH showed genetic interactions with a number of proteins involved in translation and ribosome biogenesis .

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08245|protein.P08245]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yciH; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=yciH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004307,ECOCYC:EG11128,GeneID:947058`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1342658-1342984:+; feature_type=gene
