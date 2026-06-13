---
entity_id: "gene.b3859"
entity_type: "gene"
name: "srkA"
source_database: "NCBI RefSeq"
source_id: "gene-b3859"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3859"
  - "srkA"
---

# srkA

`gene.b3859`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3859`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

srkA (gene.b3859) is a gene entity. It encodes srkA (protein.P0C0K3). Encoded protein function: FUNCTION: A protein kinase that (auto)phosphorylates on Ser and Thr residues (PubMed:17302814). Probably acts to suppress the effects of stress linked to accumulation of reactive oxygen species. Protects cells from stress by antagonizing the MazE-MazF TA module, probably indirectly as it has not been seen to phosphorylate MazE, MazF or MazG (PubMed:23416055). Probably involved in the extracytoplasmic stress response (PubMed:9159398). {ECO:0000255|HAMAP-Rule:MF_01497, ECO:0000269|PubMed:17302814, ECO:0000269|PubMed:23416055, ECO:0000269|PubMed:9159398}. EcoCyc product frame: EG11831-MONOMER. EcoCyc synonyms: orfA, yihE. Genomic coordinates: 4042415-4043401. EcoCyc protein note: SrkA is a serine/threonine protein kinase that protects cells from several types of lethal stress . SrkA is able to autophosphorylate at serine and threonine, but not tyrosine residues . The protein kinase activity is required for stress protection by SrkA . SrkA is also able to phosphorylate a general kinase substrate, myelin basic protein, in vitro. The native substrate for SrkA has not been identified yet . A crystal structure of SrkA has been determined at 2.8 Å resolution and shows structural similarity to protein kinases . A D217A mutation abolishes catalytic activity...

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C0K3|protein.P0C0K3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=srkA; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=srkA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012604,ECOCYC:EG11831,GeneID:948346`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4042415-4043401:+; feature_type=gene
