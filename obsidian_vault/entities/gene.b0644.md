---
entity_id: "gene.b0644"
entity_type: "gene"
name: "ybeQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0644"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0644"
  - "ybeQ"
---

# ybeQ

`gene.b0644`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0644`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybeQ (gene.b0644) is a gene entity. It encodes ybeQ (protein.P77234). Encoded protein function: Sel1-repeat-containing protein YbeQ EcoCyc product frame: G6351-MONOMER. Genomic coordinates: 675570-676547. EcoCyc protein note: ybeQ shows differential codon adaptation, resulting in differential translation efficiency signatures, in aerotolerant compared to obligate anaerobic microbes. It was therefore predicted to play a role in the oxidative stress response. A ybeQ deletion mutant was shown to be more sensitive than wild-type specifically to hydrogen peroxide exposure, but not other stresses .

## Biological Role

Repressed by leuO (protein.P10151). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77234|protein.P77234]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ybeQ; function=+
- `represses` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=ybeQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002201,ECOCYC:G6351,GeneID:945251`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:675570-676547:-; feature_type=gene
