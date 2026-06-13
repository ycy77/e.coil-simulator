---
entity_id: "gene.b1508"
entity_type: "gene"
name: "hipB"
source_database: "NCBI RefSeq"
source_id: "gene-b1508"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1508"
  - "hipB"
---

# hipB

`gene.b1508`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1508`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hipB (gene.b1508) is a gene entity. It encodes hipB (protein.P23873). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Neutralizes the toxic effect of cognate toxin HipA (PubMed:20616060). Also neutralizes the toxic effect of non-cognate toxin YjjJ (PubMed:28430938). Binds to operator sites with the consensus sequence 5-'TATCCN(8)GGATA-3' to repress the hipBA operon promoter (PubMed:8021189, PubMed:19150849); binding of HipB(2) to DNA induces a 70 degree bend (PubMed:19150849). This forces HipA dimerization, which blocks HipA's active site and thus its toxic action (PubMed:26222023). May play a role in biofilm formation (PubMed:23329678). {ECO:0000269|PubMed:19150849, ECO:0000269|PubMed:20616060, ECO:0000269|PubMed:23329678, ECO:0000269|PubMed:26222023, ECO:0000269|PubMed:28430938, ECO:0000269|PubMed:8021189}. EcoCyc product frame: EG10442-MONOMER. Genomic coordinates: 1592176-1592442. EcoCyc protein note: HipB is a transcriptional repressor that functions as the antagonist of HipA, which was the first protein found to mediate the phenomenon of persistence in E. coli. A small fraction of cells within a population are dormant persister cells; these cells are phenotypic variants that are not killed by antibiotics, leading to multidrug tolerance (MDT)...

## Biological Role

Repressed by hipB (protein.P23873). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23873|protein.P23873]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hipB; function=+
- `represses` <-- [[protein.P23873|protein.P23873]] `RegulonDB` `S` - regulator=HipB; target=hipB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005024,ECOCYC:EG10442,GeneID:946065`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1592176-1592442:-; feature_type=gene
