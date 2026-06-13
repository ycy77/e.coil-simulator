---
entity_id: "gene.b2685"
entity_type: "gene"
name: "emrA"
source_database: "NCBI RefSeq"
source_id: "gene-b2685"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2685"
  - "emrA"
---

# emrA

`gene.b2685`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2685`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

emrA (gene.b2685) is a gene entity. It encodes emrA (protein.P27303). Encoded protein function: FUNCTION: Part of the tripartite efflux system EmrAB-TolC (PubMed:12482849, PubMed:1409590, PubMed:33065135). The system confers resistance to antibiotics such as nalidixic acid and to various hydrophobic compounds, including CCCP, FCCP and 2,4-dinitrophenol (PubMed:12482849, PubMed:1409590, PubMed:33065135). EmrA is a drug-binding protein that provides a physical link between EmrB and TolC (PubMed:12482849, PubMed:33065135). {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590, ECO:0000269|PubMed:33065135}. EcoCyc product frame: EG11354-MONOMER. Genomic coordinates: 2811427-2812599. EcoCyc protein note: EmrA is the membrane fusion protein of a tripartite efflux pump that is implicated in the export of a variety of mainly hydrophobic compounds - carbonylcyanide m-chlorophenylhydrazone (CCCP), tetrachlorosalicyanide (TSA), nalidixate, phenylmercury acetate and others (see CPLX0-2121 for more details). EmrA is anchored to the inner membrane by an N-terminal α-helix; EmrA can form dimers and trimers; the periplasmic domain of EmrA appears to be elongated and contains a drug-binding site . EmrA forms dynamic oligomers on a biochip sensor surface; EmrA forms dimers and trimers in solution; EmrA-TolC interaction can be reconstituted in vitro . emr: E. coli multidrug resistance

## Biological Role

Repressed by mprA (protein.P0ACR9). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27303|protein.P27303]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=emrA; function=+
- `represses` <-- [[protein.P0ACR9|protein.P0ACR9]] `RegulonDB` `S` - regulator=MprA; target=emrA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008838,ECOCYC:EG11354,GeneID:947166`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2811427-2812599:+; feature_type=gene
