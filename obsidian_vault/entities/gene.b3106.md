---
entity_id: "gene.b3106"
entity_type: "gene"
name: "yhaK"
source_database: "NCBI RefSeq"
source_id: "gene-b3106"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3106"
  - "yhaK"
---

# yhaK

`gene.b3106`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3106`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhaK (gene.b3106) is a gene entity. It encodes yhaK (protein.P42624). Encoded protein function: FUNCTION: Does not have quercetin 2,3-dioxygenase activity. {ECO:0000269|PubMed:18561187}. EcoCyc product frame: G7620-MONOMER. Genomic coordinates: 3254319-3255020. EcoCyc protein note: YhaK belongs to a subclass of the bicupin family . The protein may be involved in chloride binding, sensing of oxidative stress , or in the degradation of 2,4-dinitrotoluene (DNT) . A crystal structure of YhaK has been solved . YhaK contains two structurally similar domains that are in a face-to-face arrangement. In the crystal structure, the two domains are crosslinked via a disulfide bond between C10 and C204; a third cysteine, C122, is modified to a sulfenic acid. Residues that coordinate divalent metal ions in pirin-related proteins are not conserved in YhaK, and no metal ion is observed in the crystal structure . YhaK is sensitive to oxidation, forming an intramolecular disulfide bond and oligomeric complexes; oxidation can be attenuated by the thioredoxin and glutaredoxin systems. Unlike the structurally similar YhhW, YhaK does not have quercetinase activity . Expression of yhaK is induced by reactive nitrogen species and by exposure to hydroquinone . Induction by hydroquinone is abolished in a yhaJ mutant, and induction by DNT is enhanced in a yhaK mutant . The yhaK homolog in uropathogenic E...

## Biological Role

Activated by yhaJ (protein.P67660).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42624|protein.P42624]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P67660|protein.P67660]] `RegulonDB` `S` - regulator=YhaJ; target=yhaK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010217,ECOCYC:G7620,GeneID:947620`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3254319-3255020:+; feature_type=gene
