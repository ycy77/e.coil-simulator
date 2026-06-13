---
entity_id: "gene.b2594"
entity_type: "gene"
name: "rluD"
source_database: "NCBI RefSeq"
source_id: "gene-b2594"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2594"
  - "rluD"
---

# rluD

`gene.b2594`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2594`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rluD (gene.b2594) is a gene entity. It encodes rluD (protein.P33643). Encoded protein function: FUNCTION: Responsible for synthesis of pseudouridine from uracil at positions 1911, 1915 and 1917 in 23S ribosomal RNA (PubMed:9814761, PubMed:11087118, PubMed:11453071, PubMed:17937767). Other positions are not modified (PubMed:17937767). Uridine isomerization occurs as a late step during the assembly of the large ribosomal subunit (PubMed:17937767). Member of a network of 50S ribosomal subunit biogenesis factors (ObgE, RluD, RsfS and DarP(YjgA)) which assembles along the 30S-50S interface, allowing 23S rRNA modification and preventing incorrect 23S rRNA structures from forming (PubMed:33639093). {ECO:0000269|PubMed:11087118, ECO:0000269|PubMed:11453071, ECO:0000269|PubMed:17937767, ECO:0000269|PubMed:33639093, ECO:0000269|PubMed:9814761}. EcoCyc product frame: EG12098-MONOMER. EcoCyc synonyms: yfiI, sfhB. Genomic coordinates: 2735031-2736011. EcoCyc protein note: RluD is a pseudouridine synthase that catalyzes pseudouridine formation at positions 1911, 1915, and 1917 in helix 69 (H69) of the 23S rRNA . 23S rRNA modification by RluD occurs in the late assembly phase of the 50S subunit and 70S ribosome . RluD activity is involved in the resuscitation of persister cells...

## Biological Role

Repressed by rybB (gene.b4417).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33643|protein.P33643]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[gene.b4417|gene.b4417]] `RegulonDB` `S` - regulator=RybB; target=rluD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008532,ECOCYC:EG12098,GeneID:947087`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2735031-2736011:-; feature_type=gene
