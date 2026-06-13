---
entity_id: "gene.b3406"
entity_type: "gene"
name: "greB"
source_database: "NCBI RefSeq"
source_id: "gene-b3406"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3406"
  - "greB"
---

# greB

`gene.b3406`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3406`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

greB (gene.b3406) is a gene entity. It encodes greB (protein.P30128). Encoded protein function: FUNCTION: Necessary for efficient RNA polymerase transcription elongation past template-encoded arresting sites. The arresting sites in DNA have the property of trapping a certain fraction of elongating RNA polymerases that pass through, resulting in locked ternary complexes. Cleavage of the nascent transcript by cleavage factors such as GreA or GreB allows the resumption of elongation from the new 3'terminus. GreB releases sequences of up to 9 nucleotides in length. {ECO:0000255|HAMAP-Rule:MF_00930, ECO:0000269|PubMed:8431948}. EcoCyc product frame: EG11578-MONOMER. Genomic coordinates: 3536812-3537288. EcoCyc protein note: GreB stimulates the mRNA cleavage activity of RNA polymerase , which acts to release a polymerase complex that has stalled . GreB stimulates shortening of the 3' end of the transcript by 9 nucleotides or less , and the new 3' end is subject to elongation by RNA polymerase . GreB decreases abortive initiation and increases productive initiation . GreB (and GreA) is also required for wild-type transcription of some regulatory regions within lambda phage . GreB activity during transcription from a lambda phage promoter requires that GreB associate with RNA polymerase before RNA transcription begins...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30128|protein.P30128]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=greB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011117,ECOCYC:EG11578,GeneID:2847706`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3536812-3537288:+; feature_type=gene
