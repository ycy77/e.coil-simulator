---
entity_id: "gene.b0697"
entity_type: "gene"
name: "kdpB"
source_database: "NCBI RefSeq"
source_id: "gene-b0697"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0697"
  - "kdpB"
---

# kdpB

`gene.b0697`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0697`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdpB (gene.b0697) is a gene entity. It encodes kdpB (protein.P03960). Encoded protein function: FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894, PubMed:2849541, PubMed:8499455). This subunit is responsible for energy coupling to the transport system and for the release of the potassium ions to the cytoplasm (PubMed:16354672, PubMed:30478378, PubMed:34272288). {ECO:0000269|PubMed:16354672, ECO:0000269|PubMed:23930894, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:30478378, ECO:0000269|PubMed:34272288, ECO:0000269|PubMed:8499455}. EcoCyc product frame: KDPB-MONOMER. EcoCyc synonyms: kac. Genomic coordinates: 724988-727036. EcoCyc protein note: KdpB is the largest subunit of a potassium ion importing P-type ATPase; KdpB forms a phosphorylated intermediate as part of the transport cycle . KdpB contains seven transmembrane (TM) helices and two large cytoplasmic domains; the first of these is located between TM 2 and 3 and is known as the actuator- or A-domain; the second is located between TM 4 and 5 and consists of a phosphorylation- or P-domain and a nucleotide-binding- or N-domain (see and ). Asp-307, within the conserved DKTGT motif in the P-domain is the site of transient phosphorylation...

## Biological Role

Activated by rpoD (protein.P00579), kdpE (protein.P21866).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03960|protein.P03960]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kdpB; function=+
- `activates` <-- [[protein.P21866|protein.P21866]] `RegulonDB` `C` - regulator=KdpE; target=kdpB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002376,ECOCYC:EG10514,GeneID:947450`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:724988-727036:-; feature_type=gene
