---
entity_id: "gene.b2754"
entity_type: "gene"
name: "cas2"
source_database: "NCBI RefSeq"
source_id: "gene-b2754"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2754"
  - "cas2"
---

# cas2

`gene.b2754`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2754`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cas2 (gene.b2754) is a gene entity. It encodes ygbF (protein.P45956). Encoded protein function: FUNCTION: CRISPR (clustered regularly interspaced short palindromic repeat), is an adaptive immune system that provides protection against mobile genetic elements (viruses, transposable elements and conjugative plasmids) (PubMed:21255106, PubMed:24793649, PubMed:24920831). CRISPR clusters contain sequences complementary to antecedent mobile elements and target invading nucleic acids. CRISPR clusters are transcribed and processed into CRISPR RNA (crRNA). The Cas1-Cas2 complex is involved in CRISPR adaptation, the first stage of CRISPR immunity, being required for the addition/removal of CRISPR spacers at the leader end of the CRISPR locus (PubMed:24793649, PubMed:24920831, PubMed:25707795). The Cas1-Cas2 complex introduces staggered nicks into both strands of the CRISPR array near the leader repeat and joins the 5'-ends of the repeat strands with the 3'-ends of the new spacer sequence (PubMed:24920831). Spacer DNA integration requires supercoiled target DNA and 3'-OH ends on the inserted (spacer) DNA and probably initiates with a nucleophilic attack of the C 3'-OH end of the protospacer on the minus strand of the first repeat sequence (PubMed:25707795). Expression of Cas1-Cas2 in a strain lacking both genes permits spacer acquisition (PubMed:24793649, PubMed:24920831)...

## Biological Role

Repressed by hns (protein.P0ACF8), crp (protein.P0ACJ8). Activated by slyA (protein.P0A8W2), stpA (protein.P0ACG1), rpoH (protein.P0AGB3), leuO (protein.P10151).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45956|protein.P45956]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=cas2; function=+
- `activates` <-- [[protein.P0ACG1|protein.P0ACG1]] `RegulonDB` `C` - regulator=StpA; target=cas2; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=cas2; function=+
- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `C` - regulator=LeuO; target=cas2; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=cas2; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=cas2; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009036,ECOCYC:EG12845,GeneID:947213`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2878569-2878853:-; feature_type=gene
